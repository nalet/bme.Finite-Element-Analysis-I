########################################################################################################################
# Import needed modules
import os
import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import minimize, fmin
import time


########################################################################################################################
def read_odbreport(filename):
    """
    Parses ODB report into a dictionary whose lables are the variables names and items the vectors (time, variable)
    :param filename: string containing the name of the odb_report.csv file
    :return: dictionary containing all the variables data
    """
    # Initialize values
    output = {}
    aux_data = []

    # Open odb report file
    with open(filename, 'r') as report:
        for line in report:
            # Split line in quotation marks
            check = line.strip().split("'")

            # Check if it is an History Output
            if check[0].strip() == 'History Output':

                # Dump information if it is not the previous History Output
                if len(aux_data) != 0:
                    # Save current data
                    output[current_var] = np.array(aux_data)

                # Extract variable
                current_var = check[1].strip()

                # Create dictionary entry with new variable
                output[current_var] = {}

                # Reset auxiliary data
                aux_data = []

                continue

            # Check if the parsed line is a number. If not, it continues
            check = check[0].split(',')

            # Convert first float
            try:
                num1 = float(check[0])
            except ValueError:
                continue

            # Convert second float
            num2 = float(check[1].strip())

            # Store pair of values
            aux_data.append([num1, num2])

    # Save last iteration
    output[current_var] = np.array(aux_data)

    return output


########################################################################################################################
def calculate_cost(parameters, D, kappa, name_abaqus_job, name_abaqus_inp, name_exp_data):
    """
    Cost function to minimize. Receives the material parameters to optimize, executes Abaqus analysis, Abaqus ODB report
    and calculates the cost
    :param parameters: array or list of material parameters to be optimized
    :param D: Compressibility (constant)
    :param kappa: Dispersion (constant)
    :param name_abaqus_job: name of the abaqus simulation (e.g., Job-1)
    :param name_abaqus_inp: name of the abaqus INP file (contains CAE instructions. E.g., sample-45.inp)
    :param name_exp_data: name of the text file containing the experimental data to fit
    :return: cost function (scalar function)
    """
    # File names
    name_odbreport = name_abaqus_job + '_results'

    # Complete the parameters
    model_parameter = np.zeros(5)
    model_parameter[0] = parameters[0]
    model_parameter[1] = D
    model_parameter[2] = parameters[1]
    model_parameter[3] = parameters[2]
    model_parameter[4] = kappa

    # Penalize unrealistic values of the parameters and calculate cost function

    if model_parameter[0] < 1e-3 or model_parameter[1] < 1e-3 or model_parameter[2] < 1e-3:
        cost = 1000000
    else:
        # Clean directory before submitting abaqus simulation
        os.system('rm %s.com %s.dat %s.msg %s.odb %s.prt %s.sim %s.sta'
                  % (name_abaqus_job, name_abaqus_job, name_abaqus_job, name_abaqus_job,
                     name_abaqus_job, name_abaqus_job, name_abaqus_job))
        os.system('rm %s.csv' % name_odbreport)
        os.system('rm param.inp')

        # Write parameters to file and execute Abaqus
        fid = open('param.inp', 'w')
        fid.write('*Parameter\n')
        fid.write('C10=%1.6f\n' % model_parameter[0])
        fid.write('D=%1.6e\n' % model_parameter[1])
        fid.write('k1=%1.6f\n' % model_parameter[2])
        fid.write('k2=%1.6f\n' % model_parameter[3])
        fid.write('kappa=%1.6f\n' % model_parameter[4])
        fid.close()

        # Execute abaqus command -> REPLACE WITH COMMAND IN VM!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        os.system('abaqus job=%s inp=%s -interactive' % (name_abaqus_job, name_abaqus_inp))

        # Generate report
        os.system('abaqus odbreport j=%s odb=%s history mode=csv' % (name_odbreport, name_abaqus_job))

        # Read experimental results
        exp_data = np.loadtxt(name_exp_data, skiprows=1, delimiter=',')

        # Read Abaqus results
        odb_results = read_odbreport('%s.csv' % name_odbreport)
        displacement = odb_results['U2'][:, 1]
        force = odb_results['RF2'][:, 1]
        abaqus_results = np.c_[displacement, force]

        # Make sure to have unique grid on the exp data
        # and interpolate the experimental data to have
        # the values at the displacements simulated by
        # Abaqus

        # Filter unique values for experimental response
        unique_cxl_disp, index = np.unique(exp_data[:, 0], return_index=True)
        unique_cxl_force = exp_data[index, 1]
        exp_data = np.c_[unique_cxl_disp, unique_cxl_force]

        # Create interpolation for abaqus results
        sp_abaqus = interp1d(abaqus_results[:, 0], abaqus_results[:, 1], kind='linear', fill_value='extrapolate')

        # Re-evaluate abaqus data for making it coincident with experimental values
        abaqus_results = np.c_[exp_data[:, 0], sp_abaqus(exp_data[:, 0])]

        # Calculate the loss function
        cost = np.linalg.norm(exp_data[:, 1] - abaqus_results[:, 1]) / abaqus_results.shape[0]

    # Show the current status of the optimization
    print('Current value of the cost: %1.6f\n' % cost)
    print('Optimal parameter:\n')
    print('    C10:    %1.6f\n\n' % model_parameter[0])
    print('    k1:    %1.6f\n\n' % model_parameter[1])
    print('    k2:    %1.6f\n\n' % model_parameter[2])
        

    return cost


########################################################################################################################
def optimization():
    """
    Main function that launches optimization
    :return:
    """
    # Initialize time tracking
    start = time.time()

    # Fix parameters and user names
    D = 1e-2  # Fixed compressibility
    kappa = 0.2  # Fixed dispersion

    name_abaqus_inp = 'sample-45' #input('Introduce the name of your INP file (e.g., sample-45): ')  # Only in Python 3
    print('Introduce the name of your INP file (e.g., sample-45): ' + name_abaqus_inp)
    name_abaqus_job = 'Job-2' #input('Introduce the name of your Job file (e.g., Job-1): ')  # Only in Python 3
    print('Introduce the name of your Job file (e.g., Job-1): ' + name_abaqus_job)
    name_exp_data = 'exp_data_control.3p.dat' #input('Introduce the name of your experimental data file (e.g., exp_data_control.dat): ')
    print('Introduce the name of your experimental data file (e.g., exp_data_control.dat): ' + name_exp_data)

    # Initial guess
    parameters0 = np.array([5.5e-2,10,80])  # change according to parameter c10

    # Optimization
    #  minimize(fun, x0, args=()
    #  - fun: calculate_cost. The first variable is the one to be minimized. The rest are arguments that can be passed
    # in, but not minimized
    # - x0: parameters0. Initial guess for the minimization algorithm
    # - args: tuple of arguments that can be passed in into the minimization function to solve it. BUT, they are constant.
    # (i.e., are not changed by the optimizer)

    res_opt = minimize(calculate_cost, parameters0,
                       args=(D, kappa, name_abaqus_job, name_abaqus_inp, name_exp_data),
                       method='Nelder-Mead',
                       tol=0.001,
                       options={'maxiter': None, 'maxfev': None, 'disp': False, 'return_all': False,
                                'initial_simplex': None, 'xatol': 0.0001, 'fatol': 0.0001, 'adaptive': False})

    # Delete exiting file with optimal values (from previous run)
    log_file = name_abaqus_job + '_optimal_values.txt'
    if os.path.isfile(log_file):
        os.system('rm %s' % log_file)

    # Write optimal values
    optim = open(log_file, 'w')
    optim.write('############### FINAL LOG FILE!\n\n')
    optim.write('%s\n' % res_opt.message)
    optim.write('Exit flag:                          %i\n\n' % res_opt.success)
    optim.write('Number of iterations:                %i \n\n' % res_opt.nit)
    optim.write('Number function evaluation:         %i \n\n' % res_opt.nfev)
    optim.write('Final value of the cost function:   %s\n\n' % res_opt.fun)
    optim.write('Execution time (s): %1.3f\n\n' % (time.time() - start))
    optim.write('Optimal parameters:\n')
    optim.write('\t\tC10:    %1.6f\n' % res_opt.x[0])
    optim.write('\t\tk1:    %1.6f\n' % res_opt.x[1])
    optim.write('\t\tk2:    %1.6f\n' % res_opt.x[2])
    optim.close()

    os.system('cat %s' % log_file)


########################################################################################################################
def main():
    """
    Just for standalone execution
    :return:
    """
    optimization()


if __name__ == "__main__":
    main()

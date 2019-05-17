import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_rpt(filename) :
    # Import data using Pandas. Using report I XY data, this line should work
    data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '/' + filename,
                    skiprows=5, header=None, delim_whitespace=True)
    
    return data.values

def read_dat(filename) :
    # Import data using Pandas. Using report I XY data, this line should work
    data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '/' + filename)
    
    return data.values

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



exp_data_control = read_dat("exp_data_control.dat") # [:,0] = U(mm), [:,1] = F(N)
exp_data_cxl = read_dat("exp_data_cxl.dat") # [:,0] = U(mm), [:,1] = F(N)
sample_45_simple_result = read_odbreport("Job-1_results.csv")
sample_45_3p_result = read_odbreport("Job-2_results.csv")

# Plot
plt.grid()
plt.plot(exp_data_control[:,0], exp_data_control[:,1], linewidth=2, label="control")
plt.plot(exp_data_cxl[:,0], exp_data_cxl[:,1], linewidth=2, label="CXL")
plt.plot(sample_45_simple_result['U2'][:, 1], sample_45_simple_result['RF2'][:, 1], linewidth=2, label="simple optimization result 45")
plt.plot(sample_45_3p_result['U2'][:, 1], sample_45_3p_result['RF2'][:, 1], linewidth=2, linestyle=":", label="optimization 3p 45")
plt.xlabel('Displacement (mm)')
plt.ylabel('Force(N)')
plt.ylim(bottom=0)
plt.legend()
plt.show()

sample_45_stress_displacement = read_rpt("sample_45_stress_displacement.rpt")
sample_30_stress_displacement = read_rpt("sample_30_stress_displacement.rpt")

# Plot
plt.grid()
plt.plot(sample_45_stress_displacement[:,1], sample_45_stress_displacement[:,2], linewidth=2, label="45° Rotation")
plt.plot(sample_30_stress_displacement[:,1], sample_30_stress_displacement[:,2], linewidth=2, label="30° Rotation")
plt.xlabel('Displacement (mm)')
plt.ylabel('Force(N)')
plt.ylim(bottom=0)
plt.legend()
plt.show()
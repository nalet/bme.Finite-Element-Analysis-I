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

result10 = read_rpt("result10.rpt")
result50 = read_rpt("result50.rpt")

# Plot
plt.grid()
plt.plot(result10[:,1], result10[:,4], linewidth=2, label="0.01 mm")
plt.plot(result50[:,1], result50[:,4], linewidth=2, label="0.05 mm", linestyle=":")
plt.xlabel('Stress (Pascal)')
plt.ylabel('Temp (°C)')
plt.ylim(bottom=0)
plt.legend()
plt.show()
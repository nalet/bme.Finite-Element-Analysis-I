import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_rpt(filename) :
    # Import data using Pandas. Using report I XY data, this line should work
    data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '/' + filename,
                    skiprows=5, header=None, delim_whitespace=True)
    
    return data.values



shape_45_data_u2_rf2 = read_rpt("shape_45_data_u2_rf2.rpt") #[:,1] = RF2, [:,2] = U2

# Plot
plt.grid()
plt.plot(shape_45_data_u2_rf2[:,2], shape_45_data_u2_rf2[:,1], linewidth=2, label="Control")
plt.xlabel('Discplacement (mm)')
plt.ylabel('Force(N)')
plt.ylim(bottom=0)
plt.legend()
plt.show()
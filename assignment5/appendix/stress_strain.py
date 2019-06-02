import os
import numpy as np
import pandas as pd
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import sys

plt.rcParams['figure.dpi'] = 120
plt.rcParams['font.size'] = 15


h = 0.010 / 2
h_max = 0.005 / 2
step_size = 0.0001

sigma_start = 0
sigma_step = 10e6
sigma0 = 220e6
B = 3e9
E = 70e9
n = 3.2

w = 0.2
b = 0.03 / 2

h_x = np.arange(h, h_max, step_size)

x = []
y = []

current = sigma_start
c_y = 0
while c_y <= 1:
    c_y = 0
    c_x = current
    current = current + sigma_step

    if c_x == 0:
        x.append(0)
        y.append(0)
        print('{:.4e}'.format(0),'{:.4e}'.format(0),sep="\t")
        continue

    if c_x >= sigma0:
        c_y = sigma0 / E + sigma0 / B * ( c_x / sigma0 - 1 ) ** n
    else:
        c_y = c_x / E

    x.append(c_x)
    y.append(c_y)
    print('{:.4e}'.format(c_x),'{:.4e}'.format(c_y),sep="\t")
    
def read_data(filename) :
    # Import data using Pandas. Using report I XY data, this line should work
    data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '/' + filename,
                    skiprows=5, header=None, delim_whitespace=True)
    data = data.values

    x_f = []
    y_f = []

    for line in data:
        current3 = line[1]
        current2 = line[2]
        calc2 = h - current2
        c_epsilon2 = (2/np.sqrt(3))*np.log(h/calc2)
        c_sigma2 = (current3 / w * b) * (np.sqrt(3)/2) * (1e4 / 2)
        x_f.append(c_sigma2)
        y_f.append(c_epsilon2)

    return [x_f, y_f]

no_fillet_friction_less_finite_sliding_surface_to_surface = read_data("no_fillet_friction_less_finite_sliding_surface_to_surface.rpt")


# Plot
plt.grid()
plt.plot(x, y, linewidth=2, label="Analytical Solution")
plt.plot(no_fillet_friction_less_finite_sliding_surface_to_surface[0],no_fillet_friction_less_finite_sliding_surface_to_surface[1], linewidth=1, label="Finite Sliding - Surface to Surface - No Friction")
plt.ylabel('Strain')
plt.xlabel('Stress (Pa)')
plt.title('No Fillet')
plt.ylim(bottom=0)
plt.legend()
plt.show()


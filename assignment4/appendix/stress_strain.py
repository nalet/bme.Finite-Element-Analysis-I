import os
import numpy as np
import pandas as pd
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import sys

plt.rcParams['figure.dpi'] = 120
plt.rcParams['font.size'] = 15


h = 10
step_size = 0.0001

sigma_start = 0
sigma_step = 10e6
sigma0 = 220e6
B = 3e9
E = 70e9
n = 3.2

w = 275
b = 30

x = []
y = []

current = sigma_start
c_x = 0
while c_x <= 1:
    c_x = 0
    c_y = current
    current = current + sigma_step

    if c_y == 0:
        x.append(0)
        y.append(0)
        print('{:.4e}'.format(0),'{:.4e}'.format(0),sep="\t")
        continue

    if c_y >= sigma0:
        c_x = sigma0 / E + sigma0 / B * ( c_y / sigma0 - 1 ) ** n
    else:
        c_x = c_y / E

    x.append(c_x)
    y.append(c_y)
    print('{:.4e}'.format(c_y),'{:.4e}'.format(c_x),sep="\t")
    
def read_data(filename) :
    # Import data using Pandas. Using report I XY data, this line should work
    data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '/' + filename,
                    skiprows=5, header=None, delim_whitespace=True)
    data = data.values

    x_f = [0]
    y_f = [0]
    print(filename)
    for line in data:
        rf2 = abs(line[1]) # force
        u2 = abs(line[2]) # displacement
    
        epsilon2 = np.log(h/(h-u2))
        sigma2 = rf2 / w * b

        epsilon_bar = 2 / np.sqrt(3) * epsilon2
        sigma_bar = np.sqrt(3) / 2 * sigma2

        x_f.append(epsilon_bar)
        y_f.append(sigma_bar)
        
        print('{:.4e}'.format(sigma_bar),'{:.4e}'.format(epsilon_bar),sep="\t")
        

    return [x_f, y_f]

no_fillet_friction_less_finite_sliding_surface_to_surface = read_data("no_fillet_friction_less_finite_sliding_surface_to_surface.rpt")


# Plot
plt.grid()
plt.plot(x, y, linewidth=1, label="Analytical Solution")
plt.plot(no_fillet_friction_less_finite_sliding_surface_to_surface[0],no_fillet_friction_less_finite_sliding_surface_to_surface[1], linewidth=1, label="Finite Sliding - Surface to Surface - No Friction")
plt.xlabel('Strain')
plt.ylabel('Stress (Pa)')
plt.title('No Fillet')
plt.ylim(bottom=0)
plt.legend()
plt.show()


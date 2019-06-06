import os
import numpy as np
import pandas as pd
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import sys

plt.rcParams['figure.dpi'] = 120
plt.rcParams['font.size'] = 9




sigma_start = 0
sigma_step = 10
sigma0 = 220
B = 3e3
E = 70e3
n = 3.2

w = 20
b = 0.030 / 2 # symmetric
h = 0.010

eh = 0.005
ew = 0.0007
eb = 0.030 / 2 # symmetric

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
    try:
        # Import data using Pandas. Using report I XY data, this line should work
        data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '/' + filename,
                        skiprows=5, header=None, delim_whitespace=True)
    except:
        print('File ' + filename + ' not found')
    data = data.values

    x_f = [0]
    y_f = [0]
    print(filename)
    for line in data:
        rf2 = abs(line[1]) # force
        u2 = abs(line[2]) # displacement
    
        epsilon2 = np.log(h/(h-u2))
        sigma2 = rf2 / ( w * b )

        epsilon_bar = 2 / np.sqrt(3) * epsilon2
        sigma_bar = np.sqrt(3) / 2 * sigma2

        x_f.append(epsilon_bar)
        y_f.append(sigma_bar)
        
        print('{:.4e}'.format(sigma_bar),'{:.4e}'.format(epsilon_bar),sep="\t")
        

    return [x_f, y_f]

def read_data_e(filename) :
    try:
        # Import data using Pandas. Using report I XY data, this line should work
        data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '/' + filename,
                        skiprows=5, header=None, delim_whitespace=True)
    except:
        print('File ' + filename + ' not found')
    data = data.values

    x_f = [0]
    y_f = [0]
    print(filename)
    for line in data:
        rf2 = abs(line[1]) # force
        u2 = abs(line[2]) # displacement
    
        epsilon2 = np.log(eh/(eh-u2))
        sigma2 = rf2 / ( ew * eb )

        epsilon_bar = 2 / np.sqrt(3) * epsilon2
        sigma_bar = np.sqrt(3) / 2 * sigma2

        x_f.append(epsilon_bar)
        y_f.append(sigma_bar)
        
        print('{:.4e}'.format(sigma_bar),'{:.4e}'.format(epsilon_bar),sep="\t")
        

    return [x_f, y_f]

no_fillet_friction_less_finite_sliding_surface_to_surface = read_data("../../assignment4/appendix/no_fillet_friction_less_finite_sliding_surface_to_surface.rpt")
no_fillet_friction_less_finite_sliding_node_to_surface = read_data("../../assignment4/appendix/no_fillet_friction_less_finite_sliding_node_to_surface.rpt")
no_fillet_friction_less_small_sliding_surface_to_surface = read_data("../../assignment4/appendix/no_fillet_friction_less_small_sliding_surface_to_surface.rpt")
no_fillet_friction_less_small_sliding_node_to_surface = read_data("../../assignment4/appendix/no_fillet_friction_less_small_sliding_node_to_surface.rpt")

no_fillet_friction_02_finite_sliding_surface_to_surface = read_data("../../assignment4/appendix/no_fillet_friction_02_finite_sliding_surface_to_surface.rpt")
no_fillet_friction_02_finite_sliding_node_to_surface = read_data("../../assignment4/appendix/no_fillet_friction_02_finite_sliding_node_to_surface.rpt")
no_fillet_friction_02_small_sliding_surface_to_surface = read_data("../../assignment4/appendix/no_fillet_friction_02_small_sliding_surface_to_surface.rpt")
no_fillet_friction_02_small_sliding_node_to_surface = read_data("../../assignment4/appendix/no_fillet_friction_02_small_sliding_node_to_surface.rpt")

eulerian = read_data_e("eulerian.rpt")
eulerian_friction = read_data_e("eulerian_friction.rpt")

# Plot
plt.grid()
plt.plot(x, y, linewidth=1, alpha=0.5, label="Analytical Solution")


plt.plot(no_fillet_friction_less_finite_sliding_surface_to_surface[0],no_fillet_friction_less_finite_sliding_surface_to_surface[1], linewidth=1, alpha=0.5, label="friction less - finite sliding - surface to surface")
plt.plot(no_fillet_friction_less_finite_sliding_node_to_surface[0],no_fillet_friction_less_finite_sliding_node_to_surface[1], linewidth=1, alpha=0.5, label="friction less - finite sliding - node to surface")
plt.plot(no_fillet_friction_less_small_sliding_surface_to_surface[0],no_fillet_friction_less_small_sliding_surface_to_surface[1], linewidth=1, alpha=0.5, label="friction less - small sliding - surface to surface")
plt.plot(no_fillet_friction_less_small_sliding_node_to_surface[0],no_fillet_friction_less_small_sliding_node_to_surface[1], linewidth=1, alpha=0.5, label="friction less - small sliding - node to surface")

plt.plot(no_fillet_friction_02_finite_sliding_surface_to_surface[0],no_fillet_friction_02_finite_sliding_surface_to_surface[1], linewidth=1, alpha=0.5, label="with friction - finite sliding - surface to surface")
plt.plot(no_fillet_friction_02_finite_sliding_node_to_surface[0],no_fillet_friction_02_finite_sliding_node_to_surface[1], linewidth=1, alpha=0.5, label="with friction - finite sliding - node to surface")
plt.plot(no_fillet_friction_02_small_sliding_surface_to_surface[0],no_fillet_friction_02_small_sliding_surface_to_surface[1], linewidth=1, alpha=0.5, label="with friction - small sliding - surface to surface")
plt.plot(no_fillet_friction_02_small_sliding_node_to_surface[0],no_fillet_friction_02_small_sliding_node_to_surface[1], linewidth=1, alpha=0.5, label="with friction - small sliding - node to surface")

plt.plot(eulerian[0],eulerian[1], linewidth=2, alpha=1, linestyle='dashed', label="friction less - eulerian")
plt.plot(eulerian_friction[0],eulerian_friction[1], linewidth=2, alpha=1, linestyle='dashed', label="with friction - eulerian")



plt.xlabel('Strain')
plt.ylabel('Stress (Pa)')
plt.title('Compare Eulerian Approach with Assignment 4 No Fillet Approach')
plt.ylim(bottom=0)
plt.legend()
plt.show()
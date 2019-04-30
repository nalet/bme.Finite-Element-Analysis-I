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
step_size = 0.00025

sigma0 = 220e6
B = 3e9
E = 70e9
n = 3.2

w = 0.2
b = 0.03 / 2

print('{:.4e}'.format(sigma0),'{:.4e}'.format(B),'{:.4e}'.format(E),'{:.4e}'.format(n),sep="\t")

h_x = np.arange(h, h_max, step_size)

x = []
y = []

current = h
while current >= h_max - step_size:
    c_epsilon = (2/np.sqrt(3))*np.log(h/current)
    c_sigma = ( ( ( ( c_epsilon - (sigma0/E) ) * (B/sigma0) ) ** (1/n) ) + 1 ) * sigma0
    if current == h : 
        c_sigma = sigma0
    x.append(c_sigma)
    y.append(c_epsilon)
    print('{:.4e}'.format(c_sigma),'{:.4e}'.format(c_epsilon),sep="\t")
    current = current - step_size

def read_data(filename) :
    # Import data using Pandas. Using report I XY data, this line should work
    data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '\\' + filename,
                    skiprows=5, header=None, delim_whitespace=True)
    data_nofric = data.values

    x_f = []
    y_f = []

    for line in data_nofric:
        current3 = line[1]
        current2 = line[2]
        calc2 = h - current2
        c_epsilon2 = (2/np.sqrt(3))*np.log(h/calc2)
        c_sigma2 = (current3 / w * b) * (np.sqrt(3)/2) * (1e4 / 2)
        x_f.append(c_sigma2)
        y_f.append(c_epsilon2)

    return x_f, y_f

x_f , y_f = read_data("data.2.nofric")
x_wf, y_wf = read_data("data.2.withfric")

x_1f, y_1f = read_data("data.1.nofric.nosliding.nodetonode")
x_2f, y_2f = read_data("data.1.nofric.smallsliding")
x_3f, y_3f = read_data("data.1.nofric.smallsliding.nodetonode")

# Plot
plt.grid()
plt.plot(y, x, linewidth=2, color='firebrick', label="Analytical Solution")
plt.plot(y_f, x_f, linewidth=2, color='blue', label="Finite Sliding - Surface to Surface - No Friction")
plt.plot(y_wf, x_wf, linewidth=2, color='red', label="Finite Sliding - Surface to Surface - With Friction")
plt.plot(y_1f, x_1f, linewidth=2, color='green', label="Finite Sliding  - Node to Node - No Friction")
plt.plot(y_2f, x_2f, linewidth=2, color='black', label="Small Sliding - Surface to Surface -No Friction")
plt.plot(y_3f, x_3f, linewidth=2, color='purple', label="Small Sliding - Node to Node - No Friction")
plt.xlabel('Strain')
plt.ylabel('Stress (Pa)')
plt.ylim(bottom=0)
plt.legend()
plt.show()


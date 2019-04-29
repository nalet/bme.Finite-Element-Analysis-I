import os
import numpy as np
import pandas as pd
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import sys

plt.rcParams['figure.dpi'] = 120
plt.rcParams['font.size'] = 15


h = 0.2
h_max = 0.1
step_size = 0.005

sigma0 = 220e6
B = 3e9
E = 70e9
n = 3.2

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
    print('{:.4e}'.format(current),'{:.4e}'.format(c_epsilon),'{:.4e}'.format(c_sigma),sep="\t")
    current = current - step_size


# Plot
plt.grid()
plt.plot(y, x, linewidth=2, color='firebrick', label="Analytical Solution")
plt.xlabel('Strain')
plt.ylabel('Stress (Pa)')
plt.ylim(bottom=0)
plt.legend()
plt.show()

import os
import numpy as np
import pandas as pd
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import sys

plt.rcParams['figure.dpi'] = 120
plt.rcParams['font.size'] = 15
# Import data using Pandas. Using report I XY data, this line should work
<<<<<<< HEAD
data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + sys.argv[0],
                   skiprows=5, header=None, delim_whitespace=True)
data = data.values
# Fast Fourier Transform
y = fft(data[:, sys.argv[1]])
=======
data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '/abaqus.5.rpt',
                   skiprows=5, header=None, delim_whitespace=True)
data = data.values
# Fast Fourier Transform
y = fft(data[:, 3])
>>>>>>> 575fb7b1101321312edfd0bb6440cb728a29c5b1
# Absolute value
m = np.abs(y)
# Frequency
freq = np.linspace(0, 50, y.shape[0], endpoint=True)
# Plot
plt.grid()
plt.plot(freq[:25], m[:25], linewidth=2, color='firebrick')
plt.xlabel('Frequency (Hz)')
plt.ylabel('|FFT(y)|')
plt.show()

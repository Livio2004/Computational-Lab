import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin 
from scipy.fft import fft, ifft, fftfreq

L = 2*np.pi
N = 128
alpha = 0.5
dx = L/N
#funzione u tempo 0
def u(x):
    return np.sin(x)+0.5*np.sin(3*x)

x = np.linspace(0,L,N)
fi = u(x)
p = fftfreq(N, d=dx) * (2 * np.pi)
utilde0 = fft(fi)

tempi = np.linspace(0,2,20)

cmap = plt.cm.plasma
colors = cmap(np.linspace(0, 1, len(tempi)))

# calculate u0tilde

plt.figure()
for i, t in enumerate(tempi):
    utilde = utilde0* np.exp(-alpha*((p)**2)*t)
    iifft = ifft(utilde)
    plt.plot(x, iifft, color=colors[i])

sm = plt.cm.ScalarMappable(cmap=cmap)
sm.set_array(tempi)
plt.colorbar(sm, ax=plt.gca())
plt.show()

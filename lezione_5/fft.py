import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin 

L = 2*np.pi
N = 128
alpha = 0.5

#funzione u tempo 0
def u(x):
    return np.sin(x)+0.5*np.sin(3*x)

fft= lin.discrete_fourier(L,N)
fi = u(fft.x)
utilde0 = fft.fourier(fi)

tempi = np.linspace(0,2,20)

cmap = plt.cm.plasma
colors = cmap(np.linspace(0, 1, len(tempi)))

# calculate u0tilde

plt.figure()
for i, t in enumerate(tempi):
    utilde = utilde0* np.exp(-alpha*((fft.p)**2)*t)
    ifft = fft.antifourier(utilde)
    plt.plot(fft.x, ifft.real, color=colors[i])

sm = plt.cm.ScalarMappable(cmap=cmap)
sm.set_array(tempi)
plt.colorbar(sm, ax=plt.gca())
plt.show()


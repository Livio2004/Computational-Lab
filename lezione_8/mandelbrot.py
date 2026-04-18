import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin
from sympy import *
import seaborn as sns
sns.set_theme(style='darkgrid')

def mandelbrot(n,c):
    z = 0 + c*0
    N = c*0
    for i in range(n):
        mask = np.abs(z) <= 2
        z[mask] = z[mask]**2 + c[mask]
        mask = np.abs(z) <= 2
        N[mask] = i        
    return np.abs(z) <= 2, N.real

x= np.linspace(-2,2,1000)
y = np.linspace(-2,2,1000)
X, Y = np.meshgrid(x,y)
Z = X+1j*Y
iter = 200
mask, N = mandelbrot(iter,Z)
plt.figure(figsize=(12,6))
plt.imshow(N, cmap='magma', extent=[X.min(), X.max(), Y.min(), Y.max()])
plt.colorbar(label='Velocità di fuga (iterazioni)')
plt.title(f"Insieme di Mandelbrot ({iter} iterazioni)")
plt.xlabel("Reale")
plt.ylabel("Immaginario")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_mandelbrot(x0, y0, w, N, M, ax):
    x = np.linspace(x0 - w, x0 + w, N)
    y = np.linspace(y0 - w, y0 + w, N)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    
    im = ax.imshow(mandelbrot(M,X + 1j*Y)[1], cmap='viridis', animated=True)
    im.set_extent([X.min(), X.max(), Y.min(), Y.max()])
    return [im]
    
N = 1024
x0, y0 = -0.75, 0.0
x0, y0 = -0.7436438870371587, 0.13182590420531197  
w = 1.0

M = 150

fig, ax = plt.subplots()

def update(w):
    ax.set_title(f"Zoom = {1/w:.1f}")
    return plot_mandelbrot(x0, y0, w, N, M, ax)

ani = FuncAnimation(fig, update, frames=np.logspace(0, -4, 40), interval=500, blit=True)
plt.show()
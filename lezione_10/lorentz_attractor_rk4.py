import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
from sympy import *
import linalg as lin
from matplotlib import animation
from matplotlib.animation import FFMpegWriter


xyz  = np.array([0, 1, 10])
rho, sigma, beta = 28, 10, 8/3 

t0 = 0     
tf = 100   
dt = 0.001
t = [t0, tf]


def Lorentz( x, y, z, t): 
    return np.array([sigma*(y - x),   # ... dx/dt
                     rho*x - y - x*z, # ... dy/dt
                     x*y - beta*z])   # ... dz/dt


equaz = lin.equazioni_differenziali(t, Lorentz, xyz, dt)
tempi, soluz = equaz.rk4()
n = len(tempi)

evol = soluz.T

fig = plt.figure('Attrattore di Lorenz', facecolor='k', figsize=(10, 9))
ax = fig.add_subplot(111, projection='3d')
fig.tight_layout()

def update(i): 
    ax.view_init(-6, -56 + i/10) 
    ax.clear()
    ax.set_facecolor('k')
    ax.set_axis_off()

    ax.plot(evol[:i, 0], evol[:i, 1], evol[:i, 2], color='lime', lw=0.9)

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 15000, 5), 
                              interval=1, repeat=False)

#FARE GIF SPIEGATO DA GEMINI


# 1. Definiamo i parametri del "Writer"
# fps: fluidità del video
# bitrate: qualità del video (più alto = più nitido, ma file più pesante)
writer = FFMpegWriter(fps=60, metadata=dict(artist='Me'), bitrate=2000)

nome_video = "lorenz_attractor.mp4"

print("Codifica del video in corso...")
# 2. Salvataggio
ani.save(nome_video, writer=writer)

print(f"Video salvato con successo come {nome_video}")

plt.show()


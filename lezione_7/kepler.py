import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit
import linalg as lin
from matplotlib.animation import FuncAnimation

def x(E):
    a = 1
    e = 0.5
    return a*(np.cos(E)-e)

def y(E):
    a = 1
    e = 0.5
    return a*np.sqrt(1-e**2)*np.sin(E)


e = 0.5 #eccentricità
a = 1 #semiasse maggiore 
#0.5T = 2pi -esin(2pi)
T = 2*(2*np.pi-e*np.sin(2*np.pi))
M = lambda t: 0.5*t 
t = np.linspace(0,T, 100)
Mt = M(t)
a = -np.pi/4
b = 3*np.pi
rootf= []
for i in t:
    rooteq = lambda E: E-e*np.sin(E)-M(i)
    soluzione = lin.root_functions(a, b, rooteq)
    rootf1, root1 =  soluzione.regula_falsi()
    rootf.append(rootf1)

rootf = np.array(rootf)

xi = x(rootf)
yi = y(rootf)
plt.figure(figsize=(12,6))
colors = np.sin(t/2.0)
plt.scatter(xi, yi, c = colors, cmap= 'viridis')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 1) 
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal') # Non voglio l'ellisse deformata 
ax.grid(True, linestyle='--', alpha=0.6)


ax.plot(xi, yi, 'w--', alpha=0.3,color= 'green',  label='Orbita')
# Il Sole a 0 0 nel mio sdr
ax.plot(0, 0, 'yo', markersize=10, label='Sole')
punto, = ax.plot([], [], 'ro', markersize=8, label='Pianeta')
testo_tempo = ax.text(-1.8, 1.3, '', fontsize=12)



#USARE QUESTO MODELLO PER ANIMAZIONI FUTURE 
def init():
    punto.set_data([], [])
    testo_tempo.set_text('')
    return punto, testo_tempo

# Funzione di update per ogni frame i perchè ho 100 punti in questo caso
def update(i):
    punto.set_data([xi[i]], [yi[i]]) # Passiamo liste o array
    testo_tempo.set_text(f'Tempo: {t[i]:.2f}')
    return punto, testo_tempo

# Uso FuncAnimation per l'animazione
#uso 50 millisecondi per ogni frame (ne ho 100 in tutto)
ani = FuncAnimation(fig, update, frames=len(t), 
                    init_func=init, interval=50)

plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin 

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
f = np.array([0, 1.5, 2, 2.5, 2, 4, 2, 2.5, 2, 1.5, 0])

masks = [
    np.array([True,False,True,True,False,True,False,True,True,False,True]),
    np.array([True,False,True,True,True,True,True,True,True,False,True]),
    np.array([True]*len(x))
]

pol1 = lin.interpolazioni(x[masks[0]],f[masks[0]])
pol2 = lin.interpolazioni(x[masks[1]],f[masks[1]])
pol3 = lin.interpolazioni(x[masks[2]],f[masks[2]])

x_sample = np.linspace(0,10,100)

polv1 = pol1.lagrange_interpolation(x_sample)
polv2 = pol2.lagrange_interpolation(x_sample)
polv3 = pol3.lagrange_interpolation(x_sample)
polv=np.vstack((polv1, polv2, polv3))

fig, axes = plt.subplots(1, 3, figsize=(12, 5))
for i, l in zip(range(3),['A','B','C']):
    axes[i].scatter(x[masks[i]], f[masks[i]],color ='r', label=f'Dataset {l}')
    axes[i].plot(x_sample, polv[i], label=f'interpolazione con Lagrange')
    axes[i].set_xlabel("$x$")
    axes[i].set_ylabel("$f(x)$")
    axes[i].legend()


plt.tight_layout()
plt.show()

#con la matrice di Vandermonde
V = np.vander(x, increasing=True)
a = np.linalg.solve(V, f)
mio_polinomio = np.polynomial.Polynomial(a)
x_plot = np.linspace(0, 10, 1000)
y_plot = mio_polinomio(x_plot)


plt.figure(figsize=(10,6))
plt.plot(x_plot, y_plot, label='Metodo completo con sistema lineare')
plt.scatter(x,f,label='dataset')
plt.legend()
plt.show()    
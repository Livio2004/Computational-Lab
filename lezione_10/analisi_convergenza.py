import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
from sympy import *
import linalg as lin


func = lambda x, y : x*y
risultato_analitico = lambda x: 2*np.exp((x**2)/2)
h = 0.1
x = np.array([0,1])
y0=2
t_sol, y_sol = lin.forward_euler(x, func, y0, h)
xi = np.arange(x[0], x[1]+2*h, h)
#print(y_sol)
#print(risultato_analitico(xi))
residui = np.array(np.abs(y_sol-risultato_analitico(xi)))
print(residui)
plt.plot(xi, residui)
plt.yscale('log')
plt.show()

h_test = [0.1, 0.05, 0.01, 0.005, 0.001]
errori_finali = []

for h_i in h_test:
    t_i, y_i = lin.forward_euler(x, func, y0, h_i)
    err = np.abs(y_i[-1] - risultato_analitico(t_i[-1]))
    errori_finali.append(err)

plt.figure()
plt.loglog(h_test, errori_finali, 'o-', label='residui')
plt.loglog(h_test, h_test, '--', label='Trend  O(h) grande') 
plt.xlabel('Passo h')
plt.ylabel('Errore finale a t=1')
plt.legend()
plt.show()

h_test = [0.1, 0.05, 0.01, 0.005, 0.001]
errori_finali = []

for h_i in h_test:
    t_i, y_i = lin.backward_euler(x, func, y0, h_i)
    err = np.abs(y_i[-1] - risultato_analitico(t_i[-1]))
    errori_finali.append(err)

plt.figure()
plt.loglog(h_test, errori_finali, 'o-', label='residui')
plt.loglog(h_test, h_test, '--', label='Trend  O(h) grande') 
plt.xlabel('Passo h')
plt.ylabel('Errore finale a t=1')
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

h = 0.1
x = np.linspace(0, 2, 100)
y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(x, y)

L = X 

# per x > 0 la soluzione esplode comunque, ma studiamo h*L 
stabilità = h * L

plt.figure(figsize=(8, 6))
cp = plt.contourf(X, Y, stabilità, levels=[0, 0.1, 0.5, 1.0, 2.0], cmap='RdYlGn_r')
plt.colorbar(cp, label='h * L (Lipschitz factor)')
plt.title("Mappa di stabilità locale (h*L)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()





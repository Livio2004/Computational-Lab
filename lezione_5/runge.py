import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin 


runge = lambda x: 1/(1+25*x**2)
x1 = np.linspace(-1,1,8)
x2 = np.linspace(-1,1,12)
y1 = runge(x1)
y2 = runge(x2)
plt.figure(figsize=(10,6))
pol1 = lin.interpolazioni(x1,y1)
pol2 = lin.interpolazioni(x2,y2)
x_sample=np.linspace(-1,1,200)
polv1 = pol1.lagrange_interpolation(x_sample)
polv2 = pol2.lagrange_interpolation(x_sample)
plt.scatter(x1,y1, color ='yellow')
plt.scatter(x2,y2,color='black')
plt.plot(x_sample, runge(x_sample))
plt.fill_between(x_sample,polv1, label = 'N = 8', color = 'green', alpha=0.4)
plt.fill_between(x_sample,polv2, label = 'N = 12', color = 'red', alpha =0.4)
plt.title('errore interpolazione')
plt.legend()
plt.tight_layout()
plt.show()

x_sample2 = np.linspace(-0.1,0.1,2000)
errori_integrale = []
n_values = np.arange(10,81,10)
for i in n_values:
    x= np.linspace(-1,1,i)
    y = runge(x)
    pol = lin.interpolazioni(x,y)
    polv = pol.lagrange_interpolation(x_sample2)
    residuo = np.power(np.abs(runge(x_sample2)-polv),2)
    integrale = np.trapezoid(residuo, x_sample2)
    errori_integrale.append(integrale)

errori_integrale= np.array(errori_integrale)
plt.figure(figsize=(8, 6), facecolor='#eaeaea')
plt.semilogy(n_values, errori_integrale, 'o', color='#2a5b84', markersize=6)
plt.xlabel('Numero di punti (n)', fontsize=12)
plt.ylabel('Errore', fontsize=12)
    
formula = r'$\int_{-0.1}^{0.1} dx|f(x) - P_n(x)|$'
plt.text(n_values[1], errori_integrale[-2], formula, fontsize=16)
    
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

x_sample2 = np.linspace(0.8,1,2000)
errori_integrale = []
n_values = np.arange(10,81,10)
for i in n_values:
    x= np.linspace(-1,1,i)
    y = runge(x)
    pol = lin.interpolazioni(x,y)
    polv = pol.lagrange_interpolation(x_sample2)
    residuo = np.power(np.abs(runge(x_sample2)-polv),2)
    integrale = np.trapezoid(residuo, x_sample2)
    errori_integrale.append(integrale)

errori_integrale= np.array(errori_integrale)
plt.figure(figsize=(8, 6), facecolor='#eaeaea')
plt.semilogy(n_values, errori_integrale, 'o', color='#2a5b84', markersize=6)
plt.xlabel('Numero di punti (n)', fontsize=12)
plt.ylabel('Errore', fontsize=12)
    
formula = r'$\int_{0.8}^{1} dx|f(x) - P_n(x)|$'
plt.text(n_values[1], errori_integrale[-2], formula, fontsize=16)
    
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
    
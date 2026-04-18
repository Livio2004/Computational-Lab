import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin
from sympy import *


func = lambda z : (z**2-1)*(z**2+1)
x0 = complex(0.5,0.5)
sol, history = lin.newton(x0, func)
f_complex= lambda z: (z**2+1)*(z**2-1)
f_complex_prime=lambda z:4*z**3
def newton_roots2(f,f_prime,x0,tol,N):  #where history collects the values of x during the iteration
    x=x0-f(x0)/f_prime(x0)
    
    for i in range(N):
        x=x-f(x)/f_prime(x)
        #History.append(x)(for every cicle i would append a Matrrix of 10**6 size)
        #print(np.max(abs(f(x))), f(x[0,0]))
        if np.max( np.abs(f(x)))<tol:
            print('the alghortim converges after',i,'iteration')
            return x
    return x


print(sol)
N = 1024
x = np.linspace(-1,1,N).astype(np.float64)
X, Y = np.meshgrid(x, x)
Z = X + 1j*Y
solci = newton_roots2(f_complex, f_complex_prime, Z, tol = 10e-10, N =2000)
print(np.mean(np.abs(solci)))
fig = plt.figure()
plt.imshow(np.angle(solci), cmap="viridis")
plt.show()
solci , _= lin.newton(Z, func, max_iter =1000)
fig = plt.figure()
plt.imshow(np.angle(solci), cmap="viridis")
plt.show()
plt.imshow(np.abs(solci), cmap= 'plasma')
print(np.mean(np.abs(solci)))
plt.show()

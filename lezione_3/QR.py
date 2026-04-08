import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin

#algoritmo houseolder matrice 2x2
def householder(A):
    u = A[:,0].copy()
    n = np.sqrt(u@u)
    if (u[0] + n) > (u[0]-n):
        s = +1
    else:
        s = -1
    den = n**2 + s * u[0] * n
    u[0] += s * n
    return np.eye(len(A)) - np.outer(u,u) / den

def QR_decomposition(A):
    n = A.shape[0]
    R = A.copy()
    Q = np.eye(n)
    for i in range(n-1):
      P = np.eye(n)
      Pp = householder(R[i:, i:])
      P[i:,i:] = Pp
      print('la matrice P', P)
      R = P@R
      Q = Q@P

    return Q, R


        



A = np.array([[4,12,-16],
              [12,37,-43],
              [-16,-43,98]], dtype = np.float64)

b = np.array([1,5,3], dtype = np.float64)

print(f"La matrice originale vale: \n {A}")

Q, R = QR_decomposition(A)

print(f'La matrice ortogonale vale: \n {Q}')
print(f'La matrice triangolare superiore vale: \n {R}')

print(f'La verifica vale \n {Q@R} ')

sistema = lin.linear_system(A,b)
x1= sistema.solve_QR()
print(f'la soluzione del sistema con QR vale : \n {x1}')
x2 = sistema.solve_cholensky()
print(f'La soluzione con cholensky vale {x2}')
sistema.verifica_sistema_cholesky()

sistema.verifica_sistema_QR()




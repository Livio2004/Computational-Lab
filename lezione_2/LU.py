import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin


#controllo matrici simmetrica 

def check_symmetry(A):
    n = A.shape[0]
    for i in range(n):
        for j in range(i+1,n):
                if A[i,j]!=A[j,i]:
                     print("La matrice non è simmetrica")
                     return False
                
    print("la matrice è simmetrica")

    return True

def cholesky_reduction(A):
    n = A.shape[0]
    L=np.eye(3, dtype = np.float64)
    for i in range(n):
          for j in range(0, i+1):
            s = np.sum(np.power(L[i,:j],2))
            if i==j :
                 L[i,j]=np.sqrt(A[i,i]-s)
            if i >j :
                 s_ij = np.sum(L[i, :j]*L[j, :j] )
                 L[i,j]=(1/L[j,j])*(A[i,j]-s_ij)
    return L

def cholesky_sistema(A, b):
     n = A.shape[0]
     #risolvo prima Ly = b e poi Ldagax = y
     L = cholesky_reduction(A)
     Ldaga = np.transpose(L)
     y = lin.backward_substition(L,b)
     x = lin.forward_substition(Ldaga,x)
     return x


     

A = np.array([[4,12,-16],
              [12,37,-43],
              [-16,-43,98]])

b = np.array([1,5,3])


sistema = lin.linear_system(A, b)

x = sistema.solve()
print(f"La soluzione del sistema \n  {A}*x= {b}è : \n {x}")
sistema.verifica_sistema()








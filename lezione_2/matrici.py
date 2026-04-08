import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 


def backward_substition(A,b):
    #Checkiamo se la matrice A è triangolare superiore
    if not np.allclose(A, np.triu(A)):
        raise ValueError("La matrice A deve essere triangolare superiore")
    n = A.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:]))/A[i,i]
    return x
    
def forward_substition(A,b):
    n = A.shape[0]
    x = np.zeros(n)
    for i in range(n):
        x[i] = (b[i] - np.dot(A[i, :i], x[:i]))/A[i,i]
    return x

def gaussian_elimination(A, b):
    n = A.shape[0]
    #bisogna fare il ciclo sulle colonne e poi sulle righe
    for j in range(n):
        for i in range(j+1,n):
            c = A[i,j]/A[j, j]
            A[i,j:]=A[i, j:]-c*A[j,j:]
            b[i]=b[i]-c*b[j]
    return A, b

def gaussian_elimination_pivoting(A, b):
    n = A.shape[0]
    #bisogna fare il ciclo sulle colonne e poi sulle righe
    for j in range(n):
        pivot_riga = np.argmax(A[j:,j])+j
        print(pivot_riga)

        if (np.abs(A[pivot_riga, j])<10e-12):
            print('ciao')
            raise ValueError('La matrice è singolare ')
        
        if (pivot_riga != j):
            A[[j,pivot_riga]]= A[[pivot_riga, j]]
            b[[j,pivot_riga]]=b[[pivot_riga,j]]

        for i in range(j+1,n):
            c = A[i,j]/A[j, j]
            A[i,j:]=A[i, j:]-c*A[j,j:]
            print(A)
            b[i]=b[i]-c*b[j]
    return A, b





    
    
U = np.array([[2,1,1], 
              [0,1,-2], 
              [0,0,1]], dtype = np.float64)

b = np.array([1,-1,4])
n = U.shape[0]
print(n)

x = backward_substition(U,b)
print('la soluzione del sistema lineare è:', x)
verifica = np.dot(U,x)
controllo = b - verifica
print(f'verifica della soluzione: {verifica}. Dovrebbe essere uguale a b: {b}')
for i in range(0,n):
    if controllo[i] == 0 :
        print('complimenti hai fatto tutto in modo corretto')
    else :
        print("controlla bene...")

U2 = np.array([[2,1,1],
               [1,1,-2],
               [1,2,1]], dtype=np.float64)
b2 = np.array([8,-2,2])

U2, b2 = gaussian_elimination(U2, b2)
print("Il sistema triangolarizzato è:",U2, "x=", b2)
x2 = backward_substition(U2,b2)
print('la soluzione del sistema lineare è:', x2)

U_pivot = np.array([[2,1,1],
               [2,1,-4],
               [1,2,1]], dtype=np.float64)

U_pivot, b2 = gaussian_elimination_pivoting(U_pivot, b2)
print(f"In questo caso si usa il pivoting e viene:{U_pivot} con b = {b2}")







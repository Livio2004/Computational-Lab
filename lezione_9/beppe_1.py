import numpy as np 
import sympy as sp
import matplotlib.pyplot as plt
def hermite(n):
    h_0=1
    h__1=0 #h(n=-1)
    H=[h__1,h_0]
    coeffs=np.zeros(n+1)
    
    for i in range(1,n+1,1):
        if n==-1: return h__1
        if n==0: return h_0
        
        x=sp.symbols('x', real=True)
        h_i=2*x*H[i]-2*(i-1)*H[i-1]
        H.append(h_i)

    
    
        
    return sp.simplify(H[n+1]),np.flip( sp.Poly(H[n+1]).all_coeffs() )#we return the polynomial in a symbolic writing and the coeeficcents

def companion(coeffs):
    C=np.eye(len(coeffs)-1,k=1)
    C[-1,0:]=-coeffs[:-1]
    return C


def iterative_householder(A,i):
    u = A[i:,i].copy()
    n = np.sqrt(np.vdot(u,u))
    if np.abs((u[0] + n)) >np.abs( (u[0]-n)):
        s = +1
    else:
        s = -1
    den = n**2 + s * u[0] * n
    u[0] += s * n
    return np.eye(len(A)-i,dtype=complex) - np.outer(u,u.conj()) / den


#------------------------------------------------------------------------#
def QR_decomposition(A):
    R=A.copy().astype(complex)
    Q=np.eye(len(A),dtype=complex)
    for i in range(len(A)-1):
        P_i=iterative_householder(R,i)
        R_i=P_i @ R[i:,i:]
        R[i:,i:]=R_i
        I=np.eye(len(A),dtype=complex)
        I[i:,i:]=P_i
        Q=Q@I.T.conj()
    return(Q,R)
#------------------------------------------------------------------------#

pol,coeffs_6=hermite(5)
x=sp.symbols('x', real=True)
func=sp.lambdify(x, pol, modules='numpy')
I=np.linspace(-2.5,2.5,1000)
plt.plot(I,func(I))
plt.axhline(y=0, color='black')
plt.grid(True)

C=companion(coeffs_6)
Q,R=QR_decomposition(C)
print(Q@R)
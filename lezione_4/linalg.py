import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 


class linear_system:
    def __init__(self, A, b=None):
        self.A = np.array(A, dtype=np.complex128)
        if b is None:
            self.b = np.array(self.A.shape[0])
        self.b = np.array(b, dtype=np.float64)
        self.n = self.A.shape[0]
        self.L = None
        self.P = 0
        self.Q = None
        self.R = None

    def check_symmetry(self):
        for i in range(self.n):
            for j in range(i+1,self.n):
                    if self.A[i,j]!=self.A[j,i]:
                        print("La matrice non è simmetrica")
                        return False
                
        print("la matrice è simmetrica")
        return True
    
    def cholesky_reduction(self):
        if not self.check_symmetry():
            raise ValueError("La matrice non è simmetrica!")
        
        L = np.zeros((self.n, self.n))
        for i in range(self.n):
          for j in range(0, i+1):
            s = np.sum(np.power(L[i,:j],2))
            if i==j :
                 L[i,j]=np.sqrt(self.A[i,i]-s)
            if i >j :
                 s_ij = np.sum(L[i, :j]*L[j, :j] )
                 L[i,j]=(1/L[j,j])*(self.A[i,j]-s_ij)
        self.L = L
        return self.L
    
    def backward_substition(self, A, b):
    #Checkiamo se la matrice A è triangolare superiore
        if not np.allclose(A, np.triu(A)):
            raise ValueError("La matrice A deve essere triangolare superiore")
        x = np.zeros(self.n)
        for i in range(self.n-1, -1, -1):
            x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:]))/A[i,i]
        return x
    
    def forward_substition(self, A,b):
        x = np.zeros(self.n)
        for i in range(self.n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]))/A[i,i]
        return x

    def gaussian_elimination(self, A, b):
    #bisogna fare il ciclo sulle colonne e poi sulle righe
        for j in range(self.n):
            for i in range(j+1,self.n):
                c = A[i,j]/A[j, j]
                A[i,j:]=A[i, j:]-c*A[j,j:]
                b[i]=b[i]-c*b[j]
        return A, b

    def gaussian_elimination_pivoting(self, A, b):
        #bisogna fare il ciclo sulle colonne e poi sulle righe
        for j in range(self.n):
            pivot_riga = np.argmax(A[j:,j])+j
            print(pivot_riga)

        if (np.abs(A[pivot_riga, j])<10e-12):
            print('ciao')
            raise ValueError('La matrice è singolare ')
        
        if (pivot_riga != j):
            A[[j,pivot_riga]]= A[[pivot_riga, j]]
            b[[j,pivot_riga]]=b[[pivot_riga,j]]

        for i in range(j+1,self.n):
            c = A[i,j]/A[j, j]
            A[i,j:]=A[i, j:]-c*A[j,j:]
            print(A)
            b[i]=b[i]-c*b[j]
        return A, b
    
    def solve_cholensky(self):
        #risoluzione generale del sistema lineare con cholesky
        if self.L is None:
            self.cholesky_reduction()
        
        # 1. Ly = b
        y = self.forward_substition(self.L, self.b)
        # 2. L^T x = y
        x = self.backward_substition(self.L.T, y)
        return x
    
    '''def householder(self, R):
        u = R[:,0].copy()
        n = np.sqrt(u@u)
        if (u[0] + n) > (u[0]-n):
            s = +1
        else:
            s = -1
        den = n**2 + s * u[0] * n
        u[0] += s * n
        return np.eye(len(R)) - np.outer(u,u) / den'''
    
    def householder(self, R):
        u = R[:, 0].copy().astype(complex)
        n = np.linalg.norm(u)
        
        if n == 0:
            return np.eye(len(R), dtype=complex)

        if np.abs(u[0]) > 1e-15:
            s = u[0] / np.abs(u[0])
        else:
            s = 1.0 
        u[0] += s * n
        
        norma_u_quadra = np.real(u.conj().T @ u)
        
        if norma_u_quadra < 1e-15:
            return np.eye(len(R), dtype=complex)
        return np.eye(len(R), dtype=complex) - 2.0 * np.outer(u, u.conj()) / norma_u_quadra

    def QR_decomposition(self, A):
        n = self.A.shape[0]
        R = A.copy()
        Q = np.eye(n)
        self.P = 0
        for i in range(n-1):
            P = np.eye(n, dtype = np.complex128)
            Pp = self.householder(R[i:, i:])
            P[i:,i:] = Pp
            R = P@R
            Q = Q@P
            self.P+=1
        self.Q = Q
        self.R = R
        return Q, R
    
    def solve_QR(self):
        Q, R = self.QR_decomposition()
        b = Q.T @ self.b
        x = self.backward_substition(R, b)
        return x

    
    def verifica_sistema_cholesky(self):
        verifica = np.dot(self.A, self.solve_cholensky())
        residuo= np.linalg.norm(verifica-self.b)
        print(f"Il residuo per il sistema con Cholensky vale {residuo}")
        return None
    
    def verifica_sistema_QR(self):
        verifica = np.dot(self.A, self.solve_QR())
        residuo= np.linalg.norm(verifica-self.b)
        print(f"Il residuo per il sistema con QR vale {residuo}")
        return None
    
    def cholesky_determinant(self):
        if self.L is None:
            self.cholesky_reduction()
        diag_elements = np.diag(self.L)
        # Calcoliamo il prodotto dei quadrati
        determinante = np.prod(diag_elements**2)
    
        return determinante
    def QR_determinant(self):
        #uso binet per q e R
        detQ = np.power(-1, self.P)
        detR = np.prod(np.diag(self.R))
        return detQ*detR
    
    def eigensolver_QR(self, tol, N):
        Ak = self.A.copy().astype(complex)
        Qk = np.eye(self.n, dtype= complex)
        for i in range(N):
            Q,R = self.QR_decomposition(Ak)
            Ak = np.dot(R, Q)
            Qk = np.dot(Qk, Q)
            diag = np.abs(np.diag(Ak))
            subdiag = np.abs(np.diag(Ak, k=-1))
            somma_adiacenti = diag[:-1] + diag[1:]
            if np.all(subdiag <= tol * somma_adiacenti):
                print(f"Convergenza relativa raggiunta all'iterazione {i}")
                break
        autovalori = np.diag(Ak)
        autovettori = []
        for j in range(Qk.shape[1]):
            autovettore_j = Qk[:, j]
            autovettori.append(autovettore_j)
        autovettori = np.array(autovettori)
        return autovalori, autovettori
    
    def residui_QR(self, tol, N):
        plt.figure(figsize=(10, 6))
        target_vals, _ = self.eigensolver_QR(tol, N) 
        target_vals = np.sort(np.real(target_vals)) 
        storia_residui = [[] for _ in range(self.n)]
        for i in range(1, N + 1):
            current_vals, _ = self.eigensolver_QR(tol, i)
            current_vals = np.sort(np.real(current_vals)) # Ordiniamo anche questi
            
            for a in range(self.n):
                # Residuo: distanza tra la stima i-esima e l'autovalor finale
                res = np.abs(current_vals[a] - target_vals[a])
                storia_residui[a].append(res)
                
        for a in range(self.n):
            plt.semilogy(range(1, N + 1), storia_residui[a], label=f'λ_{a} ≈ {target_vals[a]:.2f}')
        
        plt.xlabel('Iterazioni')
        plt.ylabel('Residuo |λ_i - λ_target|')
        plt.title('Convergenza degli Autovalori (QR)')
        plt.legend()
        plt.show()



            
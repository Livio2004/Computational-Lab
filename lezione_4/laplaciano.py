import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin
N = 10
K = 2*np.eye(N)-np.eye(N, k=1)-np.eye(N, k=-1)

sistema = lin.linear_system(K)
autovalori, autovettori = sistema.eigensolver_QR(10**(-100), 100)
sistema.residui_QR(10**(-16),100)

def eigensolver_QR(K,N =100):
        Ak = K.copy().astype(complex)
        Qk = np.eye(K.shape[0], dtype= complex)
        for i in range(N):
            Q,R = np.linalg.qr(Ak)
            Ak = np.dot(R, Q)
            Qk = np.dot(Qk, Q)
        autovalori = np.diag(Ak)
        autovettori = []
        for j in range(Qk.shape[1]):
        # Prendiamo la colonna j-esima (l'autovettore corrispondente)
            autovettore_j = Qk[:, j]
            autovettori.append(autovettore_j)
        autovettori = np.array(autovettori)
        return autovalori, autovettori

def residui_QR(K, N=100):
        plt.figure(figsize=(10, 6))
        target_vals, _ = eigensolver_QR(K) 
        target_vals = np.sort(np.real(target_vals)) # Ordiniamoli per facilitare il confronto
        
        storia_residui = [[] for _ in range(K.shape[0])]
        for i in range(1, N + 1):
            # Calcoliamo la stima attuale all'iterazione i
            current_vals, _ = eigensolver_QR(K,i)
            current_vals = np.sort(np.real(current_vals)) # Ordiniamo anche questi
            
            for a in range(K.shape[0]):
                # Residuo: distanza tra la stima i-esima e il target finale
                res = np.abs(current_vals[a] - target_vals[a])
                storia_residui[a].append(res)
                
        for a in range(K.shape[0]):
            plt.semilogy(range(1, N + 1), storia_residui[a], label=f'λ_{a} ≈ {target_vals[a].real:.2f}')
        
        plt.xlabel('Iterazioni')
        plt.ylabel('Residuo |λ_i - λ_target|')
        plt.title('Convergenza degli Autovalori (QR)')
        plt.grid(True, which="both", ls="-")
        plt.legend()
        plt.show()



residui_QR(K,100)
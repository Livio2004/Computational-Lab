import numpy as np 
import matplotlib.pyplot as plt
from numba import jit
import sys
import time 



def somma_ottimizzata(n_totale, blocco = int(10e9/2)):
    totale = 0.0
    for i in range(1, n_totale+1, blocco):
        fine_blocco = min(i+blocco-1, n_totale)
        n= np.arange(i, fine_blocco+1, dtype=np.float64)
        totale += np.sum(1/np.power(n,2))
    return totale

def serie_armonica_2(n):
    return np.array(np.sum(1/np.power(np.arange(1, n+1),2), dtype=np.float32))

def serie_armonica_reverse_order(n):
    return np.array(np.sum(1/np.power(np.arange(n, 0, -1),2), dtype=np.float32))

def serie_armonica_2_2(n):
    return np.array(np.sum(1/np.power(np.arange(1, n+1),2), dtype=np.float64))

def serie_armonica_reverse_order_2(n):
    return np.array(np.sum(1/np.power(np.arange(n, 0, -1),2), dtype=np.float64))


numero = int(float(sys.argv[1])) if len(sys.argv) > 1 else 1000000
n = numero 
#risultato_n = serie_armonica_2(n)
#risultato_n_reverse = serie_armonica_reverse_order(n)
risultato_esatto = np.pi**2/6
#risultato_n_2 = serie_armonica_2_2(n)
#risultato_n_reverse_2 = serie_armonica_reverse_order_2(n)
'''
print(f'Il risultato della serie con {n} è:{risultato_n}')
print(f'Il risultato della serie con {n} in ordine inverso è:{risultato_n_reverse}')
print(f"Il risultato esatto è: {risultato_esatto}")

print(f"Il risultato della serie con {n} in float64 è:{risultato_n_2}")
print(f'Il risultato della serie con {n} in ordine inverso in float64 è:{risultato_n_reverse_2}')'''

# plot convergenza 
n_valori = np.arange(1, n+1, int(10e9/4))
time1 = time.time()
#results = np.array([serie_armonica_2(i) for i in n_valori])
results = np.array([somma_ottimizzata(i) for i in n_valori])
#results_reverse = np.array([serie_armonica_reverse_order(i) for i in n_valori])
print(results)
time2 = time.time()
print(f'Tempo totale per calcolare i risultati: {time2 - time1:.2f} secondi')
#results_2 = np.array([serie_armonica_2_2(i) for i in n_valori])
#results_reverse_2 = np.array([serie_armonica_reverse_order_2(i) for i in n_valori])
plot_y=np.abs(results - risultato_esatto)
#plot_y_reverse=np.abs(results_reverse - risultato_esatto)
#plot_y_2=np.abs(results_2 - risultato_esatto)
#plot_y_reverse_2=np.abs(results_reverse_2 - risultato_esatto)

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10, 6))
ax[0].plot(n_valori, plot_y, label='Errore ordine normale')
#ax[0].plot(n_valori, plot_y_reverse, label='Errore ordine inverso')
ax[0].set_xscale('log')
ax[0].set_yscale('log')
ax[0].set_xlabel('n (log scale)')
ax[0].set_ylabel('Errore assoluto (log scale)')
ax[0].set_title('Convergenza della serie armonica al quadrato')
ax[0].legend()
#ax[1].plot(n_valori, plot_y_2, label='Errore ordine normale (float64)')
#ax[1].plot(n_valori, plot_y_reverse_2, label='Errore ordine inverso (float64)')
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xlabel('n (log scale)')
ax[1].set_ylabel('Errore assoluto (log scale)')
ax[1].set_title('Convergenza della serie armonica al quadrato (float64)')
ax[1].legend()
plt.tight_layout()
plt.show()





                  

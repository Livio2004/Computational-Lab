import numpy as np
import matplotlib.pyplot as plt
from numba import jit
import sys
import time


@jit(nopython=True)
def somma_serie_armonica_2(n):
    s = np.array(0.0, dtype=np.float32)
    for i in range(1, n+1):
        s += np.array(1/np.power(n,2), dtype=np.float32)
    return s 


def serie_armonica_2(n):
    return np.array(np.sum(1/np.power(np.arange(1, n+1),2), dtype=np.float32))


numero = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
n = numero
time1 = time.time()
risultato_n = serie_armonica_2(n)
time2 = time.time()
print(f'Tempo per calcolare la serie senza JIT: {time2 - time1:.2f} secondi')
time3 = time.time()
risultato_jit = somma_serie_armonica_2(n)
time4 = time.time()
print(f'Tempo per calcolare la serie con JIT: {time4 - time3:.2f} secondi')
risultato_esatto = np.pi**2/6




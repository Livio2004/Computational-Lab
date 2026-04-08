import numpy as np
import matplotlib.pyplot as plt

# 1. Creiamo il nostro "Nucleo di Uranio" virtuale
# Generiamo una matrice simmetrica molto grande (es. 2000x2000) del GOE
N = 2000
A = np.random.randn(N, N)
H = (A + A.T) / 2.0  # La rendiamo simmetrica (condizione fondamentale in quantistica)

# 2. Calcoliamo le energie del sistema (gli autovalori)
# np.linalg.eigvalsh li restituisce già ordinati dal più piccolo al più grande
energie = np.linalg.eigvalsh(H)

# 3. Selezioniamo solo il "cuore" dello spettro.
# Evitiamo i bordi del semicerchio perché lì la densità cambia rapidamente.
# Prendiamo solo le energie centrali (dal 25% al 75% dell'array).
energie_centrali = energie[int(N * 0.25) : int(N * 0.75)]

# 4. Calcoliamo lo SPACING (la distanza tra un livello di energia e il successivo)
spacings = np.diff(energie_centrali)

# 5. Normalizziamo gli spacing in modo che la distanza media sia esattamente 1
spacings_normalizzati = spacings / np.mean(spacings)

# ---------------- GRAFICA E CONFRONTO TEORICO ---------------- #
plt.figure(figsize=(10, 6))

# Istogramma della nostra simulazione
plt.hist(spacings_normalizzati, bins=50, density=True, alpha=0.7, 
         color='darkorange', edgecolor='black', label='Simulazione (Distanza tra autovalori)')

# Creiamo l'asse X per le curve teoriche
s = np.linspace(0, 4, 200)

# A. Curva di Poisson (se le particelle non interagissero)
poisson = np.exp(-s)
plt.plot(s, poisson, 'k--', lw=2, label='Poisson (Livelli indipendenti - Errato per l\'Uranio)')

# B. Congettura di Wigner (La formula che gli valse il Nobel)
# Questa descrive la "repulsione dei livelli"
wigner = (np.pi / 2.0) * s * np.exp(-np.pi * s**2 / 4.0)
plt.plot(s, wigner, 'r-', lw=3, label='Wigner Surmise (Repulsione dei livelli)')

# Dettagli del grafico
plt.title("Repulsione dei Livelli: Il Caos Quantistico nell'Uranio", fontsize=14, fontweight='bold')
plt.xlabel("Distanza tra livelli energetici adiacenti (s)", fontsize=12)
plt.ylabel("Probabilità P(s)", fontsize=12)
plt.xlim(0, 4)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
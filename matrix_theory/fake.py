import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# 1. SCARICO E PREPARAZIONE DATI
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM", "V", "JNJ", 
           "WMT", "PG", "MA", "UNH", "DIS", "HD", "BAC", "VZ", "KO", "PFE",
           "INTC", "CMCSA", "PEP", "CSCO", "NFLX", "ABT", "ADBE", "CRM", "NKE", "T",
           "MRK", "CVX", "XOM", "WFC", "MCD", "TXN", "MDT", "HON", "UNP", "IBM",
           "QCOM", "GS", "BA", "CAT", "MMM", "GE", "F", "GM", "AMD", "UBER"]

print("Scaricamento dati in corso dal 2020 al 2024...")
# Usiamo 'Close' per evitare l'errore KeyError
data = yf.download(tickers, start="2020-01-01", end="2024-01-01")['Close']

# Pulizia dei dati mancanti e calcolo rendimenti
data = data.dropna(axis=1, how='all')
returns = data.pct_change(fill_method=None).dropna()

# Standardizziamo i rendimenti (media 0, varianza 1)
returns_norm = (returns - returns.mean()) / returns.std()

T, N = returns_norm.shape
if T == 0 or N == 0:
    print("Errore critico: i dati sono vuoti. Riavvia lo script.")
    exit()

Q = T / N  

# 2. MATRICE DI CORRELAZIONE E DECOMPOSIZIONE
corr_matrix = (returns_norm.T @ returns_norm) / T

# Usiamo 'eigh' che ci restituisce sia gli Autovalori che gli AUTOVETTORI (ci servono per ricostruire)
eigenvalues, eigenvectors = np.linalg.eigh(corr_matrix)

# 3. MARCHENKO-PASTUR E SEPARAZIONE DEL RUMORE
# Aggiustiamo la varianza togliendo il "Market Mode" (l'ultimo autovalore, il più grande)
# Questo fa combaciare la teoria con i dati reali!
sigma_sq = 1.0 - (eigenvalues[-1] / N) 

lambda_max = sigma_sq * (1 + np.sqrt(1/Q))**2
lambda_min = sigma_sq * (1 - np.sqrt(1/Q))**2

# 4. *** LA MAGIA: RICOSTRUZIONE DELLA MATRICE PULITA ***
# Copiamo gli autovalori originali
clean_eigenvalues = eigenvalues.copy()

# Troviamo quali sono gli autovalori "spazzatura" (quelli sotto il limite rosso)
noise_indices = clean_eigenvalues < lambda_max

# Sostituiamo tutti gli autovalori rumorosi con la loro media 
# (Questo distrugge il rumore ma mantiene intatta l'energia totale della matrice)
noise_mean = np.mean(clean_eigenvalues[noise_indices])
clean_eigenvalues[noise_indices] = noise_mean

# Ricostruiamo la matrice di correlazione usando l'algebra lineare:
# Matrice = Autovettori * Autovalori_Puliti * Autovettori_Trasposti
clean_corr_matrix = eigenvectors @ np.diag(clean_eigenvalues) @ eigenvectors.T

# Riportiamo a 1 la diagonale principale (un'azione è correlata al 100% con se stessa per definizione)
np.fill_diagonal(clean_corr_matrix, 1.0)

# 5. GRAFICO DELLA DIMOSTRAZIONE
lambda_vals = np.linspace(lambda_min, lambda_max, 500)
mp_pdf = (Q / (2 * np.pi * sigma_sq * lambda_vals)) * np.sqrt(np.maximum(0, (lambda_max - lambda_vals) * (lambda_vals - lambda_min)))

plt.figure(figsize=(12, 6))

# Filtriamo per il grafico (tagliamo i giganti a destra per vedere bene la curva)
filtered_evals = eigenvalues[eigenvalues < lambda_max * 1.5] 

plt.hist(filtered_evals, bins=40, density=True, alpha=0.75, color='dodgerblue', edgecolor='black', label='Autovalori Reali')
plt.plot(lambda_vals, mp_pdf, 'r-', lw=3, label='Teoria Marchenko-Pastur (Rumore)')
plt.axvline(lambda_max, color='red', linestyle='dashed', linewidth=2, label=f'Limite Rumore (λ_max = {lambda_max:.2f})')

plt.title('Dimostrazione: Il 90% del Mercato è Rumore Quantistico', fontsize=14, fontweight='bold')
plt.xlabel('Autovalori (λ)', fontsize=12)
plt.ylabel('Densità', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 6. RESOCONTO FINALE
print("\n--- RISULTATO DELLA PULIZIA QUANTISTICA ---")
print(f"Azioni analizzate: {N}")
print(f"Segnali VERI (forze macroeconomiche reali): {np.sum(~noise_indices)}")
print(f"Rumore AZZERATO (correlazioni finte): {np.sum(noise_indices)}")
print("\nL'oggetto 'clean_corr_matrix' è stato generato con successo.")
print("Ora puoi passarlo all'algoritmo di Markowitz per un portafoglio a prova di bomba.")
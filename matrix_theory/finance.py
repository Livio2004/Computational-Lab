import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM", "V", "JNJ", 
           "WMT", "PG", "MA", "UNH", "DIS", "HD", "BAC", "VZ", "KO", "PFE",
           "INTC", "CMCSA", "PEP", "CSCO", "NFLX", "ABT", "ADBE", "CRM", "NKE", "T",
           "MRK", "CVX", "XOM", "WFC", "MCD", "TXN", "MDT", "HON", "UNP", "IBM",
           "QCOM", "GS", "BA", "CAT", "MMM", "GE", "F", "GM", "AMD", "UBER"]

print("Scaricamento dati in corso (dal 2020 al 2024)...")
# Scarichiamo i dati
data = yf.download(tickers, start="2020-01-01", end="2024-01-01")['Close']

# --- FIX 1: Eliminiamo le colonne (azioni) difettose prima delle righe ---
# Se un'azione (come CMCSA) non è stata scaricata, buttiamo solo lei, non tutti i giorni!
data = data.dropna(axis=1, how='all')

# --- FIX 2: Risolto il FutureWarning con fill_method=None ---
returns = data.pct_change(fill_method=None).dropna()

# Standardizziamo i rendimenti
returns_norm = (returns - returns.mean()) / returns.std()

T, N = returns_norm.shape

# --- FIX 3: Controllo di sicurezza ---
if T == 0 or N == 0:
    print("ERRORE CRITICO: I dati sono vuoti. Prova a riavviare lo script (il database yfinance si sbloccherà).")
    exit()

Q = T / N  
print(f"Giorni analizzati (T): {T}, Azioni valide (N): {N}, Rapporto Q: {Q:.2f}")

# 3. Creiamo la Matrice di Correlazione empirica (quella "sporca")
corr_matrix = (returns_norm.T @ returns_norm) / T

# ... DA QUI IN POI IL CODICE RESTA IDENTICO A PRIMA ...
# 4. Estraiamo le "energie" del mercato: gli autovalori
eigenvalues = np.linalg.eigvalsh(corr_matrix)

# 5. Calcoliamo i limiti del RUMORE usando la Teoria di Marchenko-Pastur
sigma_sq = 0.6 
lambda_max = sigma_sq * (1 + np.sqrt(1/Q))**2
lambda_min = sigma_sq * (1 - np.sqrt(1/Q))**2

lambda_vals = np.linspace(lambda_min, lambda_max, 500)
mp_pdf = (Q / (2 * np.pi * sigma_sq * lambda_vals)) * np.sqrt(np.maximum(0, (lambda_max - lambda_vals) * (lambda_vals - lambda_min)))

# 6. PLOT
plt.figure(figsize=(12, 6))
zoom_limit = lambda_max * 2
filtered_evals = eigenvalues[eigenvalues < zoom_limit]

plt.hist(filtered_evals, bins=40, density=True, alpha=0.75, 
         color='dodgerblue', edgecolor='black', label='Autovalori Reali (Mercato)')

plt.plot(lambda_vals, mp_pdf, 'r-', lw=3, label='Rumore Quantistico (Marchenko-Pastur)')
plt.axvline(lambda_max, color='red', linestyle='dashed', linewidth=2, label=f'Limite Rumore ($\lambda_{{max}}$ = {lambda_max:.2f})')

plt.title('S&P 500: Separare il Vero Segnale Finanziario dal Rumore Statistico', fontsize=14, fontweight='bold')
plt.xlabel('Autovalori (λ)', fontsize=12)
plt.ylabel('Densità di Probabilità', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()

# 7. Il Verdetto Finale
signal_eigenvalues = eigenvalues[eigenvalues > lambda_max]
print("\n--- RISULTATO DELL'ANALISI ---")
print(f"Autovalori totali calcolati: {N}")
print(f"Autovalori classificati come VERO SEGNALE: {len(signal_eigenvalues)}")
print(f"Autovalori classificati come PURO RUMORE: {N - len(signal_eigenvalues)}")
print(f"Percentuale della matrice da 'buttare': {((N - len(signal_eigenvalues)) / N) * 100:.1f}%")
import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin 
from scipy.optimize import curve_fit


def lorentziana(E, F, M, gamma):
    return F/((E-M)**2+gamma**2/4)



E, y= np.loadtxt('data.txt', unpack = True)
C = np.loadtxt('cov.txt')
varianze = np.diag(C)
errori_y = np.sqrt(varianze)
X = np.vstack((np.ones_like(E), E, E**2)).T
y_inverso = 1/y
C_inverso = (1/y[:, None]**2)*C/(y[None,:]**2)
alpha, C_alpha, chi2 = lin.fit_lineare_generale(X, y_inverso,C_inverso)
a0, a1, a2 = alpha[0], alpha[1], alpha[2]

popt, pcov = curve_fit(
    lorentziana, 
    E, 
    y, 
    p0=[5000, 180, 300], 
    sigma=C, 
    absolute_sigma=True
)
F_fit = 1.0 / a2
M_fit = -a1 / (2 * a2)
Gamma_fit = 2 * np.sqrt((a0 / a2) - M_fit**2)

F_fit_scipy, M_fit_scipy, Gamma_fit_scipy = popt
errori_parametri = np.sqrt(np.diag(pcov))
N_simulazioni = 10000
parametri_simulati = np.random.multivariate_normal(popt, pcov, N_simulazioni)
E_plot = np.linspace(E.min(), E.max(), 200)

tutte_le_curve = np.zeros((N_simulazioni, len(E_plot)))

for i in range(N_simulazioni):
    p = parametri_simulati[i]
    tutte_le_curve[i, :] = lorentziana(E_plot, *p)

limite_inferiore = np.percentile(tutte_le_curve, 15.865, axis=0)
limite_superiore = np.percentile(tutte_le_curve, 84.135, axis=0)

# 5. Disegniamo!
y_fit_scip = lorentziana(E_plot, *popt)

plt.plot(E_plot, y_fit_scip, 'b-', label='Fit Centrale')
plt.fill_between(E_plot, limite_inferiore, limite_superiore, color='blue', alpha=0.3, label='Banda 1-Sigma (Monte Carlo)')
plt.legend()
plt.show()

print(" RISULTATI FITTING ")
print(f"Chi-quadro: {chi2:.2f}")
print(f"F Fit = {F_fit:.2f}")
print(f"M  Fit = {M_fit:.2f}")
print(f"Gama Fit = {Gamma_fit:.2f}")

E_1 = np.linspace(600,1000,200)
X_plot = np.vstack((np.ones_like(E_1), E_1, E_1**2)).T
y_fit = X_plot@alpha
lorentz = lorentziana(E_1, F_fit, M_fit, Gamma_fit)
lorentz_1 = lorentziana(E, F_fit, M_fit, Gamma_fit)
var_tilde = np.sum((X_plot @ C_alpha) * X_plot, axis=1)
sigma_tilde = np.sqrt(var_tilde)
sigma_lorentz = sigma_tilde*lorentz**2
var_tilde_1 = np.sum((X @ C_alpha) * X, axis=1)
sigma_tilde_1 = np.sqrt(var_tilde_1)
sigma_lorentz_1 = sigma_tilde_1*lorentz_1**2

fig, ax = plt.subplots(nrows=3, ncols =1, figsize=(11,7))
plt.title(f'Fit lorentziana con chi2 ={chi2:.2f}')

ax[0].plot(E_1, y_fit, label=f'parabola inverso lorentizana con chi quadro = {chi2:.2f}')
ax[0].scatter(E, y_inverso, color = 'green', label ='punti sperimentali')
ax[1].plot(E_1, lorentz, label ='Lorentziana dopo trasformazione della parabola')
ax[2].plot(E_plot, y_fit_scip, 'b-', label='Fit Centrale')
ax[2].fill_between(E_plot, limite_inferiore, limite_superiore, color='blue', alpha=0.3, label='Banda 1-Sigma (Monte Carlo)')
ax[1].fill_between(E_1,lorentz- sigma_lorentz, lorentz+sigma_lorentz)
ax[1].errorbar(E, lorentz_1,yerr =errori_y, barsabove= True, capsize=1, color = 'black',label = 'punti sperimentali' )
plt.legend()
plt.tight_layout()
plt.show()
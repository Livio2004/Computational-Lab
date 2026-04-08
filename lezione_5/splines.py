import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin 
from scipy.interpolate import make_interp_spline
runge = lambda x: 1/(1+25*x**2)
x_dati = np.linspace(-1,1,10)
y_dati = runge(x_dati)
x_plot = np.linspace(-1, 1, 500)

spline_lin = make_interp_spline(x_dati, y_dati, k=1)
spline_quad = make_interp_spline(x_dati, y_dati, k=2)
spline_cub = make_interp_spline(x_dati, y_dati, k=3)

plt.figure(figsize=(10, 6))
plt.plot(x_plot, spline_lin(x_plot), 'r--', label="Lineare (k=1) - Spigoli")
plt.plot(x_plot, spline_quad(x_plot), 'g-', label="Quadratica (k=2) - Liscia ma asimmetrica")
plt.plot(x_plot, spline_cub(x_plot), 'b-', label="Cubica (k=3) - fatta bene", linewidth=2)
plt.plot(x_dati, y_dati, 'ko', markersize=8, zorder=5)

plt.legend()
plt.title("Confronto tra Splines di grado diverso")
plt.grid(True, alpha=0.3)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# 1. Definizione Problema
f = lambda x, y: x * y
y_analyt = lambda x: 2 * np.exp(x**2 / 2)
y0 = 2
t_range = (0, 1.5)
h_val = 0.1

def forward_euler(f, y0, t_range, h):
    t = np.arange(t_range[0], t_range[1] + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(len(t) - 1):
        y[i+1] = y[i] + h * f(t[i], y[i])
    return t, y

# 2. Generazione dati
t_num, y_num = forward_euler(f, y0, t_range, h_val)
residui = np.abs(y_num - y_analyt(t_num))

# 3. Studio della convergenza (Global Error)
h_list = [0.2, 0.1, 0.05, 0.01, 0.005]
errors = [np.abs(forward_euler(f, y0, (0,1), h)[1][-1] - y_analyt(1)) for h in h_list]

# 4. Plotting
fig, ax = plt.subplots(2, 2, figsize=(12, 10))

# Soluzione
ax[0,0].plot(t_num, y_analyt(t_num), 'k', label='Analitica')
ax[0,0].plot(t_num, y_num, 'r--o', label=f'Euler h={h_val}')
ax[0,0].set_title("Confronto Soluzioni")

# Residui (Scala Log)
ax[0,1].semilogy(t_num, residui, 'b-o')
ax[0,1].set_title("Residui (Scala Log)")

# Lipschitz h*L
ax[1,0].plot(t_num, h_val * t_num, 'g')
ax[1,0].set_title("Fattore Lipschitz $h \cdot L(x)$")

# Convergenza (Log-Log)
ax[1,1].loglog(h_list, errors, 'ms-', label='Dati')
ax[1,1].loglog(h_list, h_list, 'k--', label='O(h) Line')
ax[1,1].set_title("Convergenza Globale $O(h)$")

plt.tight_layout()
plt.show()
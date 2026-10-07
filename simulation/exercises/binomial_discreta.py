import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

n = 20
p = 0.08

dist = stats.binom(n, p)

p_exacto = dist.pmf(2)

p_max3 = dist.cdf(3)

p_al_menos_1 = 1 - dist.pmf(0)

media = dist.mean()
desv = dist.std()

print(f"P(X = 2)  = {p_exacto:.4f}")
print(f"P(X <= 3) = {p_max3:.4f}")
print(f"P(X >= 1) = {p_al_menos_1:.4f}")
print(f"E[X] = {media:.4f}, Desv. est. = {desv:.4f}")

rng = np.random.default_rng(42)
simulados = rng.binomial(n, p, size=10_000)
print(f"Promedio simulado = {simulados.mean():.4f} (teórico = {media:.4f})")

x = np.arange(0, 9)
plt.bar(x - 0.2, dist.pmf(x), width=0.4, label="Teórica (PMF)")
plt.bar(x + 0.2, [np.mean(simulados == k) for k in x], width=0.4, label="Simulada")
plt.xlabel("Número de defectuosos")
plt.ylabel("Probabilidad")
plt.title("Binomial(n=20, p=0.08)")
plt.legend()
plt.show()

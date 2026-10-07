import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

mu = 5
sigma = 1.2

dist = stats.norm(loc=mu, scale=sigma)

p_menos_4 = dist.cdf(4)

p_entre = dist.cdf(7) - dist.cdf(4)

p_mas_8 = dist.sf(8)

percentil_95 = dist.ppf(0.95)

print(f"P(X < 4)     = {p_menos_4:.4f}")
print(f"P(4 < X < 7) = {p_entre:.4f}")
print(f"P(X > 8)     = {p_mas_8:.4f}")
print(f"Percentil 95 = {percentil_95:.2f} días")

rng = np.random.default_rng(42)
tiempos = rng.normal(mu, sigma, size=10_000)

print(f"\nSimulación:")
print(f"P(X < 4)     ≈ {np.mean(tiempos < 4):.4f}")
print(f"P(4 < X < 7) ≈ {np.mean((tiempos > 4) & (tiempos < 7)):.4f}")
print(f"P(X > 8)     ≈ {np.mean(tiempos > 8):.4f}")
print(f"Percentil 95 ≈ {np.percentile(tiempos, 95):.2f} días")

x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 300)
plt.hist(tiempos, bins=50, density=True, alpha=0.5, label="Simulación")
plt.plot(x, dist.pdf(x), "r-", lw=2, label="PDF teórica")
plt.axvline(percentil_95, color="k", linestyle="--", label="Percentil 95")
plt.xlabel("Días de entrega")
plt.ylabel("Densidad")
plt.title("Normal(μ=5, σ=1.2)")
plt.legend()
plt.show()

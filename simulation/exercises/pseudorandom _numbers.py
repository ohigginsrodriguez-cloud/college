a = 5
c = 3
m = 16
X0 = 7

X = X0
valores = []

for n in range(100):
    r = X / m
    valores.append(r)
    X = (a * X + c) % m

# Imprime solo los primeros y últimos para no saturar la consola
for n in range(0, 100):
    print(f"{n+1}: Xn={int(valores[n]*m)}, rn={valores[n]:.4f}")

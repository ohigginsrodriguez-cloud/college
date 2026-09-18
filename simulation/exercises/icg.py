def inverso_modular(x, modulo):
    if x == 0:
        return 0
    return pow(x, modulo - 2, modulo)


def generar_icg(
    semilla: int,
    cantidad: int,
    p: int = 2147483647,
    a: int = 1103515245,
    c: int = 12345,
):
    if not (0 <= semilla < p):
        raise ValueError(f"La semilla debe estar en el rango [0, {p - 1}]")
    if cantidad < 0:
        raise ValueError("La cantidad de valores a generar no puede ser negativa")

    resultados = []
    x = semilla
    for _ in range(cantidad):
        x = (a * inverso_modular(x, p) + c) % p
        resultados.append(x)

    return resultados


def generar_icg_normalizado(
    semilla: int,
    cantidad: int,
    p: int = 2147483647,
    a: int = 1103515245,
    c: int = 12345,
):
    """Devuelve valores en [0, 1)"""
    enteros = generar_icg(semilla, cantidad, p, a, c)
    return [val / p for val in enteros]

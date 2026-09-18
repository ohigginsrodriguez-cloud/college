from icg import generar_icg_normalizado


def simular_partido(
    prob_local: float,
    prob_visitante: float,
    ocasiones_local: int,
    ocasiones_visitante: int,
    semilla_local: int,
    semilla_visitante: int,
    duracion_partido: int = 90,
):

    def simular_equipo(nombre, prob, ocasiones, semilla):
        # Generamos 2 valores aleatorios por ocasion:
        # uno para decidir GOL/NO GOL, otro para el minuto en que ocurre
        aleatorios = generar_icg_normalizado(semilla, ocasiones * 2)

        goles = []
        fallos = []
        minutos_usados = set()

        for i in range(ocasiones):
            val_resultado = aleatorios[2 * i]
            val_minuto = aleatorios[2 * i + 1]

            # minuto de la ocasion (evitando repetir minuto exacto)
            minuto = int(val_minuto * duracion_partido) + 1
            while minuto in minutos_usados:
                minuto = (minuto % duracion_partido) + 1
            minutos_usados.add(minuto)

            if val_resultado < prob:
                goles.append(minuto)
            else:
                fallos.append(minuto)

        return {
            "equipo": nombre,
            "ocasiones_totales": ocasiones,
            "goles": sorted(goles),
            "fallos": sorted(fallos),
            "num_goles": len(goles),
        }

    resultado_local = simular_equipo(
        "Local", prob_local, ocasiones_local, semilla_local
    )
    resultado_visitante = simular_equipo(
        "Visitante", prob_visitante, ocasiones_visitante, semilla_visitante
    )

    marcador = f"{resultado_local['num_goles']} - {resultado_visitante['num_goles']}"

    return {
        "local": resultado_local,
        "visitante": resultado_visitante,
        "marcador_final": marcador,
    }


def imprimir_reporte(resultado):
    for lado in ("local", "visitante"):
        info = resultado[lado]
        print(f"\nEquipo {info['equipo']}:")
        print(f"  Ocasiones de gol: {info['ocasiones_totales']}")
        print(f"  Goles en el minuto: {info['goles']}")
        print(f"  Fallos en el minuto: {info['fallos']}")
        print(f"  Total de goles: {info['num_goles']}")

    print(f"\nResultado final: {resultado['marcador_final']}")


if __name__ == "__main__":
    prob_local = float(input("Probabilidad de anotar del equipo local (0-1): "))
    prob_visitante = float(input("Probabilidad de anotar del equipo visitante (0-1): "))
    ocasiones_local = int(input("Numero de ocasiones de gol del equipo local: "))
    ocasiones_visitante = int(
        input("Numero de ocasiones de gol del equipo visitante: ")
    )
    semilla_local = int(input("Semilla para el equipo local: "))
    semilla_visitante = int(input("Semilla para el equipo visitante: "))

    resultado = simular_partido(
        prob_local,
        prob_visitante,
        ocasiones_local,
        ocasiones_visitante,
        semilla_local,
        semilla_visitante,
    )

    imprimir_reporte(resultado)

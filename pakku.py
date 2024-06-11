from utils import PODER, cuadrado_suma_grupo


def aprox_pakku(maestros, k):
    """Algoritmo greedy propuesto en el enunciado."""
    # Formo los k grupos vacios
    grupos = []
    for _ in range(k):
        grupos.append([])

    # Ordeno los maestros por poder de forma decreciente
    maestros.sort(reverse = True, key = lambda m: m[PODER])

    for maestro in maestros:
        # Agrego el maestro al grupo de menor suma
        grupo = min(grupos, key=cuadrado_suma_grupo) # O(n), optimizable e.g. con dict?
        grupo.append(maestro)

    return grupos 
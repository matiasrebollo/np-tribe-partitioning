from utils import *


def aprox_pakku(maestros, k):
    """Algoritmo Greedy propuesto en el enunciado."""
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

def aprox_propia(maestros, k):
    """Algoritmo Greedy propuesto por nosotros"""
    grupos = []
    nuevo_grupo = []
    poder_acumulado = 0
    poder_ideal = sum(m[PODER] for m in maestros) / k

    # Ordeno los maestros por poder de forma decreciente
    maestros.sort(reverse=True, key = lambda m: m[PODER])

    for maestro in maestros:
        if poder_acumulado >= poder_ideal:
            grupos.append(nuevo_grupo)
            nuevo_grupo = []
            poder_acumulado = 0

        nuevo_grupo.append(maestro)
        poder_acumulado += maestro[PODER]
    
    grupos.append(nuevo_grupo)

    return grupos


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("USO: python src/pakku.py <path-a-dataset>")
    
    k, maestros = parse(sys.argv[1])

    print("\nSOLUCION POR APROXIMACION DE PAKKU")
    grupos_pakku = aprox_pakku(maestros, k)
    imprimir_solucion(grupos_pakku)

    print("\nSOLUCION POR APROXIMACION PROPUESTA")
    grupos_aprox_propia = aprox_propia(maestros, k)
    imprimir_solucion(grupos_aprox_propia)
    print("")
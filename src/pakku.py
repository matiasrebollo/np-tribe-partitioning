from utils import *


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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("USO: python src/pakku.py <path-a-dataset>")
    
    k, maestros = parse(sys.argv[1])

    print("\nSOLUCION POR APROXIMACION DE PAKKU (GREEDY)")
    grupos = aprox_pakku(maestros, k)
    imprimir_solucion(grupos)
    print("")
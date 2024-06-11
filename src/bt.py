from copy import deepcopy
from pakku import aprox_pakku
from utils import *


def backtracking(maestros, k):
    solucion_greedy = aprox_pakku(maestros, k) # Solucion aproximada
    solucion = [solucion_greedy, obtener_suma(solucion_greedy)]
    k_grupos_min_sum(maestros, [[] for _ in range(k)], 0, solucion)
    return solucion[0]

def k_grupos_min_sum(maestros, grupos, m, solucion):
    if m == len(maestros):  # Ya se le asigno grupo a todos los maestros
        suma_actual = obtener_suma(grupos)
        if suma_actual < solucion[1]:
            solucion[0] = deepcopy(grupos)
            solucion[1] = suma_actual
        return
    
    if obtener_suma(grupos) >= solucion[1]:  # No se termino de asignar grupo a todos los maestros pero la suma ya es mayor al optimo actual
        return

    for grupo in grupos:
        grupo.append(maestros[m])
        k_grupos_min_sum(maestros, grupos, m + 1, solucion)
        grupo.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("USO: python src/bt.py <path-a-dataset>")
    
    k, maestros = parse(sys.argv[1])

    print("\nSOLUCION POR BACKTRACKING")
    grupos = backtracking(maestros, k)
    imprimir_solucion(grupos)
    print("")
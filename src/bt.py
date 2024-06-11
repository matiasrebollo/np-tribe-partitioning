from copy import deepcopy
from pakku import aprox_pakku
from utils import *


def backtracking(maestros, k):
    solucion_greedy = aprox_pakku(maestros, k) # Solucion aproximada
    suma_greedy = obtener_suma(solucion_greedy)
    solucion = backtracking_rec(maestros, [[] for _ in range(k)], 0, solucion_greedy, suma_greedy)
    return solucion

def backtracking_rec(maestros, grupos, m, solucion_anterior, suma_anterior):
    if m == len(maestros): # Se le asigno grupo a todos los maestros
        suma_actual = obtener_suma(grupos)
        if suma_actual < suma_anterior:
            return deepcopy(grupos)
        return solucion_anterior
    
    if obtener_suma(grupos) >= suma_anterior: 
        # No se termino de asignar grupo a todos los maestros pero la suma ya es mayor al optimo actual
        return solucion_anterior
    
    optimo_actual = solucion_anterior
    suma_opt = suma_anterior
    
    for grupo in grupos:
        grupo.append(maestros[m])
        optimo_actual = backtracking_rec(maestros, grupos, m + 1, optimo_actual, suma_opt)
        suma_opt = obtener_suma(optimo_actual)
        grupo.pop()

    return optimo_actual

# def backtracking(maestros, k):
#     solucion_greedy = aprox_pakku(maestros, k) # Solucion aproximada
#     solucion = [solucion_greedy, obtener_suma(solucion_greedy)]
#     k_grupos_min_sum(maestros, [[] for _ in range(k)], 0, solucion)
#     return solucion[0]

# def k_grupos_min_sum(maestros, grupos, m, solucion):
#     if m == len(maestros):  # Ya se le asigno grupo a todos los maestros
#         suma_actual = obtener_suma(grupos)
#         if suma_actual < solucion[1]:
#             solucion[0] = deepcopy(grupos)
#             solucion[1] = suma_actual
#         return
    
#     if obtener_suma(grupos) >= solucion[1]:  # No se termino de asignar grupo a todos los maestros pero la suma ya es mayor al optimo actual
#         return

#     for grupo in grupos:
#         grupo.append(maestros[m])
#         k_grupos_min_sum(maestros, grupos, m + 1, solucion)
#         grupo.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("USO: python src/bt.py <path-a-dataset>")
    
    k, maestros = parse(sys.argv[1])

    print("\nSOLUCION POR BACKTRACKING")
    grupos = backtracking(maestros, k)
    imprimir_solucion(grupos)
    print("")
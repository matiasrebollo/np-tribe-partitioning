from csv import reader
from copy import deepcopy
import sys

NOMBRE = 0
PODER = 1


def parse(archivo):
    with open(archivo) as f:
        r = reader(f)
        k = int(next(r).pop())
        maestros_aux = [tuple(line) for line in r]
        maestros = [tuple([m, int(p)]) for (m, p) in maestros_aux]
    return k, maestros


def backtracking(maestros, k):
    solucion_greedy = aprox_pakku(maestros, k) # Solucion aproximada
    solucion = [solucion_greedy]
    k_grupos_min_sum(maestros, [[] for i in range(k)], 0, solucion)
    print(solucion)
    return solucion[0]


def k_grupos_min_sum(maestros, grupos, m, solucion):
    if m == len(maestros):  # Ya se le asigno grupo a todos los maestros
        if obtener_suma(grupos) < obtener_suma(solucion[0]):
            solucion[0] = deepcopy(grupos)
        return
    
    if obtener_suma(grupos) >= obtener_suma(solucion[0]):  # No se termino de asignar grupos pero la suma ya es mayor al optimo actual
        return

    for i in grupos:
        i.append(maestros[m])
        k_grupos_min_sum(maestros, grupos, m + 1, solucion)
        i.pop()


def obtener_suma(grupos):
    """Devuelve la suma de cuadrados total."""
    suma_total = 0
    for grupo in grupos:
        suma_total += suma_grupo(grupo) ** 2
    return suma_total


def suma_grupo(grupo):
    return(sum([i[PODER] for i in grupo]))


def aprox_pakku(maestros, k):
    """Algoritmo greedy propuesto en el enunciado"""

    # Formo los k grupos vacios
    grupos = []
    for i in range(k):
        grupos.append([])

    # Ordeno los maestros por poder de forma decreciente
    maestros.sort(reverse = True, key = lambda m: m[PODER])

    for maestro in maestros:
        # Agrego el maestro al grupo de menor suma
        grupo = min(grupos, key=suma_grupo) # O(n²), optimizable e.g. con dict
        grupo.append(maestro)

    return grupos    


def imprimir_grupos(grupos):
    contador = 1
    for grupo in grupos:
        print("Grupo", contador, end=": ")
        print(", ".join([i[NOMBRE] for i in grupo]))
        contador += 1

    print("Coeficiente: ", obtener_suma(grupos))



def main():
    if len(sys.argv) != 2:
        sys.exit("USAGE: python main.py <path-a-dataset>")
    
    k, maestros = parse(sys.argv[1])
    aprox = aprox_pakku(maestros, k)
    imprimir_grupos(aprox)
    print("")
    bt = backtracking(maestros, k)
    imprimir_grupos(bt)



if __name__ == '__main__':
    main()

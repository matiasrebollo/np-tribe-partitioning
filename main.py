from csv import reader
from copy import deepcopy
import sys
import pulp

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
    solucion = [solucion_greedy, obtener_suma(solucion_greedy)]
    k_grupos_min_sum(maestros, [[] for _ in range(k)], 0, solucion)
    return solucion[0]


def k_grupos_min_sum(maestros, grupos, m, solucion):
    if m == len(maestros):  # Ya se le asigno grupo a todos los maestros
        if obtener_suma(grupos) < solucion[1]:
            solucion[0] = deepcopy(grupos)
        return
    
    if obtener_suma(grupos) >= solucion[1]:  # No se termino de asignar grupo a todos los maestros pero la suma ya es mayor al optimo actual
        return

    for grupo in grupos:
        grupo.append(maestros[m])
        k_grupos_min_sum(maestros, grupos, m + 1, solucion)
        grupo.pop()


def obtener_suma(grupos):
    """Devuelve la suma de cuadrados total."""
    suma_total = 0
    for grupo in grupos:
        suma_total += cuadrado_suma_grupo(grupo)
    return suma_total


def cuadrado_suma_grupo(grupo):
    suma = 0
    for maestro in grupo:
        suma += maestro[PODER]
    return suma ** 2


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

def programacion_lineal(maestros, k):
    n = len(maestros)

    #Inicializamos el problema y sus variables
    problem = pulp.LpProblem("grupos_balanceados", pulp.LpMinimize)
    p = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(k)], cat = "Binary")
    S = pulp.LpVariable.dicts("S", range(k), cat = "Continuous")
    M = pulp.LpVariable("M", cat = "Continuous")
    m = pulp.LpVariable("m", cat = "Continuous")

    #Planteamos restricciones
    for i in range(n): #Cada maestro debe pertenecer exactamente a un grupo
        problem += pulp.lpSum(p[(i, j)] for j in range(k)) == 1
    for j in range(k): 
        problem += S[j] == pulp.lpSum(p[(i, j)] * maestros[i][PODER] for i in range(n)) #Calculamos las sumas de cada grupo
        problem += S[j] <= M
        problem += S[j] >= m
    problem += M - m
    problem.solve(pulp.PULP_CBC_CMD(msg=False))

    grupos = [[] for _ in range(k)]
    for j in range(k):
        grupo = [i for i in range(n) if pulp.value(p[(i, j)]) == 1]
        grupos[j] = [maestros[i] for i in grupo]
    return grupos



def imprimir_solucion(grupos):
    contador = 1
    for grupo in grupos:
        print("Grupo", contador, end=": ")
        print(", ".join([maestro[NOMBRE] for maestro in grupo]))
        contador += 1

    print("Coeficiente:", obtener_suma(grupos))



def main():
    if len(sys.argv) != 2:
        sys.exit("USAGE: python main.py <path-a-dataset>")
    
    k, maestros = parse(sys.argv[1])
    grupos_aprox = aprox_pakku(maestros, k)
    print("SOLUCION POR APROXIMACION DE PAKKU (GREEDY)")
    imprimir_solucion(grupos_aprox)

    print("\nSOLUCION POR BACKTRACKING")
    grupos_bt = backtracking(maestros, k)
    imprimir_solucion(grupos_bt)

    print("\nSOLUCION POR PROGRAMACION LINEAL")
    grupos_pl = programacion_lineal(maestros, k)
    imprimir_solucion(grupos_pl)
    


if __name__ == '__main__':
    main()

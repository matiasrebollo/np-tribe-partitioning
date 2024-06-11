import sys
import pulp
from utils import PODER, imprimir_solucion, parse


def programacion_lineal(maestros: list[tuple[str|int]], k: int):
    n = len(maestros)
    c = [i[PODER] for i in maestros]

    problem = pulp.LpProblem("grupos_balanceados", pulp.LpMinimize)
    # Por cada maestro i y por cada grupo j, defino una variable booleana: "i se encuentra en j"
    x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(k)], cat = "Binary")
    y = pulp.LpVariable.dicts("y", [(i, j, w) for i in range(n) for j in range(i+1, n) for w in range(k)], cat = "Binary")
    S = pulp.LpVariable.dicts("S", range(k), cat="Continuous")

    for i in range(n): # Cada maestro debe pertenecer exactamente a un grupo
        problem += pulp.lpSum(x[(i, j)] for j in range(k)) == 1

    for (i, j, w) in y.keys(): # Cada Y_(i,j,w) es X_(i,w) AND X_(j,w)
        problem += 2*y[(i, j, w)] <= x[(i, w)] + x[(j, w)]
        problem += x[(i, w)] + x[(j, w)] <= y[(i, j, w)] + 1
    
    for w in range(k):
        coefs = [i**2 for i in c] + [2*c[i]*c[j] for i in range(n) for j in range(i+1, n)]
        grupo_x = [x[(i, w)] for i in range(n)]
        grupo_y = [y[(i, j, w)] for i in range(n) for j in range(i+1, n)]
        grupo = grupo_x + grupo_y
        problem += S[w] == pulp.LpAffineExpression([(grupo[i], coefs[i]) for i in range(len(grupo))])

    problem += pulp.lpSum(S)
    problem.solve(pulp.PULP_CBC_CMD(msg=False))

    grupos = [[] for _ in range(k)]
    for j in range(k):
        grupo = [i for i in range(n) if pulp.value(x[(i, j)]) == 1]
        grupos[j] = [maestros[i] for i in grupo]
    
    return grupos

def aprox_programacion_lineal(maestros, k):
    n = len(maestros)

    # Inicializamos el problema y sus variables
    problem = pulp.LpProblem("grupos_balanceados", pulp.LpMinimize)
    p = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(k)], cat = "Binary")
    S = pulp.LpVariable.dicts("S", range(k), cat = "Continuous")
    M = pulp.LpVariable("M", cat = "Continuous")
    m = pulp.LpVariable("m", cat = "Continuous")

    # Planteamos restricciones
    for i in range(n):  # Cada maestro debe pertenecer exactamente a un grupo
        problem += pulp.lpSum(p[(i, j)] for j in range(k)) == 1
    for j in range(k): 
        problem += S[j] == pulp.lpSum(p[(i, j)] * maestros[i][PODER] for i in range(n))     # Calculamos las sumas de cada grupo
        problem += S[j] <= M
        problem += S[j] >= m
    problem += M - m
    problem.solve(pulp.PULP_CBC_CMD(msg=False))

    grupos = [[] for _ in range(k)]
    for j in range(k):
        grupo = [i for i in range(n) if pulp.value(p[(i, j)]) == 1]
        grupos[j] = [maestros[i] for i in grupo]

    return grupos


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("USAGE: python main.py <path-a-dataset>")
    
    k, maestros = parse(sys.argv[1])
    imprimir_solucion(programacion_lineal(maestros, k))

import pulp
from utils import *


def programacion_lineal(maestros: list[tuple[str|int]], k: int):
    n = len(maestros)
    x = [m[PODER] for m in maestros]

    problem = pulp.LpProblem("grupos_balanceados", pulp.LpMinimize)
    # Por cada maestro i y por cada grupo j, se define una variable booleana: "i se encuentra en j"
    p = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(k)], cat = "Binary")
    y = pulp.LpVariable.dicts("y", [(i, j, w) for i in range(n) for j in range(i+1, n) for w in range(k)], cat = "Binary")
    S = pulp.LpVariable.dicts("S", range(k), cat="Continuous")

    for i in range(n): # Cada maestro debe pertenecer a exactamente un grupo
        problem += pulp.lpSum(p[(i, j)] for j in range(k)) == 1

    for (i, j, w) in y.keys(): # Cada Y_(i,j,w) es X_(i,w) AND X_(j,w)
        problem += 2*y[(i, j, w)] <= p[(i, w)] + p[(j, w)]
        problem += p[(i, w)] + p[(j, w)] <= y[(i, j, w)] + 1
    
    for w in range(k):
        coefs = [i**2 for i in x] + [2*x[i]*x[j] for i in range(n) for j in range(i+1, n)]
        grupo_x = [p[(i, w)] for i in range(n)]
        grupo_y = [y[(i, j, w)] for i in range(n) for j in range(i+1, n)]
        grupo = grupo_x + grupo_y
        problem += S[w] == pulp.LpAffineExpression([(grupo[i], coefs[i]) for i in range(len(grupo))])

    problem += pulp.lpSum(S)
    problem.solve(pulp.PULP_CBC_CMD(msg=False))

    grupos = [[] for _ in range(k)]
    for j in range(k):
        grupo = [i for i in range(n) if pulp.value(p[(i, j)]) == 1]
        grupos[j] = [maestros[i] for i in grupo]
    
    return grupos

def aprox_programacion_lineal(maestros, k):
    n = len(maestros)

    # Se inicializa el problema y sus variables
    problem = pulp.LpProblem("grupos_balanceados", pulp.LpMinimize)
    p = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(k)], cat = "Binary")
    S = pulp.LpVariable.dicts("S", range(k), cat = "Continuous")
    M = pulp.LpVariable("M", cat = "Continuous")
    m = pulp.LpVariable("m", cat = "Continuous")

    # Se plantean restricciones
    for i in range(n):  # Cada maestro debe pertenecer exactamente a un grupo
        problem += pulp.lpSum(p[(i, j)] for j in range(k)) == 1
    for j in range(k): 
        problem += S[j] == pulp.lpSum(p[(i, j)] * maestros[i][PODER] for i in range(n))     # Se calculan las sumas de cada grupo
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
        sys.exit("USO: python src/pl.py <path-a-dataset>")
    
    k, maestros = parse(sys.argv[1])

    print("\nSOLUCION POR PROGRAMACION LINEAL")
    grupos = programacion_lineal(maestros, k)
    imprimir_solucion(grupos)
    
    print("\nSOLUCION POR PROGRAMACION LINEAL (APROXIMACION)")
    grupos_aprox = aprox_programacion_lineal(maestros, k)
    imprimir_solucion(grupos_aprox)
    print("")
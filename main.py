from csv import reader
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
    pass


def verificador():
    pass


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
        grupos.append(set())

    # Ordeno los maestros por poder de forma decreciente
    maestros.sort(reverse = True, key = lambda m: m[PODER])

    for maestro in maestros:
        # Agrego el maestro al grupo de menor suma
        grupo = min(grupos, key=suma_grupo) # O(n²), optimizable e.g. con dict
        grupo.add(maestro)

    return grupos    


def main():
    if len(sys.argv) != 2:
        sys.exit("USAGE: python main.py <path-a-dataset>")
    
    k, maestros = parse(sys.argv[1])
    print(k, maestros)
    print(aprox_pakku(maestros, k))



if __name__ == '__main__':
    main()

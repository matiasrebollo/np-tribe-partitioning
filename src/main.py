import sys
from bt import backtracking
from pakku import aprox_pakku
from pl import aprox_programacion_lineal, programacion_lineal
from utils import imprimir_solucion, parse


def main():
    if len(sys.argv) != 2:
        sys.exit("USAGE: python main.py <path-a-dataset>")
    
    k, maestros = parse(sys.argv[1])

    print("\nSOLUCION POR BACKTRACKING")
    grupos_bt = backtracking(maestros, k)
    imprimir_solucion(grupos_bt)

    print("\nSOLUCION POR PROGRAMACION LINEAL")
    grupos_pl = programacion_lineal(maestros, k)
    imprimir_solucion(grupos_pl)

    print("\nSOLUCION POR PROGRAMACION LINEAL (APROXIMACION)")
    grupos_aprox_pl = aprox_programacion_lineal(maestros, k)
    imprimir_solucion(grupos_aprox_pl)

    grupos_aprox_pakku = aprox_pakku(maestros, k)
    print("\nSOLUCION POR APROXIMACION DE PAKKU (GREEDY)")
    imprimir_solucion(grupos_aprox_pakku)
    print("")


if __name__ == '__main__':
    main()

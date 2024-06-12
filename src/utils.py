import datetime
import sys
from csv import reader

NOMBRE = 0
PODER = 1


def parse(archivo):
    with open(archivo) as f:
        r = reader(f)
        k = int(next(r).pop())
        maestros_aux = [tuple(line) for line in r]
        maestros = [tuple([m, int(p)]) for (m, p) in maestros_aux]
    return k, maestros

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

def imprimir_solucion(grupos):
    contador = 1
    for grupo in grupos:
        print("Grupo", contador, end=": ")
        print(", ".join([maestro[NOMBRE] for maestro in grupo]))
        contador += 1

    print("Coeficiente:", obtener_suma(grupos))

def mostrar_hora_inicio():
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Empezo a las", formatted_time)
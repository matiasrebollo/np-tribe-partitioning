from time import perf_counter
from utils import obtener_suma
from greedy import aprox_pakku, aprox_propia
from functools import partial
from random import randrange, randint
import matplotlib.pyplot as plt
import numpy as np

TAM_MUESTRA = 10
MAX_PODER = 1000000 # Numero grande, para que funcione randrange


def obtener_tiempo(metodo, n):
    """genera un set de n maestros y calcula el tiempo promedio en obtener
    el coeficiente de la partición mediante el metodo recibido."""
    x = [randrange(1, MAX_PODER) for _ in range(n)]
    x = list(zip(range(n), x))
    k = randint(1, n)

    tiempo_acumulado = 0

    for _ in range(TAM_MUESTRA):
        start = perf_counter()
        coeficiente = obtener_suma(metodo(x, k))
        fin = perf_counter()
        tiempo_acumulado += (fin - start)*1000

    return tiempo_acumulado/TAM_MUESTRA


if __name__ == "__main__":
    tamanio_datos = np.arange(100, 5000, 100)
    fun_1 = np.frompyfunc(partial(obtener_tiempo, aprox_pakku), 1, 1)
    fun_2 = np.frompyfunc(partial(obtener_tiempo, aprox_propia), 1, 1)
        
    tiempos_1 = fun_1(tamanio_datos)
    tiempos_2 = fun_2(tamanio_datos)

    plt.title("Comparación de complejidad de algoritmos de aproximacion")
    plt.xlabel("tamaño de entrada")
    plt.ylabel("tiempo consumido [ms]")

    plt.plot(tamanio_datos, tiempos_1, 'b-',label='mediciones aprox pakku')
    plt.plot(tamanio_datos, tiempos_2, 'r-',label='mediciones aprox grupal')
 
    plt.legend()
    plt.tight_layout()
    plt.savefig("grafico_complejidad.png")
    plt.show()
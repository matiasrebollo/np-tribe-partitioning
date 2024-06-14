from time import perf_counter
from utils import obtener_suma
from greedy import aprox_pakku, aprox_propia
from functools import partial
from random import randrange, randint
import matplotlib.pyplot as plt
import numpy as np

MAX_PODER = 1000000 # Numero grande, para que funcione randrange
COTA_APROX_PAKKU = 1.003952
COTA_APROX_PROPIA = 1.536598

def generar_data(n):
    x = [randrange(1, MAX_PODER) for _ in range(n)]
    x = list(zip(range(n), x))
    k = randint(1, n)

    return x, k

if __name__ == "__main__":
    tamanio_datos = [i for i in range(100, 1000, 50)]
    coefs_1 = []    # obtenidos por la aprox de pakku
    coefs_2 = []    # obtenidos por nuestra aproximacion

    for n in tamanio_datos:
        x, k = generar_data(n)
        coefs_1.append(obtener_suma(aprox_pakku(x, k)))
        coefs_2.append(obtener_suma(aprox_propia(x, k)))
    
    valor_esperado_1 = [i/COTA_APROX_PAKKU for i in coefs_1]
    valor_esperado_2 = [i/COTA_APROX_PROPIA for i in coefs_2]
        
    plt.title("Comparación de optimidad de algoritmos de aproximacion y ")
    plt.xlabel("tamaño de entrada")
    plt.ylabel("valor coeficiente")

    plt.scatter(tamanio_datos, coefs_1, s=10,label='aprox pakku')
    plt.scatter(tamanio_datos, coefs_2, s=10,label='aprox grupal')
    plt.scatter(tamanio_datos, valor_esperado_1, s=10, label='minimo coeficiente esperado segun pakku')
    plt.scatter(tamanio_datos, valor_esperado_2, s=10, label='minimo coeficiente esperado segun nosotros')
 
    plt.legend(fontsize=7, loc='best')
    plt.tight_layout()
    plt.savefig("grafico_coeficientes.png")
    plt.show()
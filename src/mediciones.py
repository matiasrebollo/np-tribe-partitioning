import random

from bt import backtracking
from greedy import *
from utils import obtener_suma

MAX_MAESTROS = 10
MAX_GRUPOS = 8

def generar_dataset(n):
    NOMBRES = ["Pakku", "Yue", "Yakone", "Wei", "Hasook", "Senna", "Hama", "Amon", "Sangok", "Misu"]
    return [tuple([NOMBRES[i], random.randint(1, 1000)]) for i in range(n)]

def buscar_cotas_aprox():
    cota_pakku = 1
    cota_aprox_propia = 1
    for n in range(1, MAX_MAESTROS):
        for k in range(1, MAX_GRUPOS):
            maestros = generar_dataset(n)

            grupos_bt = backtracking(maestros, k)
            coef_opt = obtener_suma(grupos_bt)
            grupos_pakku = aprox_pakku(maestros, k)
            coef_pakku = obtener_suma(grupos_pakku)
            grupos_aprox_propia = aprox_propia(maestros, k)
            coef_aprox_propia = obtener_suma(grupos_aprox_propia)

            if coef_pakku / coef_opt > cota_pakku:
                cota_pakku = coef_pakku / coef_opt
            if coef_aprox_propia / coef_opt > cota_aprox_propia:
                cota_aprox_propia = coef_aprox_propia / coef_opt
    
    print("Cota aproximacion de Pakku: ", cota_pakku)
    print("Cota aproximacion propia: ", cota_aprox_propia)

def main():
    buscar_cotas_aprox()

if __name__ == '__main__':
    main()
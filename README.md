# Trabajo Práctico 3: Problemas NP-Completos para la defensa de la Tribu del Agua
## Ejecución

- Para ejecutar **todos** los distintos métodos implementados para un determinado dataset, ingresar en una terminal (desde el root del repositorio):
    |   `python src/main.py <path-a-dataset>` |
    |:-------:|
    
    Por ejemplo: `python src/main.py pruebas_drive/5_2.txt`
    
    El programa imprimirá por pantalla los grupos y el coeficiente obtenido para cada uno de los algoritmos utilizados, incluyendo los de aproximación.
- Para ejecutar únicamente el algoritmo de Backtracking, ingresar:
    |   `python src/bt.py <path-a-dataset>` |
    |:-------:|
- Para ejecutar los algoritmos de Programación Lineal, ingresar:
    |   `python src/pl.py <path-a-dataset>` |
    |:-------:|
- Para ejecutar los algoritmos Greedy de aproximación, ingresar:
    |   `python src/greedy.py <path-a-dataset>` |
    |:-------:|
- Para ejecutar **todos** los tests, ingresar:
    |`python tests.py`  |
    |:-------:|
- Para ejecutar un test en particular, ingresar:
    |`python tests.py Test.<nombre-del-test>`  |
    |:-------:|
    
    Por ejemplo: `python tests.py Test.test_drive_5_2`

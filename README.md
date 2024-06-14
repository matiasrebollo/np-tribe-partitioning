# Trabajo Práctico 3: Problemas NP-Completos para la defensa de la Tribu del Agua

## Introducción

Es el año 95 DG. La Nación del Fuego sigue su ataque, esta vez hacia la Tribu del Agua, luego de una humillante derrota a manos del Reino de la Tierra, gracias a nuestra ayuda. La tribu debe defenderse del ataque.

El maestro Pakku ha recomendado hacer lo siguiente: Separar a todos los Maestros Agua en $k$ grupos (S1,S2,⋯,Sk​). Primero atacará el primer grupo. A medida que el primer grupo se vaya cansando entrará el segundo grupo. Luego entrará el tercero, y de esta manera se busca generar un ataque constante, que sumado a la ventaja del agua por sobre el fuego, buscará lograr la victoria.

En función de esto, lo más conveniente es que los grupos estén parejos para que, justamente, ese ataque se mantenga constante.

Conocemos la fuerza/maestría/habilidad de cada uno de los maestros agua, la cuál podemos cuantificar diciendo que para el maestro i ese valor es xi​, y tenemos todos los valores $x_1,x_2, \cdots ,x_n$​ (todos valores positivos).

Para que los grupos estén parejos, lo que buscaremos es minimizar la adición de los cuadrados de las sumas de las fuerzas de los grupos. Es decir:

$$
\min{\sum^{k}_{i=1}} {\left({\sum\_{x_j\in S_i}x_j}\right)}^2
$$

El Maestro Pakku nos dice que esta es una tarea difícil, pero que con tiempo y paciencia podemos obtener el resultado ideal.


## Consigna

Para los primeros dos puntos, considerar la versión de decisión del Problema de la Tribu del Agua:

Dado una secuencia de n fuerzas/habilidades de maestros agua $x_1,x_2, \cdots ,x_n$ y dos números $k$ y $B$, definir si existe una partición en $k$ subgrupos S1,S2,⋯ ,Sk​ tal que:

$$
\min{\sum^{k}_{i=1}} {\left({\sum\_{x_j\in S_i}x_j}\right)}^2 \le B
$$

Cada elemento $x_i$ debe estar asignado a un grupo y sólo un grupo.

Demostrar que el Problema de la Tribu del Agua se encuentra en NP.

Demostrar que el Problema de la Tribu del Agua es, en efecto, un problema NP-Completo. Si se hace una reducción involucrando un problema no visto en clase, agregar una (al menos resumida) demostración que dicho problema es NP-Completo.

Escribir un algoritmo que, por backtracking, obtenga la solución óptima al problema (valga la redundancia) en la versión de optimización planteada originalmente. Generar sets de datos para corroborar su correctitud, así como tomar mediciones de tiempos.

Escribir un modelo de programación lineal que resuelva el problema de forma óptima. Ejecutarlo para los mismos sets de datos para corroborar su correctitud. Tomar mediciones de tiempos y compararlas con las del algoritmo que implementa Backtracking.

El Maestro Pakku nos propone el siguiente algoritmo de aproxiamción: Generar los k grupos vacíos. Ordenar de mayor a menor los maestros en función de su habilidad o fortaleza. Agregar al más habilidoso al grupo con menos habilidad hasta ahora (cuadrado de la suma). Repetir siguiendo con el siguiente más habilidoso, hasta que no queden más maestros por asignar.

Este algoritmo sirve como una aproximación para resolver el problema de la tribu del agua. Implementar dicho algoritmo, analizar su complejidad y analizar cuán buena aproximación es. Para esto, considerar lo siguiente: Sea I una instancia cualquiera del problema, y z(I) una solución óptima para dicha instancia, y sea A(I) la solución aproximada, se define A(I)/z(I)≤r(A) para todas las instancias posibles. Realizar mediciones utilizando el algoritmo exacto y la aproximación, con el objetivo de definir dicha relación. Realizar también mediciones que contemplen volúmenes de datos ya inmanejables para el algoritmo exacto, a fin de corroborar empíricamente la cota calculada anteriormente (implementando para sets de datos cuya solución se sepa de antemano). Para este punto no es requisito la demostracion formal de la cota.

Opcional: Implementar alguna otra aproximación (o algoritmo greedy) que les parezca de interés. Comparar sus resultados con los dados por la aproximación del punto anterior. Indicar y justificar su complejidad. No es obligatorio hacer este punto para aprobar el trabajo práctico (pero si resta puntos no hacerlo).

Agregar cualquier conclusión que parezca relevante.

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

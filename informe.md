# Objetivo


# Análisis del problema
## El problema es NP

Para demostrar que el problema está en NP, basta con implementar un verificador del problema de complejidad polinomial en funcion a la entrada.
En otras palabras, debemos implementar un programa que, dado un conjunto de $n$ maestros $M$, una cantidad de grupos $k$, un numero $B$, y $l$ conjuntos $S_1, S_2, \cdots, S_l$, defina si esos conjuntos son una solución al problema de los maestros de agua.

$S$ es solución si cumple con las siguientes condiciones:
+ $S_1, S_2, \cdots, S_n$ es partición de $M$.
+ $l = k$
+
$$
\sum^{k}_{i=1} {\left({\sum\_{x_j\in S_i}x_j}\right)}^2 \le B
$$

A continuacion se presenta la implementacion de dicho algoritmo en python:


```python

def verificar_solucion(M: set, k: int, B: int, S: list[set]) -> bool:
  # S = [S_1, S_2, ... S_l]  |M| = n
  copia = M.copy()
  if len(S) != k:
    return False

  for S_i in S:  # k iteraciones
    for i in S_i:  # n/k iteraciones en promedio
      if i not in M:  # O(1)
        return False
      copia.discard(i)  # O(1)

  if len(copia) != 0:
    return False

  return obtener_suma(S) <= B  # O(n)

```

Complejidad Temporal: $\mathcal{O}(n)$ en funcion de la entrada. falta justificar un poco


## El problema es NP-Completo

El problema de los maestros del agua (llamesmoslo MA) es un porblema NP-Completo si cumple con las siguientes condiciones:

1. El problema está en NP (Ya demostrado)
2. Cualquier problema NP-Completo puede reducirse polinomialmente a este problema.

Para demostrar la segunda condición basta con reducir algún problema NP-Completo a MA. Para esto buscaremos reducir el problema de Subset Sum, el cual se sabe que es NP-Completo, al problema de los maestros.

Definimos el problema de Subset Sum (SS): dado un conjunto S de n enteros positivos, y un numero T, decidir si existe un subconjunto de S tal que la suma delos elementos de tal subconjunto es T.

#### Reducción SS a MA

+ Defino $n$ maestros por cada elemento de $S$, con un poder equivalente al valor del mismo (nos referirimos a este conjuto de maestros como $S$ a lo largo de la reducción) .
+ Defino dos maestros adicionales, $z_1$ con $poder(z_1) = sum(S)$, y $z_2$ con $poder(z_2) = 2T$, tal que el poder total de todos los maestros equivale a $2(sum(S) + T)$.
+ Llamo al MA con $k = 2$, $M = \set\{S \cup z_1 \cup z_2\}$ y $B = 2(sum(S) + T)^2$. 
 
#### si hay MA

Para empezar vale la pena observar que, como se busca que los grupos queden lo más balanceados posibles, la mejor solución posible al problema de los maestros será aquella donde se logran formar k grupos con una suma igual de elementos. En tal caso, si llamamos $m$ al poder total de los maestros, cada grupo tendrá $m/k$ poder acumulado.

En este caso, $m = 2(sum(S) + T)$ y $k = 2$, por lo que cada grupo debería tener $(sum(S) + T)$ de poder total para llegar al mejor caso posible.
Desarrollamos el coeficiente para este mejor caso:

$$
\sum^{k}_{i=1} {\left({\sum\_{x_j\in S_i}x_j}\right)}^2 = (T + sum(S))^2 + (T + sum(S))^2 = 2(T + sum(S))^2
$$

Observamos que el coeficiente para el mejor caso coincide con el $B$ que se le dió al problema, por lo que si existe una solución con un coeficiente de a lo sumo B, existe una forma de repartir los maestros en dos grupos tal que cada grupo suma $(sum(S) + T)$ en total.

Entonces, $z_1$ y $z_2$ no pueden estar en el mismo grupo, pues juntos suman $(sum(S) + 2T)$. Si un grupo $S_1$ contiene al maestro $z_1$, necesitará un subconjunto de $S$ que llegue a $T$, i.e. **necesita a la solucion del SS**. Por otra parte, si el grupo contiene a $z_2$, necesitara de un subconjunto de maestros cuyo poder total sume $(sum(S) - T)$, dicho grupo se obtiene de aquellos elementos que no se hayan usado en la solución del SS. 

Por lo tanto, si se encontró solución al MA con $B = 2(sum(S) + T)^2$, debe existir solución de SS.

#### si hay SS

Supongamos que existe una solucion $S\'$ tal que $sum(S\') = T$, entonces $sum(S\' \cup z1) = sum(S-S\'\cup z2)$ por lo que puedo dividir en dos grupos de mismo poder $S_1 = \set\{S\', z_1\}$ y $S_2 = \set\{S-S\', z_2\}$, y se tratará de la mejor solución al problema de los maestros. Si desarrollamos el coeficiente:

$$
\sum^{k}_{i=1} {\left({\sum\_{x_j\in S_i}x_j}\right)}^2 = sum(S_1)^2 + sum(S_2)^2 = (T + sum(S))^2 + (sum(S)-T + 2T)^2 = (T + sum(S))^2 + (sum(S) + T)^2 = 2(T + sum(S))^2
$$

Por lo tanto existirá una división de maestros tal que 

$$
\sum^{k}_{i=1} {\left({\sum\_{x_j\in S_i}x_j}\right)}^2 \le 2(T + sum(S))^2
$$

Finalmente, $SS \le_{p} MA$, y como MA es NP, el problema de los maestros de agua es un problema NP-Completo.
 

# Algoritmos y complejidad
## Backtracking
## Programación lineal
## Greedy

# Casos de prueba


# Mediciones


# Conclusiones

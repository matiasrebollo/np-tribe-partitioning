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

Complejidad Temporal: $\mathcal{O}(n)$ en funcion de la entrada.


## El problema es NP-Completo

# Algoritmos y complejidad
## Backtracking
## Programación lineal
## Greedy

# Casos de prueba


# Mediciones


# Conclusiones

# Objetivo
En el presente trabajo se llevará a cabo el desarrollo y análisis de algoritmos de Backtracking y Programación Lineal para resolver un problema NP-Completo, así como el análisis de posibles aproximaciones. También se realizará una demostración de la clase de complejidad del mismo.

# Análisis del problema
## El problema está en NP
Para demostrar que el problema de la Tribu del Agua se encuentra en NP, basta con implementar un certificador eficiente de soluciones del mismo que sea de complejidad polinomial en función al tamaño de la entrada. En otras palabras, debemos implementar un algoritmo que, dado un conjunto de $n$ maestros $M$ cada uno con su poder $x_i$, una cantidad de grupos $k$, un número $B$, y $l$ conjuntos $S_1, S_2,..., S_l$, defina si esos conjuntos son una solución al problema en cuestión.

$S$ es solución si cumple con las siguientes condiciones:
+ $S_1, S_2,..., S_n$ es partición de $M$
+ $l = k$
+
$$
 \sum^{k}_{i=1} {\left({\sum_{x_j\in S_i}x_j}\right)}^2 \le B
$$

A continuación se presenta la implementación de dicho algoritmo en Python:

```python
def verificar_solucion(M: set, k: int, B: int, S: list[set]) -> bool:
  # S = [S_1, S_2, ... S_l]  |M| = n
  copia = M.copy()
  if len(S) != k:
    return False

  # O(k) * O(n/k) = O(n)
  for S_i in S:  # k iteraciones
    for maestro in S_i:  # n/k iteraciones en promedio
      if maestro not in M:  # O(1)
        return False
      copia.discard(maestro)  # O(1)

  if len(copia) != 0:
    return False

  return obtener_suma(S) <= B  # O(k) * O(n/k) = O(n)
  
def obtener_suma(S):
  suma_total = 0
  for S_i in S:   # O(k)
      suma_total += cuadrado_suma_grupo(S_i)
  return suma_total

def cuadrado_suma_grupo(S_i):
  suma = 0
  for maestro in S_i:   # O(n/k)
      suma += maestro[PODER]
  return suma ** 2
```

La complejidad temporal del verificador es $\mathcal{O}(n)$ + $\mathcal{O}(n)$ = $\mathcal{O}(n)$ en función de la entrada.

## El problema es NP-Completo
El problema de la Tribu del Agua (a partir de ahora TA) es NP-Completo si cumple con las siguientes condiciones:
1. [El problema está en NP (demostrado en la sección anterior)](#el-problema-está-en-np).
2. Cualquier problema NP-Completo puede reducirse polinomialmente a este problema.

Para comprobar la segunda condición se plantea reducir el problema de Subset Sum, el cual se sabe que es NP-Completo, al problema en cuestión.

Se define el problema de Subset Sum (SS) de la siguiente manera: Dado un conjunto $S$ de $n$ enteros positivos y un número $T$, decidir si existe un subconjunto de $S$ tal que la suma de los elementos del mismo es $T$.

### Reducción SS a TA
+ Se definen $n$ maestros, uno por cada elemento de $S$, con un poder $x_i$ equivalente al valor del mismo (se referirá a este conjunto de maestros como $S$ a lo largo de la reducción).
+ Se agregan dos maestros adicionales: 
  + $z_1 = sum(S)$ 
  + $z_2 = 2T$
 
  El poder total de todos los maestros ahora equivale a $m = 2(sum(S) + T)$.
+ Se llama a TA con:
  + $M = \{S \cup z_1 \cup z_2\}$
  + $k = 2$   
  + $B = 2(sum(S) + T)^2$ 
 
#### Si hay solución a TA
Para empezar vale la pena observar que, como se busca que los grupos queden lo más balanceados posible, la mejor solución posible es aquella en donde se logran formar $k$ grupos con sumas equivalentes de los elementos que los conforman. Entonces, siendo $m$ el poder total de los maestros, cada grupo tendrá $m/k$ poder acumulado.

Para esta reducción, $m = 2(sum(S) + T)$ y $k = 2$, por lo que cada grupo deberá tener $sum(S) + T$ de poder total en el caso ideal. Desarrollando el coeficiente para este escenario:

$$
\sum^{k}_{i=1} {\left({\sum_{x_j\in S_i}x_j}\right)}^2 = sum(S_1)^2 + sum(S_2)^2 = (sum(S) + T)^2 + (sum(S) + T)^2 = 2(sum(S) + T)^2
$$

Se puede ver que el coeficiente para el mejor caso coincide con el $B$ que se le dió al problema, por lo que si existe una solución con un coeficiente de a lo sumo $B$, existe una forma de repartir los maestros en dos grupos tal que cada grupo suma $sum(S) + T$.

Entonces, $z_1$ y $z_2$ no pueden estar en el mismo grupo porque juntos suman $sum(S) + 2T$. Si un grupo $S_1$ contiene al maestro $z_1$, necesita un subconjunto de $S$ que sume $T$, i.e. **necesita a la solución del SS**. Por otra parte, si el grupo contiene a $z_2$, necesita de un subconjunto de maestros cuyo poder total sume $sum(S) - T$. Este subconjunto se obtiene de aquellos elementos que no se hayan usado en la solución del SS. 

Por lo tanto, si se encuentra solución a TA con $B = 2(sum(S) + T)^2$, debe existir solución a SS.

#### Si hay solución a SS
Suponiendo que existe una solución $S'$ tal que $sum(S') = T$, entonces $sum(S' \cup z1) = sum(S-S'\cup z2)$ por lo que es posible dividir en dos grupos de mismo poder $S_1 = \set{S', z_1}$ y $S_2 = \set{S-S', z_2}$, que es la mejor solución a TA. Desarrollando el coeficiente:

$$
\sum^{k}_{i=1} {\left({\sum_{x_j\in S_i}x_j}\right)}^2 = sum(S_1)^2 + sum(S_2)^2 = (sum(S) + T)^2 + (sum(S)-T + 2T)^2 = (sum(S) + T)^2 + (sum(S) + T)^2 = 2(sum(S) + T)^2
$$

Por lo tanto, existe una división de maestros tal que:

$$
\sum^{k}_{i=1} {\left({\sum_{x_j\in S_i}x_j}\right)}^2 \le 2(T + sum(S))^2
$$

Finalmente, SS $\le_{p}$ TA y como TA es NP, también es NP-Completo.
 
# Algoritmos y complejidad
## Backtracking

## Programación lineal
### Versión Óptima
#### Constantes

+ $n$: Número de maestros agua.
+ $k$: Número de grupos.
+ $c_i$: Habilidad del maestro $i$ (valores positivos).

#### Variables

+ $X_{ij}$: Variable booleana, "maestro $i$ en el grupo $j$"
+ $Y_{ijw}$: Variable booleana, $X_{iw} \land X_{jw}$
+ $S_i$: Cuadrado de la suma de poder de los maestros del grupo $i$.

#### Restricciones

+ _Cada maestro i debe ser asignado a un único grupo:_

$$
\sum_{j=1}^{k} X_{ij} = 1 \forall i
$$

+ $Y_{ijw} = X_{iw} \land X_{jw}$:

$$
2Y_{ijw} \le X_{iw} + X_{jw} \le Y_{ijw} + 1
$$

+ Desarrollo del cuadrado de la suma de poderes de un grupo:

$$
S_w = \left({\sum\_{i = 1}^{n}c_i\cdot X_{iw}}\right)^2 = \sum\_{i = 1}^{n}c_i^2\cdot X_{iw} + 2\left({\sum_{i=1}^{n}\sum\_{j = i+1}^{n}c_ic_j\cdot Y_{ijw}}\right) \forall w
$$

#### Función objetivo

$$
\min \sum_{i=1}^k S_i
$$

### Versión Aproximada

#### Definición de variables

+ $n$: Número de maestros agua.
+ $k$: Número de grupos.
+ $x_i$: Habilidad del maestro $i$ (valores positivos).
+ $p_{ij}$: Variable binaria que indica si el maestro $i$ está en el grupo $j$ ($p_{ij} = 1$) o no ($p_{ij} = 0$).
+ $S_j$: Suma de habilidades del grupo $j$.
+ $M$: Máxima suma de habilidades entre todos los grupos.
+ $m$: Mínima suma de habilidades entre todos los grupos.

#### Función objetivo

El objetivo es minimizar la diferencia entre la suma de habilidades del grupo con la mayor suma y el grupo con la menor suma:

$$
Minimizar: Z = M - m
$$

... falta
## Greedy

# Casos de prueba


# Mediciones


# Conclusiones
- El problema de la Tribu del Agua efectivamente está en NP y es NP-Completo.
# Objetivo
En el presente trabajo se llevará a cabo el desarrollo y análisis de algoritmos de Backtracking y Programación Lineal para resolver un problema NP-Completo, así como el análisis de posibles aproximaciones. También se realizará una demostración de la clase de complejidad del mismo.

# Análisis del problema
Se define la versión de decisión del problema de la Tribu del Agua de la siguiente manera:

Dada una secuencia de $n$ fuerzas/habilidades/poderes de maestros de agua $x_1,x_2 \ldots x_n$, y dos números $k$ y $B$, definir si existe una partición en $k$ subgrupos $S_1, S_2, \ldots, S_k$ tal que:

$$
\sum_{i=1}^{k} \left({\sum_{x_j\in S_i}x_j}\right)^2 \le B
$$

## El problema es NP-Completo
El problema de la Tribu del Agua (a partir de ahora TA) es NP-Completo si cumple con las siguientes condiciones:
1. [El problema se encuentra en NP](#el-problema-se-encuentra-en-np).
2. [Cualquier problema NP-Completo puede reducirse polinomialmente a este problema](#cualquier-problema-np-completo-puede-reducirse-polinomialmente-a-este-problema).

### El problema se encuentra en NP
Para demostrar que el problema de la Tribu del Agua está en NP, basta con implementar un certificador eficiente de soluciones del mismo que sea de complejidad polinomial en función al tamaño de la entrada. En otras palabras, debemos implementar un algoritmo que, dado un conjunto de $n$ maestros $M$ cada uno con su poder $x_i$, una cantidad de grupos $k$, un número $B$, y $l$ conjuntos $S_1, S_2, \ldots, S_l$, defina si esos conjuntos son una solución al problema en cuestión.

$S$ es solución si cumple con las siguientes condiciones:
+ $S_1, S_2, \ldots, S_n$ es partición de $M$
+ $l = k$
+ $\sum_{1 \le i \le k}\left({\sum_{x_j\in S_i}x_j}\right)^2 \le B$

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

La complejidad temporal del verificador es $\mathcal{O}(n)$ + $\mathcal{O}(n)$ = $\mathcal{O}(n)$ en función de la entrada. Por lo tanto, TA $\in$ NP.

### Cualquier problema NP-Completo puede reducirse polinomialmente a este problema

Para comprobar la segunda condición se plantea reducir el problema de Subset Sum, el cual se sabe que es NP-Completo, al problema en cuestión.

Se define el problema de Subset Sum (SS) de la siguiente manera: 

Dado un conjunto $S$ de $n$ enteros positivos y un número $T$, decidir si existe un subconjunto de $S$ tal que la suma de los elementos del mismo es $T$.

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
Para empezar vale la pena observar que, como se busca que los grupos queden lo más balanceados posible, la solución ideal es aquella en donde se logran formar $k$ grupos con sumas equivalentes de los elementos que los conforman. Entonces, siendo $m$ el poder total de los maestros, cada grupo tendrá $m/k$ poder acumulado.

Para esta reducción, $m = 2(sum(S) + T)$ y $k = 2$, por lo que cada grupo deberá tener $sum(S) + T$ de poder total en el caso ideal. Desarrollando el coeficiente para este escenario:

$$
\sum_{i=1}^{k} {\left({\sum_{x_j\in S_i}x_j}\right)}^2 = sum(S_1)^2 + sum(S_2)^2 = (sum(S) + T)^2 + (sum(S) + T)^2 = 2(sum(S) + T)^2
$$

Se puede apreciar que el coeficiente para el mejor caso coincide con el $B$ que se le dio al problema, por lo que si existe una solución con un coeficiente de a lo sumo $B$, existe una forma de repartir los maestros en dos grupos tal que cada grupo suma $sum(S) + T$.

Entonces, $z_1$ y $z_2$ no pueden estar en el mismo grupo porque juntos suman $sum(S) + 2T$. Si un grupo $S_1$ contiene al maestro $z_1$, necesita un subconjunto de $S$ que sume $T$, i.e. **necesita a la solución de SS**. Por otra parte, si el grupo contiene a $z_2$, necesita de un subconjunto de maestros cuyo poder total sume $sum(S) - T$. Este subconjunto se obtiene de aquellos elementos que no se hayan usado en la solución de SS. 

Por lo tanto, si se encuentra solución a TA con $B = 2(sum(S) + T)^2$, existe solución a SS.

#### Si hay solución a SS
Suponiendo que existe una solución $S'$ tal que $sum(S') = T$, entonces $sum(S' \cup z1) = sum(S-S'\cup z2)$. Por consiguiente, es posible dividir $S$ en dos grupos de mismo poder $S_1 = \set{S', z_1}$ y $S_2 = \set{S-S', z_2}$, que es la mejor solución a TA. Desarrollando el coeficiente:

$$
\sum_{i=1}^{k} {\left({\sum_{x_j\in S_i}x_j}\right)}^2 = sum(S_1)^2 +  sum(S_2)^2 = (T + sum(S))^2 + (sum(S)-T + 2T)^2 = (sum(S) + T)^2 + (sum(S) + T)^2 = 2(sum(S) + T)^2
$$

Por lo tanto, existe una partición de maestros tal que:

$$
\sum_{i=1}^{k} {\left({\sum_{x_j\in S_i}x_j}\right)}^2 \le 2(T + sum(S))^2
$$

Finalmente, SS $\le_{p}$ TA y como TA es NP también es NP-Completo.
 
# Algoritmos y complejidad
Se propusieron varios algoritmos siguiendo distintas técnicas de programación, siendo algunos de ellos óptimos y otros versiones aproximadas. Para los siguientes casos se tiene en cuenta la versión de optimización de TA.

## Backtracking

Implementamos el siguiente algoritmo:

0. Calculo una aproximación con un algoritmo greedy, que sirva como poda inicial.
1. Elijo un grupo y asigno al maestro actual a tal grupo.
2. Avanzo al siguiente maestro, con la mejor solución calculada hasta el momento (inicialmente la greedy).
    - Si la asignación actual cubre todos los maestros, devuelvo entre esta y mejor solución hasta el paso anterior, aquella con menor coeficiente.
    - Si no se terminaron de repartir los maestros pero el coeficiente actual ya supera el mejor coeficiente hasta el momento, retrocedo y vuelvo a al paso 1 con          otro grupo.
3. Si llegué hasta acá, ya se evaluó todas las asignaciones posible para el maestro actual, devuelvo la mejor.

```python
def backtracking(maestros, k):
    solucion_greedy = aprox_pakku(maestros, k)  # Solucion aproximada
    suma_greedy = obtener_suma(solucion_greedy)
    solucion = backtracking_rec(maestros, [[] for _ in range(k)], 0, solucion_greedy, suma_greedy)
    return solucion

def backtracking_rec(maestros, grupos, m, solucion_anterior, suma_anterior):
    if m == len(maestros):  # Se le asigno grupo a todos los maestros
        suma_actual = obtener_suma(grupos)
        if suma_actual < suma_anterior:
            return deepcopy(grupos)
        return solucion_anterior
    
    if obtener_suma(grupos) >= suma_anterior: 
        # No se termino de asignar grupo a todos los maestros pero la suma ya es mayor al optimo actual
        return solucion_anterior
    
    optimo_actual = solucion_anterior
    suma_opt = suma_anterior
    
    for grupo in grupos:
        grupo.append(maestros[m])
        optimo_actual = backtracking_rec(maestros, grupos, m + 1, optimo_actual, suma_opt)
        suma_opt = obtener_suma(optimo_actual)
        grupo.pop()

    return optimo_actual
```

## Programación Lineal
Se plantean dos modelos distintos y se utiliza la librería _pulp_ de Python para ejecutarlos. El código de ambos se encuentra en _pl.py_.

### Versión óptima
En esta versión se busca resolver el problema original.
#### Constantes
+ $n$: número de maestros agua.
+ $k$: número de grupos.
+ $c_i$: poder del maestro $i$ (valores positivos).

#### Definición de variables
+ $X_{ij}$: variable booleana, "maestro $i$ en el grupo $j$"
+ $Y_{ijw}$: variable booleana, $X_{iw} \land X_{jw}$
+ $S_i$: cuadrado de la suma de poder de los maestros del grupo $i$.

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

### Versión aproximada
A diferencia del caso anterior,esta versión modela una versión aproximada del problema, en cual se busca minimizar la diferencia del grupo con la mayor suma, y el grupo con la menor suma.

#### Definición de variables
+ $n$: número de maestros agua.
+ $k$: número de grupos.
+ $x_i$: poder del maestro $i$ (valores positivos).
+ $p_{ij}$: variable binaria que indica si el maestro $i$ está en el grupo $j$ ($p_{ij} = 1$) o no ($p_{ij} = 0$).
+ $S_j$: suma de poder del grupo $j$.
+ $M$: máxima suma de poder entre todos los grupos.
+ $m$: mínima suma de poder entre todos los grupos.

#### Restricciones
+ Cada maestro debe estar asignado exactamente a un grupo:
+ 
$$
\sum_{j=1}^{k} p_{ij} = 1 \quad \forall i \in \{1, 2, \ldots, n\}
$$

+ La suma de poder del grupo $j$ debe ser igual a la suma de las poder de los maestros asignados a ese grupo:
 
$$
S_j = \sum_{i=1}^{n} p_{ij} \cdot x_i \quad \forall j \in \{1, 2, \ldots, k\}
$$

+ Máxima y mínima suma de poder:

$$
S_j \leq M \quad \forall j \in \{1, 2, \ldots, k\}
$$

$$
S_j \geq m \quad \forall j \in \{1, 2, \ldots, k\}
$$

#### Función objetivo

$$
\min: M - m
$$

#### Análisis de complejidad
Para resolver el problema se utiliza el método Simplex, que es un algoritmo utilizado en problemas de Programación Lineal (PL). Este método es eficiente para encontrar soluciones óptimas en problemas de PL cuando las restricciones y la función objetivo son lineales y las variables pueden tomar valores reales.

Sin embargo, en este caso específico, algunas de las variables son binarias y pueden tomar únicamente los valores 0 o 1. Debido a la presencia de las mismas, el problema se clasifica como un problema de Programación Lineal Entera (PLE). 

La complejidad de resolver un problema de PLE utilizando el algoritmo _branch-and-bound_ es, en el peor de los casos, exponencial en función del número de variables binarias. Por lo tanto, es $\mathcal{O}(2^{nk})$ lo cual implica que a medida que el número de variables binarias aumenta (mayor cantidad de maestros y/o grupos), el tiempo de cómputo necesario para resolver el problema crece exponencialmente.

## Algoritmos Greedy

### Aproximación de Pakku

Pakku propone el siguiente algoritmo greedy:
+ Genero los $k$ grupos vacios. $\mathcal{O}(k)$
+ Ordeno los maestros de mayor a menor según su habilidad. $\mathcal{O}(n\log n)$
+ Por cada maestro obtengo el grupo con menor cuadrado de la suma (en $\mathcal{O}(n)$ ) y lo agrego a este. $n\mathcal{O}(n) = \mathcal{O}(n^2)$

Complejidad temporal: $\mathcal{O}(k) + \mathcal{O}(n\log n) + \mathcal{O}(n^2) = \mathcal{O}(n^2 + k)$
en función de los datos de entrada.

Este no es un algoritmo óptimo, pues un contraejemplo es el siguiente:

#### Codigo
```python
def aprox_pakku(maestros, k):
    """Algoritmo greedy propuesto en el enunciado."""
    # Formo los k grupos vacios
    grupos = []
    for _ in range(k):
        grupos.append([])

    # Ordeno los maestros por poder de forma decreciente
    maestros.sort(reverse = True, key = lambda m: m[PODER])

    for maestro in maestros:
        # Agrego el maestro al grupo de menor suma
        grupo = min(grupos, key=cuadrado_suma_grupo) # O(n)
        grupo.append(maestro)

    return grupos 
```

### Algoritmo propuesto por el grupo

Aprovechando la idea de que el algoritmo en su mejor caso logra repartir los maestros de forma completamente equitativa, tal que cada grupo tenga $\frac{1}{k} \sum x_i$ poder acumulado, proponemos el siguiente algoritmo:

+ Obtenemos el numero $p = \frac{1}{k} \sum_{1\le i \le n} x_i$ en $\mathcal{O}(n)$.
+ Ordenamos los maestros de mayor a menor según su habilidad.  $\mathcal{O}(n\log n)$
+ Por cada maestro, lo meto en un mismo grupo hasta que se pase de $p$, pasando a un nuevo grupo en tal caso. $\mathcal{O}(n)$

Complejidad temporal: $\mathcal{O}(n) + \mathcal{O}(n\log n) + \mathcal{O}(n) = \mathcal{O}(n\log n)$ en función de los datos de entrada.

Este no se trata de un algoritmo óptimo, tal como observamos en el siguiente contraejemplo:

#### Codigo
```python
def aprox_propia(maestros, k):
    """Algoritmo greedy propuesto por nosotros"""
    grupos = []
    nuevo_grupo = []
    poder_acumulado = 0
    limite_poder = sum([i[PODER] for i in maestros]) / k

    # Ordeno los maestros por poder de forma decreciente
    maestros.sort(reverse=True, key = lambda m: m[PODER])

    for maestro in maestros:
        if poder_acumulado > limite_poder:
            grupos.append(nuevo_grupo)
            nuevo_grupo = []
            poder_acumulado = 0

        nuevo_grupo.append(maestro)
        poder_acumulado += maestro[PODER]
    
    grupos.append(nuevo_grupo)

    return grupos
```

# Casos de prueba


# Mediciones


# Conclusiones
- El problema de la Tribu del Agua efectivamente está en NP y es NP-Completo.

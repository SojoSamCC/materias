![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

![alt text](image-3.png)

# Orden de elección

1. BFS o DFS si no hay pesos en las aristas.
2. Dijkstra
3. Bellman-Ford
4. Floyd.


![alt text](image-4.png)

DFS me dice si hay ciclos pues es capaz de detectar backedges. Si el DFS no encontró ciclos, entonces tenemos un DAG.

![alt text](image-5.png)

1. No, puede haber ciclo.
2. 
3. Sí. No es único, ejemplo dos nodos sin aristas.
4. (n*(n-1))/2. porque cada nodo puede tener a lo sumo n nodos y cada uno de sus hijos n-1, y luego n-2, ...

![alt text](image-6.png)

![alt text](image-7.png)

La cosa es: 
 1. Elijo un nodo que tenga grado de entrada cero.
 2. Remuevo las aristas que salen de ese nodo.
 3. Repetir.

![alt text](image-8.png)

# Ejercicios

![alt text](image-9.png)

```
Se me ocurren dos maneras de resolverlo:
1. Multiplico p * t para cada arista y luego hago dijkstra sobre eso.
2. Hacer Dijkstra pero solo fijandome en p, luego Dijkstra sobre t y me quedo con la intersección de esos DAGs, si en algún momento me quedan aristas sueltas que no son de la intersección entonces priorizo usar las aristas de del subgrafo t.
```

![alt text](image-10.png)

![alt text](image-11.png)

![alt text](image-12.png)

![alt text](image-13.png)

Existen $n\times t$ nodos y $m\times t$ aristas. En ambos casos es $O(N^2)$ porque $t\in O(n)$

Es mejor hacer lo del nodo fantasma porque si hacemos lo de ver el mínimo de los Kazan entonces eso me suma una complejidad de O(n*t) lo cual es innecesario si simplemente agregamos el nodo fantasma conectado a cada Kazan con aristas de peso 0.

![alt text](image-14.png)

No hay ciclos porque el t siempre crece, entonces no puede pasar que haya una arista que me conecte con t menor o igual.

> Complejidad Dijkstra: O(m log n)

# Notas
1. Un árbol no tiene porqué ser dirigido.
2. El DAG me va a dar el camino mínimo entre todos los caminos minimos posibles. El árbol me da UN camino mínimo para todo par de nodos.


![alt text](image-15.png)

![alt text](image-16.png)

Aprovechando que es un DAG queremos calcular el camino mínimo usando programación dinámica.

![alt text](image-17.png)

La complejidad es O(n x t) + O(m x t) porque cada nodo lo revisamos una vez y cada arista la revisamos una sola vez.

$$
\sum_{v_t en G_t}{d_out (v_t)} = m\times t
$$

# MORALEJA: el camino mínimo en un DAG lo puedo calcular en tiempo lineal. Es válido usar libremente en el parcial esa frase.

![alt text](image-18.png)

![alt text](image-19.png)

![alt text](image-20.png)

![alt text](image-21.png)

# Ejercicio: Rayuela Rectangular

![alt text](image-22.png)

![alt text](image-23.png)

![alt text](image-24.png)

![alt text](image-25.png)

![alt text](image-26.png)

![alt text](image-27.png)

Es un DAG porque solo hay aristas que me conectan con casilleros que son mayores o iguales al que estoy, entonces no es posible que haya una arista que me devuelva a un nodo menor.

![alt text](image-28.png)

![alt text](image-29.png)

# MORALEJA FINAL: si el grafo es un DAG entonces camino mínimo, máximo sale en complejidad lineal y no hay que justificar!

# Camino mínimo todos a todos

![alt text](image-30.png)

![alt text](image-31.png)

Si yo sé que mi m es chiquito o más o menos como n entonces es mejor correr Dijkstra desde cada nodo porque me queda en $O(n^2 log n)$ que es mejor que $O(n^3)$. Pero solo puedo usar Dijkstra desde cada nodo si no hay aristas negativas ni ciclos negativos.

> Moraleja: Bellman-Ford no es muy útil para calcular el camino mínimo de todos a todos. Dijkstra PUEDE llegar a ser útil.

> MORALEJA JOHNSON: si queremos correr Dijkstra desde cada nodo, entonces mejor hacer Johnson que tiene la misma complejidad (y hace lo mismo que Dijkstra) pero cumpliendo únicamente la condición de que no hay ciclos negativos. Johnson se las arregla para sacar las aristas negativas. 

> Para Johnson solo hay que recordar que me resuelve el camino mínimo todos a todos en complejidad O(nm log n) si no hay ciclos negativos. Lo usamos como caja negra. Conviene usarlo solo si m no es muy grande con respecto a n.

# Invariantes

- **Floyd:** en la iteración k tenemos el camino mínimo de todos a todos usando como nodos intermedios los primeros k nodos.
- **Dantzig:** en la iteración k tenemos el camino mínimo de todos a todos usando los primeros k nodos.

![alt text](image-32.png)

![alt text](image-33.png)

![alt text](image-34.png)

```
Se me ocurre modelar esto como un grafo donde cada nodo es un acorde y hay una arista entre cada nodo con peso igual al tiempo que le toma a rasta pasar de un acorde a otro. Luego lo que hago es ejecutar Dantzig y le digo a Rasta que toque los acordes que van desde el primero hasta el último siguiendo los nodos de la secuencia que contiene el nodo "más rápido de tocar" si se parte desde el nodo en el que estoy parado. Difícil de explicar pero es simplemente que luego de tener DAntzig me armo el camino de los acordes haciendo recorriendo la matriz a partir de un nodo a otro pero solo si el nodo al que voy es el que me toma menos tiempo entre los demás nodos vecinos (medio recursivo eso).
```

![alt text](image-35.png)

![alt text](image-36.png)

![alt text](image-37.png)

No usamos Johnson porque el grafo es completo y m se hace muy grande.

![alt text](image-38.png)

```
Se me ocurre que a partir de la secuencia anterior, entonces ver cuál es el acorde en la secuencia de acordes input que me minimiza el pasaje entre los acordes.
```

![alt text](image-39.png)

Ese delta es el lo mismo que la función que me dice el tiempo de una arista a otra.


> En el parcial debemos justificar lo más formal posible esa desigualdad triangular.

![alt text](image-40.png)

![alt text](image-41.png)

![alt text](image-42.png)

![alt text](image-43.png)

![alt text](image-44.png)

![alt text](image-45.png)

E1 es mejor también cuando m es chiquito y Q también.

# Posible ayuda para el taller:

Podemos hacer un if que dependiendo del tamaño del input haga un algoritmo u otro.

# Notas
- aristas s-t eficientes son las aristas que pertenecen a un camino mínimo entre s y t. Definición formal: dist(u, v) + costo(v, w) + dist(w, z) = dist(u, z). dist(u, v) = Dijkstra desde u; dist(w, z) es Dijkstra desde z en el grafo transpuesto; costo(v, w) es dato.
- $O(n\times m) + O(m\times n) \leq O(n^2)$
- Complejidad de una dinámica es la cantidad de estados posibles.
- Grafo denso: muchas aristas, aprox O(n^2).
- Grafo Ralo: pocas aristas, aprox O(n).
- No hay una definición estricta entre lo que es un grafo denso o un grafo ralo.
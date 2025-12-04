# Clase de repaso post segundo parcial (resuelven el segundo parcial porque no aprobó ni el 20% aún bajando el puntaje mínimo de aprobación)

---

# Mi parcial

[INSERTAR FOTO]

---

# Notas

# Ejercicio 1
I
el B

II
el D. BFS me da un ciclo pero no sabemos cuál.

III
el C.

IV
4 o más.

# Ejercicio 2

Generalmente las demostraciones son constructivas y no van a haber una serie de pasos definida para poder demostrar. Sin embargo no dejan de ser matemáticamente rigurosa.

Idea del algoritmo: saco a v y w del grafo, corro DFS o BFS para hallar componentes conexas en el grafo. Luego agrego a v y w en lo que me quedó, me fijo los nodos que se conectan con v y que están en diferentes compoenentes conexas, luego lo mismo para w y me fijo se logré conectar las dos componentes conexas.

Idea pura: encontrar un camino de v a una componente, un camino de la componente a w, un camino de w a OTRA componente, y finalmente un camino desde la otra componente a la primera componente.

No salía con punto de articulación porque complicaba mucho. Igual no anda, [poner contraejemplo que tengo el celu.]

En este caso también salía corriendo DFS desde v y me fijo si hay un hijo de w que me conecta con v (una backedge). En este caso este algoritmo funciona (hay que justificar un poco por qué, **tarea**).

> Nota: el contraejemplo de que no funciona en cualquiera lo tengo en el celu.
>
> [Poner foto]

# Ejercicio 3

> Nota: este fue un quilombo.

## Solución fácil (sí, así lo dijeron):

> Tiraron que era la misma idea que el ejercicio de las habitaciones.

Es un grafo de estados. En cada nodo tengo el numero del puesto y un conjunto de comidas compradas: tengo 2^k nodos por cada comida porque por cada puesto tengo 2^n combinaciones de comidas compradas

>> Ejemplito: (puesto1, [0, 1, 0, 1]) -> ... -> (puestoN, [1, 1 , 1, 1]). 0 si no tengo esa comida y 1 si sí la tengo.

> Lo de las dos personas viene el post-procesamiento.

Pongo una arista entre un estado y otro si tengo un puesto como ``(i, c) -> S_{i, j} -> (j, c')`` ```C in C' C' - C = Comidas que me vende el puesto`` ``S_{i, j} es el tiempo que me tarda en ir de un puesto a otro.``` O sea, pongo una arista entre un puesto y otro si TODAS las comidas del puesto al que voy están en el conjunto de comidas que me faltan. ```c`` es la cantidad de comidas que compré hasta el puesto i.

Luego se corre Dijkstra desde el nodo origen minimizando por el tiempo que tarda de ir de un nodo a otro.

Para poder armar la respuesta con las dos personas lo que se hace es. 

1. Me paro en la hilera del último puesto. Voy a tener 2^k combinaciones de comidas compradas.
2. Buscar entre todos los estados de comidas compradas de esa hilera dos estados de comidas que al ser unidos como conjunto me de todas las comidas ``Ejemplo: [1, 0, 0] + [0, 1, 1] = [1, 1, 1] ; Otro: [1, 1, 0] + [1, 0, 1] = [1, 1, 1]``. Hacer esto con cada par posible.
3. Quedarme con el máximo tiempo entre ese par y minimizar el tiempo global comparando entre todos los tiempos minimos encontrados.

> Complejidad de lo último: O(k*(2^k)^2). Multiplicas por k porque la comparación entre unir los dos conjuntos es lineal en la cantidad de comidas. 2^k porque hay 2^k estados por comparar. 2^k está al cuadrado porque hay que realizar la comparación entre todos los estados que tenemos, eso es cuadrático.

Sabemos que el tiempo es mínimo en el estado del nodo final porque corrimos Dijkstra desde el nodo inicial.

## Solución un poco más difícil:

La idea es la misma que la anterior PERO ahora no compramos todas las comidas, agrego nodos de modo tal de: compro una comida, compro la otra, compro una y luego compro la que me faltó, no compro ninguna (eso me agrega k aristas por cada nodo). Luego cuando llegamos al final solo me hace falta comparar entre pares que sean "complementarios" ``Ejemplo: [1, 0, 1] + [0, 1, 0] = [1, 1, 1]``

```
Ejemplo:

(i, c) {pollo, papa}
| |  |________________________
| |____________              |
|             |              |
(i, c+pollo)  (i, c+papa)    (i, c)
|              |             |
(i, c+pollo+papa)            |
|                            |
|                            |
otra puesto__________________|

Todas las aristas tienen peso 0 porque estoy en el mismo puesto.
```

Hacer esto me garantiza que tardo menos o lo mismo que la idea anterior porque no me estoy moviendo entre un puesto y otro, sino que me quedo en el mismo.

Esto optimiza el post procesado porque solo tengo que comparar entre conjuntos complementarios y eso es lineal.

# Ejercicio 4

## a)

El modelado es (idea):
```
s -> capa equipos (1) -> capa equipos a los que se les transfirió (2) -> t
```

Entonces un equipo en (1) se conecta con todos los equipos en la capa (2) si le transfiere puntos a ese equipo OJO, metemos la conexión a través de un nodo intermedio que indique que le transferimos al nodo en la capa (2) transfiriendo primero los puntos a los otros equipos.

La restricción k+1 **ES** necesaria porque si metemos infinito entonces el flujo máximo es: nadie redistribuye su flujo y eso no necesariamente significa que obtengamos que haya un flujo que supere al de ¬Echu.



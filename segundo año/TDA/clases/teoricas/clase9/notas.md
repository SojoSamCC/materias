# Flujo máximo

Hay muchos problemas que se resuelben con flujo máximo. Uno que está bueno es el de matchinf máximo.

![alt text](image.png)

La función capacidad es la que me dice la cantidad máxima de flujo que acepta esa arista.

La cantidad X_ij debe cumplir que no se pasa de la capacidad del arco.

![alt text](image-2.png)
![alt text](image-1.png)

El de la izquierda es la capacidad y el de la derecha es la cantidad de unidades de flujo que enviamos por esa arista. Es ejemplo no es de flujo máximo.

![alt text](image-3.png)

Un corte me divide en dos subconjuntos, en uno esta s y en el otro está t.

El corte es importante porque me indica conceptualmente que si tengo dos regiones y si lo que sale de una no es todo lo que le llega a la otra, entonces en algún lado se está acumulando el flujo y no es lo que buscamos (mandar todo el flujo posible sin acumularlo en un luegar diferente de t).

Esa sumatoria es importante pues es la formalización de la idea de arriba.

Demo
![alt text](image-4.png)
![alt text](image-5.png)

![alt text](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)


![alt text](image-9.png)

La capacidad de un corte es la suma de las capacidades de las aristas que envían flujo. Eso no implica que el flujo máximo es la capacidad del corte porque no necesariamente vamos a estar enviando todo el flujo posible por cada arista con capacidad, podemos tener aristas que me limitan el flujo que puedo enviar.

![alt text](image-10.png)
![alt text](image-11.png)
![alt text](image-12.png)

![alt text](image-13.png)
![alt text](image-14.png)

![alt text](image-15.png)

Aumentar un flujo es enviar más flujo por arcos que no están saturados ó devolviendo flujo por un arco que ya estamos usando.

![alt text](image-16.png)
![alt text](image-17.png)

Idea: siempre que haya un camino residual, podemos aumentar el flujo.

![alt text](image-18.png)
![alt text](image-19.png)

![alt text](image-20.png)

La proposición es: los caminos de aumento me aumentan el flujo en la red original. Lo aumenta según $\Delta$ P.

Si no hay un camino de aumento s a t en la red residual, entoces el flujo ya es máximo.

En el corte mínimo, la capacidad es igual al corte mínimo.

![alt text](image-21.png)

![alt text](image-22.png)

A Ford Fulkerson no le importa cómo encuentras un camino de s a t en la red residual.

[Ver diapos 41-53]

![alt text](image-23.png)

U es la capacidad máxima del grafo original.

![alt text](image-24.png)

![alt text](image-25.png)

Edmonds y Karp es literalmente el mismo algoritmo de Ford y Fulkerson pero especificando que debemos usar BFS para encontrar el camino de aumento.

![alt text](image-26.png)
![alt text](image-27.png)

El problema del matching máximo QUE VEMOS EN LA MATERIA solo se hace de a pares, o sea entre dos conjuntos.


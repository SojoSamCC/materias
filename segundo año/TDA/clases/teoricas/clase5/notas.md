# Árboles generadores mínimos

Un árbol generados (AG): de un grafo G es un subgrafo generados (que tiene el mismo conjunto de vértices) de G que es árbol.

![alt text](image.png)

![alt text](image-1.png)

La longitud de un árbol es la suma de todos los pesos de todas las aristas que lo conforman.

El árbol generador mínimo es el árbol generador que tiene longitud mínima.

![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)

## Algoritmo de Prim

![alt text](image-5.png)

El algoritmo de Prim ta bueno, comienza desde un nodo y se va por la arista de menor peso que sale de él, y así con todos los nodos que va recorriendo, siempre y cuando no llegue a un nodo que ya había visitado.

![alt text](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)

![alt text](image-9.png)
![alt text](image-10.png)
![alt text](image-11.png)
![alt text](image-12.png)
![alt text](image-14.png)

## Algoritmo de Kruskal

![alt text](image-13.png)
![alt text](image-15.png)
![alt text](image-16.png)
![alt text](image-17.png)

En la implementación de Kruskal se evitan elegir aristas "malas", entonces lo que se hace es solo usar aristas que no me conecten nodos del mismo conjunto.

![alt text](image-18.png)

Un bosque es un conjunto de árboles. No es conexo el bosque (al menos hasta que haya terminado la ejecución del algoritmo).

![alt text](image-19.png)

todas las e' son las aristas que agrega kruskal.

![alt text](image-20.png)
![alt text](image-21.png)


La altura del árbol es $\frac{n}{2}$
La raíz está a altura 1
El largo del array es $2^{altura del árbol}-1$
En el medio de cada rama **SIEMPRE** voy a tener un 0 o un 1 y no voy a tener que hacer recursión de ese lado.
La cantidad de elementos a la izquierda o derecha es $2^{altura_del_arbol_de_recursion-1} - 1$

Algunos casos de test:

6 3 6 -> 3
9 2 5 -> 2
9 5 7 -> 2
9 4 11 -> 5
32 1 2 -> 1
32 1 12 -> 6
32 1 21 -> 11
32 3 27 -> 13
32 1 32 -> 16
32 5 40 -> 18
32 2 8 -> 3
32 4 12 -> 4
32 8 20 -> 6
32 20 28 -> 4
32 20 36 -> 8
27 1 31 -> 17
27 5 26 -> 20
27 11 26 -> 14
27 9 12 -> 3
27 9 28 -> 17
27 16 28 -> 11
27 24 28 -> 4
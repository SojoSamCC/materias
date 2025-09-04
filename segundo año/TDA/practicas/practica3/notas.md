# Programación dinámica Top Down

# Ejercicio

![alt text](image.png)

Es fibonacci

![alt text](image-1.png)

Notar que sale $\floor{\frac{n}{2}}$ porque la rama más larga es la que está todo a la derecha, 
notar que la más larga es la que está todo a la izquierda

Usan notación $\Omega$ porque la función tiene **como mínimo** esa cantidad de llamados.

La cantidad de estados posibles A NIVEL MATEMÁTICO es $O(n)$ porque solo cuentas las $f(i)$ que son distintas.

# ¿Cuánto cuesta a nivel computacional? 
> Nota, así es como se justifica esto.

La cantidad de estados es n porque siempre llamamos al estado anterior sin repetirlo después en ningún otro llamado recursivo, por lo tanto la complejidad de cantidad de llamados es O(n), hacer un llamado cuesta O(1) porque solo hacemos operaciones elementales. Finalmente la complejidad computacional es O(n).

# ¿Y a nivel espacial?
Cuesta O(n) porque tenemos un array de tamaño n (pues solo hay n llamados recursivos a los cuales guardar).

# Ejercicio 2

![alt text](image-2.png)

Este estaba en la guía del cuatri pasado, recuerdo haberlo resuelto.

Aprovechar esa propiedad de una solución óptima. Si al final me quedó un asteroide es porque me convenía venderlo antes o bien no comprarlo.

![alt text](image-3.png)

1. Necesitamos la cantidad de asteroides y días disponibles. El llamado que resuelve nuestro problema es $mgn (0,n)$
    1. Estar en el día 0. Más asterorides que días, no podemos vender un asteroide que no teníamos.
2. 
![alt text](image-4.png)

## Función recursiva

$$
maximaGanancia(asteroidoes, dias) = \begin{cases}
-\infty \text{ , si } a<0 \\
-\infty \text{ , si } a>d \\
-\infty \text{ , si } d=0 \text{ y } a<0 \\
0 \quad \ \ \text{ , si } d=0 \\
max(maximaGanancia(asteroide, d-1), \\ \quad \quad \ \ max(maximaGanancia(a+1,d-1) + p_{d}, \\ \quad \quad \quad \quad \quad maximaGanancia(a-1,d-1))) \quad \quad \text{ , caso contrario}
\end{cases}
$$

Una más cheta

$$
maximaGanancia(asteroidoes, dias) = \begin{cases}
-\infty \text{ , si } a<0 \text{ o } a>0 \\
0 \quad \ \ \text{ , si } d=0 \\
max(maximaGanancia(asteroide, d-1), \\ \quad \quad \ \ maximaGanancia(a+1,d-1) + p_{d}, \\ \quad \quad \ \ maximaGanancia(a-1,d-1)) \quad \quad \text{ , caso contrario}
\end{cases}
$$

## Como guardamos memoria?

Usamos una matriz de n*n para guardarnos el estado de estar en un día particular con una cantidad de asteroides en particular. En todas las posiciones se encuentra la máxima ganancia posible de estar en un día en particular con una cantidad de asteroides dada.

En el ejemplo usaron matriz de n+1*n+1 por el tema de los índices.

## Complejidad espacial
Es O(n*n) porque la matriz tiene esas dimensiones Y porque lo que guardamos en la matriz tiene complejidad espacial O(1)

## Complejidad computacional
- Hacer cada llamado recursivo cuesta O(1).
- Cada llamado en sí me sale O(n) y hay n llamados. Por lo tanto la complejidad es O(n*n)

Notar que en cada llamado si compro entonces no puedo volver a comprar y por lo tanto solo puedo vender o no hacer nada, viendo el árbol, entonces me queda un árbol binario de altura n porque siempre reduzco a n de a uno. Finalmente la cantidad **mínima** de llamados es dos.

## Dem
![alt text](image-5.png)

La segunda sumatoria evita que mi cantidad de asteroides sea negativa.

# ¿Cuándo es mejor programación dinámica?



# ¿Qué hacemos para poder implementarla?

1. Nos armamos nuestra función recursiva. La matemática.
2. Nos empezamos a guardar los estados de cada llamado recursivo.
3. Usamos esa memoria de los estados anteriores para resolver los estados que se superponen con alguno que ya vimos.


# Ejercicio 3
En el primer día puede descansar o competir, el segundo día tiene tres opciones disponibles. 
No puede repetir competir o gimnasio dos días seguidos.
Pepi quiere descansar lo menos posible.




# Superposicion de problemas
Quiero comparar la cantidad de estados comparado con la cantidad de llamados recursivos.

# Notas
- A los profes les gusta que usemos matrices para guardarnos la data.
- Conviene mucho pasar la memorización por referencia.
- Complejidad en backtrackinf se justifica con el árbol de recursión.
- Cuando hacemos inducción tenemos que indicar sobre qué parámetros hacemos inducción.
- Nos puede pasar que tengamos que hacer inducción sobre más de un parámetro.          
- Leer segundo año\TDA\practicas\practica3\Clase Ori dp top-down.pdf está **muy buena**.
- Si busco un mínimo el neutro de la operación es +inf, si busco un máximo, entonces es -inf.
- "caso base es cuando la respuesa es trivial".
- La memoria la inicializamos, la verificamos (vemos si teníamos una solución), y la actualizamos! Solo eso. Son tres pasos.
- Cuando cant estados es << cant de llamados recursivos, entonces tenemos superposición de problemas!!! Para poder justificar al cant de llamados usamos notación $\Omega$.
- Cant estados + Complejidad de cada estado = Complejidad.
- Los subíndices en la función recursiva son como las variables globales.
- Por cada parámetro que tengo me aumenta en uno la dimensión del tamaño del problema. Cuantos menos parámetros tengo entonces me mejora la complejidad espacial y temporal!!! Pensar que si una variable puede tener 200 estados posibles, si yo la saco entonces mi programa corre 200 veces más rápido omg. 
- Si cada parámetro tiene n posibilidades y tengo 5 parámetros, entonces tengo $n^5$ combinaciones de estados.
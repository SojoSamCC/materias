# Repaso primer parcial

## Notas sobre los ejercicios que nos pueden tomar por técnica

- Seguramente en Greedy nos tomen algo de demostración.
- Confirmado que si nos toman la implementación de un greedy entonces no va a ser un greedy que sea una implementación demasiado loca de sacar/implementar.
- Van a haber ejercicios que no sean atómicos. O sea, que un ejercicio no dependa de otro ejercicio. Ejemplo: el inciso (b) depende del (a).
- A un profe se le salió que el de backtracking va a ser de DFS, seguramente.
- No nos van a pedir que probemos que estamos demostrando correctamente la demostración (o sea la invalidez de la demostración).
- No nos van a pedir demostrar una poda en backtracking.

# Multiple Choice
![alt text](image.png)
![alt text](image-1.png)

![alt text](image-2.png)
![alt text](image-3.png)

![alt text](image-4.png)
![alt text](image-5.png)

![alt text](image-6.png)
![alt text](image-7.png)

# Maximin D&C

![alt text](image-8.png)
![alt text](image-9.png)
![alt text](image-10.png)
![alt text](image-11.png)
![alt text](image-12.png)

Los profes **no** nos van a pedir más justificación que esta.

Tampoco nos van a tomar algo como lo que está en el último cuadrito.

# Viaje a Mar del Plata.

![alt text](image-13.png)
![alt text](image-14.png)
![alt text](image-15.png)
![alt text](image-16.png)
![alt text](image-17.png)

Nuestros algoritmos SIEMPRE deben estar escritos en un pseudocódigo o en algún lenguaje de programación. **NO** se vale escribirlo en palabras.

**NO** podemos asumir cosas que no nos dijeron que asumamos, o sea, si pasa algo como que una entrada es no válida o que no pueda suceder nunca, entonces nuestra función debe retornar algo como "no hay solución" y listo.

![alt text](image-18.png)

No hace falta colocar esta iteración en el parcial. Aunque tampoco está mal.

![alt text](image-19.png)
![alt text](image-20.png)

Para la demo no siempre va a pasar que usemos lemas. Eso es para que quede más lindo. Muchas veces nos va a pasar que escribamos lo mismo varias veces.

![alt text](image-21.png)

En nuestra suposición de la solución $O$ asumiremos que $O_i$ lo que significa que todo el conjunto de soluciones de la óptima hasta la posición i tiene exactamente los mismos elementos de la greedy. Luego nos fijamos que pase que en $O_{i+1}$ sea igual a la Greedy en la misma posición (i+1).

Al hacer demostración por inducción **hay** que aclarar en qué parámetro vamos a hacer inducción, en este caso vamos a hacer inducción sobre la cantidad de elementos de $O$ que coinciden con la Greedy. O sea, vamos a hacer inducción en los $i$ elementos de la $O$ para llegar a que $i = k$

![alt text](image-23.png)

```
DEMOSTRACIÓN:

Caso base:
    Quiero probar que existe una solución óptima que tiene a la primera elección Greedy.

    Se demuestra usando Lema 1.
```

![alt text](image-24.png)

Decimos que hasta $O_{i}$ son los mismos elementos que la greedy y queremos ver que pase que $O_{i+1}$ sea igual a la Greedy en la misma posición (i+1).

# Ruta Mínima

![alt text](image-25.png)

Es un ejercicio de la guía.

$\pi$ es una función que me devuelve al mismo valor.

Ese $D_{\pi(n)\pi(1)}$ lo que quiere decir es $D[n][1]$

Como es permutación significa que necesito un solo elemento por fila y un solo elemento por columna.

Lo que me piden es ver todas las permutaciones de pi y quedarme con la que minimice eso.

Eso es como tomar cada permutación e ir probando a a ver cuál es la mejor solución.

![alt text](image-26.png)

- Las soluciones candidatas son todas las permutaciones posibles con $\pi = \{1, \ ...,\ n\}$
- Solución válida vs solución candidata: la válida es una solución que parcialmente es correcta porque cumple todas las restricciones, las candidatas son todas aquellas que se puedan probar y que no necesariamente cumplen todas las restricciones. O sea, las válidas son aquellas que no deben ser podadas.
- Lo que necesitamos es una permutación donde no hayan repetidos.
- Ese + significa "concatenar".

![alt text](image-27.png)

La cantidad de estados es:

$$
\sum_{i=0}^{n} \frac{n!}{i!} = n! \sum_{i=0}^{n} \frac{1}{i!}
$$

---

Esta formula apareció en el pizarrón y no presté atención cuando la escribieron, buscar lógica.

$$
\frac{n!}{k!} = \sum_{i=k+1}^{n} i
$$

Porque cada nivel del árbol tiene $\frac{n!}{(nivel_\ arbol_\ actual)!}$

y es tiene orden $\leq O(n!)$

La poda es ir acumulando la suma de la matriz en la posición parcial y en caso de que se pase de la suma que ya tenía guardada, entonces podo esa rama.

# Pila Cauta

![alt text](image-28.png)
![alt text](image-29.png)

![alt text](image-30.png)

Esto es bien fuerza bruta, no hay poda ni nada de memorización.

La complejidad es $O(2^n)$ porque para cada caja tengo el que evaluar el caso de la pongo o no la pongo.

![alt text](image-31.png)
![alt text](image-32.png)

Ese $W$ que aparece ahí es una cota MUY ajustada del $W$ que más conviene, también se valía colocar algo como $W = \infty$ y nos ahorrabamos el problema de esa cota tan ajustada.

Ese $W$ es básicamente el peso lo más alto posible tal que con las combinaciones de las cajas y soportes disponibles NUNCA supere ese $W$, es el más ajustado.

## Notas ayuda
- En DP nuestras demos son: che, tamos viendo todas las posibles instancias.
- En Greedy nuestras demos son: che, esta solución nos asegura que llegamos a algo óptimo.
- No hace falta demostrar que una solución óptima es óptima.
- En dinámica **es** clave en muchos poder olvidarse todo lo posible del pasado. O sea, olvidarme de todos los estados anteriores posibles.
- La complejidad de una DP suele ser siempre la cantidad de estados posibles, algo así como el producto de la cota máxima de los argumentos que toma la función para cada argumento.
- Para demostrar superposición de problemas si tenemos que realizar comparación entre dos notaciones asintóticas y una tiene parámetros que la otra no tiene, entonces no podemos demostrar que hay superposición de primeras porque depende mucho de los parámetros que tengamos y sus propiedad, si no tiene restricción ese parámetro en cuestión entonces sí es verdad que no hay manera de demostrar la superposición. Caso contrario hay que comparar la notación $\Omega$ de la solución con Backtracking o fuerza bruta con la notación asintótica $O$ de la solución de programación dinámica. **Moraleja: FB V BT ($\Omega$) vs PD ($O$). Si $\Omega\gt O \implies \text{ Hay superposición de problemas.}$**.
- Complejidad temporal es cantidad de estados * cantidad de trasiciones, en el ejemplo de Pila Cauta la cantidad de transiciones es 2.
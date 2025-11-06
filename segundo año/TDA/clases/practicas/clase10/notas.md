# Flujo máximo

> Es importante demostrar correctamente flujo en el parcial.

> Todo lo que vemos en esta clase aparece mucho en la vida real.

Tenemos un grafo y dos nodos distinguidos s y t en el grafo. y una función de capacidad para cada arista del grafo.

# ¿Cómo demostrar en flujo?

Para probar que es óptimo hay que usar el teorema. Para probar que es factible usamos el sí y solo sí. Es más fácil probar la vuelta que la ida.

> La vuelta es: defino Flujo F (con su función) y quiero demostrar que el flujo que viaja por esa red de flujo es válido y que es máximo porque es el corte mínimo de la red (ahí usamos el teorema max flow - min cut).

> 

El corte mínimo es el flujo máximo de una red. El teorema es poderoso. Meterle ojo a la teórica.

# Ejercicios

![alt text](image.png)

O sea basicamente queremos ver todos los caminos de un nodo A a otro nodo C sin repetir aristas en el camino.

```
modelado:
Los nodos son las esquinas de la ciudad y las aristas las calles que conectan a cada esquina. La capacidad de flujo de cada arista es 1.
```

Podríamos hacer algo como busco un camino de A a C en el grafo y lo elimino y vuelvo ha buscar otro... FF hace eso mismo pero más limpio.

La justificación de que el algoritmo anda es que si hay un flujo en una arista es porque llega hasta el sumidero, entonces si maximizamos el flujo es lo mismo que encontrar la cantidad máxima de caminos diferentes en el grafo.

Para justificar la vuelta:
```
Vamos a querer definir esos F caminos disjuntos.

... Algo que no pude copiar.

Función F:

F(arista, nodo_adyacente_a_la_arista) = 
    | 1 si la conservación del nodo es 1.
    | 0 si la consercación del nodo es 0.
```

![alt text](image-1.png)

![alt text](image-2.png)

O sea, la suma del flujo de las aristas que entran a v es el mismo que la suma de las aristas que salen de v.

> Cuando estamos demostrando no nos importa mucho el algoritmo. Solo nos interesa demostra que si tenemos un flujo entonces tenemos una solución.

Para justificar el flujo máximo tenemos que encontrar el corte mínimo (por el teorema).

La idea es: Si hay una arista que sale de A que tiene 1 de flujo, entonces me basta hacer un corte con todas las aristas que salen de A y veo el flujo que me da ese corte (sabiendo que es máximo).
![alt text](image-3.png)

La idea es: asumiendo como hipótesis que mi Flujo es válido, entonces quiero ver que cada flujo que vale 1 me da un camino de A a C.

Idea de la demo: tengo un flujo de A a C entonces lo elimino porque eso significa que tenía un camino de A a C, luego con eso demuestro que eran todos caminos disjuntos.

![alt text](image-4.png)
![alt text](image-5.png)
![alt text](image-6.png)
![alt text](image-7.png)

Para la segunda pregunta: el flujo me quedaría mucho más grande y los caminos podrían aumentar.

![alt text](image-8.png)

```
Se me ocurre hacer algo como pongo a una persona en algún nodo de cada camino que hay entre A y C, si de casualidad hay un nodo que me conecta dos caminos, entonces pongo a una persona ahí y no pongo a nadie más en esos caminos.

O sea, se me ocurre poner a una persona en cada nodo que es una intercepción entre caminos de A a C y a una persona en un nodo que pertenece a un camino que no pertenece a una intercepción de un camino desde A a C.
```

Para hacer esto metemos a un persona en cada nodo perteneciente a un corte mínimo que tiene la menor cantidad de nodos. Aunque esto cuesta mucho a nivel temporal.

Cuando no nos importa una capacidad en un problema de flujo, le mandamos infinito a la capacida.

> IMPORTANTE: siempre que me pidan alguna capacidad de un nodo entonces se duplica al nodo y le ponemos una arista con su nuevo doble, la capacidad de la arista depende del problema.

# Nota:
- Siempre conviene darle una semántica a cada unidad de flujo que usamos.
- Un flujo válido es un flujo que pasa por una arista sin pasarse de su capacidad y que se conserva el flujo sobre cada nodo. 
- Demostrar eso sobre los nodos es: hablar de la conservación.
- Demostrar eso sobre las aristas es: hablar de la capacidad.

![alt text](image-9.png)

![alt text](image-10.png)

![alt text](image-11.png)

![alt text](image-12.png)

![alt text](image-13.png)

![alt text](image-14.png)

![alt text](image-15.png)

![alt text](image-16.png)

> OJO: corte mínimo no es igual a puente.

# Matching máximo

![alt text](image-17.png)

```
Se me ocurre lo siguiente:

Poner dos nodos nuevos uno s que se conecta a cada persona (que también son nodos) luego conecto a cada persona con los nodos que representan a las tareas que pueden cumplir, luego cada tarea con el sumidero t (que es nodo nuevo).

Existe una arista entre una persona y una tarea si esa persona puede realizar esa tarea. 

Todas las aristas tienen capacidad 1.

Si una arista tiene un 1 es porque esa persona va a realizar la tarea del nodo al que llega.
```
```
La demostración no la puedo hacer aún porque me falta práctica pero la idea es que es correcto porque como solo va a haber 1 de flujo si se realiza esa tarea entonces maximizar el flujo coincide con la cantidad de tareas máximas que se pueden hacer.
```
```
La cota de la complejidad (sin pensarlo mucho porque no tengo más tiempo) es O(nm^2)
```

![alt text](image-18.png)
![alt text](image-19.png)
![alt text](image-20.png)
![alt text](image-21.png)
![alt text](image-22.png)

> En general nos van a pedir en un parcial que modelemos al grafo, una justificación o demostración de que es corresto el modelado (dependiendo de la dificultad del modelado), dar un algoritmo para resolverlo y su complejidad.

![alt text](image-23.png)

![alt text](image-24.png)

```
una arista va de i a j y se nota como (i, j)
funcion(arista) = 
    | 1 si arista in Matching
    | 1 si arista es (s, i) 
    | 1 si arista es (j, t)
    | 0 cc
```

> En el parcial es probable que nos pidan una justificación y no una demostración. Si nos piden la demostración entonces hacemos como en el ejercicio anterior, sino hay que explicarlo lo más claro posible, que se note que entendemos por qué funciona.

![alt text](image-25.png)
![alt text](image-26.png)
![alt text](image-27.png)
Alguien notó que en realidad puede ser el mínimo entre T, P y T*P porque puede suceder que solo tenemos una arista que nos conecta entre los pares ij (personas con tareas).

![alt text](image-28.png)
![alt text](image-29.png)
![alt text](image-30.png)

# Enchufados

![alt text](image-31.png)
![alt text](image-32.png)

```
a) se me ocurre hacer algo como el ejercicio anterior pero ahora entre dispositivos y adaptadores. El tema es que hacerlo con eso hace que pierda información... También se me ocurre meter algo como por tres columnas: dispositivos, adaptadores, tomacorrientes; dispositivos con adaptadores (capacidad inifinito porque podemos tener muchas veces al mismo dispositivo), adaptadores con tomacorrientes (capacidad infinito), tomacorrientes sumidero (capacidad infinito).

Hay flujo 1 de un dispositivo a un adaptador si ese adapatador le sirve al dispositivo.

Minimizar la cantidad de dispositivos que se quedan sin corriente es equivalente a maximizar la cantidad de flujo.
```

![alt text](image-33.png)
![alt text](image-34.png)

![alt text](image-35.png)

![alt text](image-36.png)

Importante: esto no alcanza como justificación. Habría que explicar cosas como "representa una conexión válida mediante adaptadores", ...

![alt text](image-37.png)

> Tiraron por ahí (un ayudante) que es m*f según esta regla mnemotécnica: F es BFS; en respuesta a la pregunta "¿Por qué m x F?"

![alt text](image-38.png)


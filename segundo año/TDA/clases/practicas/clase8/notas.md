# Clase Árboles generadores mínimos

# Notas

- En el parcial pueden llegar a tomar algo con AGM y demoras, donde las demoras son aristas.

# AGM

![alt text](image.png)
![alt text](image-1.png)

# Camino MaxiMin

![alt text](image-2.png)

Es el camino que maximiza la arista mínima entre todos los caminos posibles.

El ejemplito: tenemos un ancho de banda, tenemos cables con conexión. Lo más rápido que puede ir mi conexión es el camino MaxiMin.

# Camino MiniMax

![alt text](image-3.png)

[VER LA DEMO]

# Aplicaciones

![alt text](image-4.png)

![alt text](image-5.png)

# Kruskal

![alt text](image-6.png)

Kruskal usa un heap para ordenar y usa Disjoints Sets para saber las componentes conexas del bosque que es un conjunto de subgrafos del árbol generador mínimo de un grafo G.

Invariante: me da un bosque generador mínimo de i aristas (porque estamos en la iteración i

Kruskal no me asegura que tenga un grafo conexo)

# Prim

![alt text](image-7.png)

Prim chequea si metemos un ciclo con una lista.

Complejidad: n log n

Usa el heap para buscar mínimos. En particular con un Fibonacci heap es la mejor complejidad.

Invariante: Me da un subarbol del AGM.

Prim

# Ejercicios

# Cifu

![alt text](image-8.png)
![alt text](image-9.png)

Modelado: 
1. Vértices: ciudades.
2. Aristas: rutas de una ciudad a otra.
3. Pesos: r . distEnKM(x, y) + c_{x, y}

Algoritmo: Prim. Porque tenemos que comenzar desde la ciudad de Cifu y porque nos asegura que vamos a tener un subgrafo conexo.

La complejidad es: O(k*n) porque tenemos k iteraciones cada una cuesta n.

probamos que Prim no me da el subgrafo mínimo del AGM: 

> Si no nos interesara el peso entonces usamos BFS porque es más barato en complejidad.

![alt text](image-10.png)
![alt text](image-11.png)

![alt text](image-12.png)

![alt text](image-13.png)
![alt text](image-14.png)

# Conjuntos deseables

![alt text](image-15.png)

Un subgrafo inducido son todas las aristas que inciden en ese conjunto de nodos.

![alt text](image-16.png)

a)
```
Comentario personal: tiene sentido porque Kruskal me ordena todas las aristas entonces si existe una iteración 1 <= j <= |E| entonces seguro que voy a tener un bosque conexo (por invariante de Kruskal) donde para cada componente conexa del bosque entonces sus aristas incidentes son mayores o iguales para toda arista de esa componente. 

Solución: 

[ver diapos]
```

Probamos que toda deseable es componente conexa.

b)
```
Algoritmo: 

Ir haciendo Krukal, si genero una nueva componente conexa entonces sumo 1 al contador, si ya tenía la componente conexa y cumplía la propiedad de que se le puede agregar una arista más de forma segura entonces sumo 1 al contador, caso contrario no hago nada.


[ver diapos]
```

# Audífonos defectuosos

![alt text](image-17.png)

Todo camino de un AGM es miniMax.
Todo camino de un AGMáx es Maximin.

![alt text](image-18.png)


![alt text](image-19.png)

![alt text](image-20.png)
![alt text](image-21.png)

Podemos justificar (y confirmado que va a estar bien) que: luego de tener el AGM entonces hacer DFS desde la casa de sasha y eso me devuelve el camino de la casa de sasha hasta ciudad, luego devuelvo lo que me piden.

![alt text](image-22.png)

La uno es hacer DFS en el AGM e ir actualizando las aristas con mayor peso.

![alt text](image-23.png)

# Alimentando hormigas

![alt text](image-24.png)
![alt text](image-25.png)

```
Se me ocurre que para el modelado lo que tengo que hacer es decir que cada cueva es un nodo y que si existe una cueva conectada a la raíz, entonces esa cueva tiene un tubo, para toda otra cueva que no es la raíz entonces es porque hay un túnel.

[ver diapos]
```

Generalmente lo que más nos conviene es modelar bien al problema con un grafo y luego corremos un algoritmo de los conocidos como caja negra para poder resolver al problema.

# Rutas y aeropuertos

![alt text](image-26.png)


```
Se me ocurre que lo que se puede hacer es algo como: 

- Un grafo tiene todas las ciudades conectadas con todas las demás ciudades y cada ciudad es un nodo, cada arista entre dos nodos es lo que sale crear un camino entre dos ciudades.
- Un nodo aeropuerto que se conecte a todos y los demás nodos. La arista de aeropuerto a toda ciudad es el costo de crear un aeropuerto en esa ciudad.
- Correr Prim desde alguna ciudad.
```

![alt text](image-27.png)
![alt text](image-28.png)

![alt text](image-29.png)
![alt text](image-30.png)
![alt text](image-31.png)
![alt text](image-32.png)

#

[Falta toda una parte de las diapos, hay que leerla porque no la dieron]
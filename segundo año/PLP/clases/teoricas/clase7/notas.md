# Clase Grafos
## Nota para el lector:
Esta clase es pesadita a nivel definiciones, van a haber muchas capturas de pantalla de las diapositivas.

---

Ejemplito para comenzar: ¿Cuánto nos tardamos en caminar desde Ciudad universitaria hasta Plaza Italia? ¿Y en Auto?

## ¿Qué es un grafo?
**INFORMALMENTE:** Es una estructura matemática que nos permite modelar una gran cantidad de problemas! Poder modelarlos nos ayuda a encontrar soluciones sobre los mismos. Son puntos en un espacio los cuales están conectados, a esas conexiones se les llama "relaciones".

![alt text](image.png)
![alt text](image-1.png)

## Definiciones
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)
Interesante lo de los $\Delta$ y $\delta$. Eso no estaba el cuatrimestre pasado.
![alt text](image-5.png)
![alt text](image-6.png)
Hay $\frac{n*(n-1)}{2}$ porque por cada vertice lo tengo que conectar con todos los demás (de ahí $n*(n-1)$), el detalle es que hay que dividirlo entre dos porque sino estoy contando dos veces la misma arista que me conecta a dos vértices distintos.
![alt text](image-7.png)
![alt text](image-8.png)

**Ojo:** Nada nos limita a repetir aristas o hacer notaciones de aristas "volteadas" (porque si e es arista y a y b son vertices, entonces e=(a,b)=(b,a))

![alt text](image-9.png)
![alt text](image-10.png)
![alt text](image-11.png)
![alt text](image-12.png)

El subgrafo generador no tiene por qué tener todas las aristas necesariamente, o sea, no tiene por qué conectar a todos los vértices.

El subgrafo inducido: "si me llevo vértices, entonces también me llevo sus aristas".

![alt text](image-13.png)

Con maximal se refiere a que si al subgrafo le agrego un vértice más, entonces ya no me queda conexo.

![alt text](image-14.png)

Que sea bipartito significa que lo puedo colorear con dos colores.
Un grafo completo no puede ser bipartito, si uno es de un color, entonces todos los demás deben ser del otro color.

![alt text](image-15.png)
![alt text](image-16.png)
![alt text](image-17.png)
![alt text](image-18.png)
![alt text](image-19.png)

Lo de ser isomorfos es que exista una f que me cambie el renombre de las aristas de uno para mandarme a las aristas del otro.

Todo grafo completo es isomorfo a todo grafo completo del mismo tamaño.

Para probar que no existe función hay que probar todas las funciones posibles, eso es $n!$

O sea, que sean isomorfos significa que uno es un reordenamiento del otro manteniendo las aristas. Algo así como tomar un par de vértices de un grafo, y moverlos a algún lado del espacio de modo tal que mantengo al mismo grafo pero con otra pinta.

![alt text](image-20.png)
![alt text](image-21.png)
![alt text](image-22.png)
![alt text](image-23.png)


![alt text](image-24.png)
![alt text](image-25.png)
![alt text](image-26.png)
![alt text](image-27.png)
![alt text](image-28.png)

Lo de recorrido/camino orientado se refiere a que el punto final de un arco debe ser el punto de comienzo del siguiente arco que me manda de un nodo a otro. 

![alt text](image-29.png)

## Partes de un grafo
- **Vértices:** son los puntos.

# Notas:
- un camino hamiltoniano es un recorrido por un grafo donde se pasa por todos los vértices exactamente una sola vez.
- Un grafo es "planar" cuando las aristas no se cruzan. Siempre que tengo un grafo planar entonces lo puedo convertir en un mapa y si tengo un grafo que es planar entonces siempre lo puedo pintar con 4 colores.
- Un grafo es completo si todos lso vertices son vecinos, un grafo es conexo si existe un camino entre todo par de vertices (no necesariamente directo).
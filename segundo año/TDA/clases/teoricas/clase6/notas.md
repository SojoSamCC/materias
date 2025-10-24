# Camino mínimo en grafos parte 1

![alt text](image.png)

O sea que lo que queremos es minimizar la suma de aristas de un nodo a otro. 

En un camino mínimo no se repiten aristas.

![alt text](image-1.png)

O sea, si podemos llegar de un nodo a otro entonces la distancia entre un nodo y otro **no** va a ser infinito.

![alt text](image-2.png)

![alt text](image-3.png)

O sea, no podemos hablar de caminos mínimos si tenemos ciclos negativos.

EL último punto dice que para todo nodo perteneciente a un camino mínimo enttre otros dos nodos, entonces el camino entre esos nodos internos también es mínimo.

![alt text](image-4.png)

![alt text](image-5.png)

# Dijkstra

![alt text](image-6.png)

![alt text](image-7.png)

![alt text](image-8.png)

Dijkstra me devuelve el camino mínimo de un nodo a todos los demás.

## Implementacion De Dijkstra

```python
def dijkstra(G, origen):

    # >> Inicialización <<
    pi = {}
    prev = {}
    S = = [origen]

    pi[origen] = 0
    prev[origen] = None

    for u in G.nodes():
        if u in S:
            continue
        
        aux = False
        for e in G.edges():
            if u in e and origen in e:
                pi[u] = G[u][origen]['weight']
                prev[u] = origen
                aux = True

        if not aux:
            pi[u] = inf
            prev[u] = None
    
    # >> Recorrido <<
    while len(S) != len(G.nodes()):
        
        w = None
        minimo = None
        
        # Busco el nodo de minimo pi entre los que no visitamos
        for clave, valor in pi:
            if clave in S:
                continue
            if minimo is None and clave not in S:
                minimo = valor
                w = clave
            elif valor < minimo and clave not in S:
                minimo = valor
                w = clave
        S.append(w)

        for nodo in G.nodes():
            if nodo in S:
                continue
            if w, node in G.edges():
                if pi[nodo] >= pi[w] + G[u][w]['weight']:
                    p[nodo] = pi[w] + G[u][w]['weight']
                    prev[nodo] = w

    return pi, prev
```

## Demo de Dijkstra

![alt text](image-9.png)
El lema es el invariante de Dijkstra

![alt text](image-10.png)
La idea es que si reemplazo al infinito por un valor menor a infinito, y a partir de ahí lo único que hago es ir achicando con las distancias que fui encontrando, entonces tengo que llegar al mínimo.

Si aparece un infinito es porque sí o sí ese nodo estaba desconectado del origen.

![alt text](image-11.png)
![alt text](image-12.png)

![alt text](image-14.png)

## Complejidad

![alt text](image-13.png)

Ese O(n^2) en realidad es O(V*E) porque tenemos un while que me recorre todos los nodos y un for que me recorre todas las aristas.

# Notas
- Dijkstra no puede con aristas negativas!

# Bellman - Ford

![alt text](image-15.png)

Para saber cuántas veces había que recorrer el algoritmo solo hay que saber que:
1. Si no hice cambios: entonces ya está.
2. Si tengo más de n-1 veces iteradas: entonces ya está.

## Demo Bellman - Ford

![alt text](image-16.png)

![alt text](image-17.png)

![alt text](image-18.png)

![alt text](image-19.png)

![alt text](image-20.png)

![alt text](image-21.png)


```python
def bellmanford(G, v):

    pi = {}
    pi[v] = 0
    for u in G.nodes():
        if u != v:
            pi[u] = inf
    
    cambio = True

    iteraciones = 0
    maximo = len(G.nodes()) - 1
    while cambio and iteraciones < maximo:
        pi_prev = pi.copy()
        cambio = False

        for u in G.nodes():
            if u == v:
                continue

            pesos = []
            for e in G.edges():
                if u in e:
                    vecino = e[1] if e[1] != u else [e]
                    peso = G[e[0]][e[1]]['weight'] + pi_prev[vecino]
                    pesos.append(peso)

            minimo = min(pesos)
            
            if pi[u] != minimo:
                cambio = True
                pi[u] = minimo

        iteraciones += 1

        if iteraciones == maximo:
            print("Encontré ciclo negativo")

    return pi
```

![alt text](image-22.png)

![alt text](image-23.png)

![alt text](image-24.png)

![alt text](image-25.png)

![alt text](image-26.png)

[ver el resto de las diapos en el pdf de la clase]

# Notas

- El invariante de Bellman Ford es: hasta la iteración k todas las aristas que estén a distancia menor a k del origen, ya están a una distancia óptima. [verificar, es algo así como el corolario]

## Complejidad

# Floyd - Warshall



# Notas

- Google maps usa el algoritmo de Dijkstra.
- Charla de DL.
- Para que Bellman ford encuentre los ciclos negativos, entonces le metemos DFS adentro y que verifique los ciclos negativos.
- Bellman-Ford relaja más la frontera en comparación con Dijkstra porque Dijkstra en cada iteración siempre me asegura que cuando actualiza siempre llega a un óptimo, mientras que con Bellman Ford como no se asegura eso en cada iteración entonces se dice que "se relaja" la misma.
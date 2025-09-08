# Algoritmos greedy

Todos los algoritmos greedy tienen estas propiedades:
1. Greedy choice: es regirme por una desición en la que confío con que mi desición me va a llevar a una solución óptima a través de una solución óptima local (mi desición). O sea, yo me la paso tomando una desición óptima local con respecto al subproblema que estoy tratando y rezo porque me lleve a la solución óptima global.

2. Tiene que tener la propiedad de poder dividir un problema en subproblemas óptimos. Esto se combina con la propiedad 1. para ir dividiendo en subproblemas usando mi greedy choice.

## Heurística

Es el método que en principio no me da la mejor solución pero sí que puede darme una solución lo suficientemente buena.

- Greedy cuando funciona es difícil de demostrar, pero cuando **no** funciona entonces es fácil de demostrar que no funciona.

## Problema de la mochila (pero ahora es fraccionaria!)

Originalmente, la mochila es 1/0 (lo pongo, o no lo pongo).

Su función recursiva es la siguiente:
$$
mochila(objetos, capacidad) = \begin{cases}
0 \text{ , si } objetos=0 \\
mochila(objetos[1:],capacidad) \text{ , si } PesoObjeto_i \gt c \\
max(mochila(objetos[1:],capacidad), \ beneficioObjeto_i + mochila(objetos[1:], capacidad-PesoObjeto_i)) \text{, cc}\\
\end{cases}
$$

Su implementación en python es: 
```python
def mochila(pesos: list[int], beneficios: list[int], capacidad: int)->int:
    
    if len(pesos) == 0 or capacidad==0:
        return 0

    if pesos[0] > capacidad:
        return mochila(pesos[1:], beneficios[1:], capacidad)
    
    pongo_el_objeto = mochila(pesos[1:], beneficios[1:], capacidad-pesos[0]) + beneficios[0]
    no_pongo_el_objeto = mochila(pesos[1:], beneficios[1:], capacidad)

    el_mejor = max(pongo_el_objeto, no_pongo_el_objeto)

    return el_mejor
```

Ahora digamos que es fraccionaria (se pueden fraccionar los objetos)

```python
def mochila_fraccionaria(pesos: list[int], beneficios: list[int], capacidad: int)->int:
    pesos = sorted(pesos)
    beneficios = sorted(beneficios)
    lista_beneficio_por_peso = [beneficios[i] / pesos[i] for i in range(len(pesos))]
    lista_beneficio_por_peso = sorted(lista_beneficio_por_peso)

    beneficio_acumulado= 0
    for i in range(len(lista_beneficio_por_peso)-1, -1, -1):
        if capacidad<=0:
            return beneficio_acumulado
        if pesos[i] <= capacidad:
            capacidad -= pesos[i]
            beneficio_acumulado += beneficios[i]
    return beneficio_acumulado
```
> Esta versión es diferente a la que hizo el profe, pero a mi parecer es más fácil de entender.

## Problema del cambio:
Es simple el algoritmo, voy devolviendo la moneda más grande tal que no se me pase de la cantidad de vuelto que tengo que dar.

Esto va a funcionar siempre que el sistema de monedas sea canónico, es decir que desde la moneda más chica hasta la más grande, la moneda siguiente es al menos el doble que la actual.

## Tiempo de espera total en un sistema

**Problema:** un servidor tiene n clientes para atender, y los puede atender en cualquier orden. Para i=1, ..., n, el tiempo necesario para atender al cliente i es $t_i \in R+$. El objetivo es determinar en qué orden se deben atender los clientes para minimizar la suma de los tiempo de estepera de los clientes.

La idea para resolver esto es ordenar desde el que tarda menos en atenderse hasta el que tarda más.

```python
def fuerza_bruta(array_tiempo_de_espera: list[int])->list[int]:
    if len(tiempos) == 0:
        return 0
    
    valores = []

    for i in range(0, len(tiempos)):
        valor = fuerza_bruta(tiempos[:i] + tiempos[i+1:]) + tiempos[i] * (len(tiempos)-1)
        valores.append(valor)

    return min(valores)
```
Es n*n! porque tengo n! llamadas recursivas y para cada nivel calculo el máximo. Por cada nivel elijo un tiempo, y luego me fijo el minimo del array que me queda de haber elegido. Basta ver el árbol de recursión porque cada nodo tiene como hijos todos los demás tiempo menos el tiempo de ese nodo y a su vez hay que ver en O(n) por cada nodo cuál es el mínimo de esos.

```python
def tiempo_espera_total_sistema_greedy(array_tiempo_de_espera: list[int])->list[int]:
    array_tiempo_de_espera = sorted(array_tiempo_de_espera)

    tiempo_espera = 0
    for i in range(len(array_tiempo_de_espera)):
        tiempo_espera += sum(array_tiempo_de_espera[:i])
    return tiempo_espera
```

## Selección de actividades

Situación: tenemos un aula y varias actividades quieren usarla dirante el día.

Cada actividad tiene hora_inicio, hora_fin, duración.

¿Cuál es el número máximo de actividades que podemos programar para el aula sin que se solapen?

## Demostrar por exchange
La idea es simple, agarro mi solución greedy y una óptima arbitraria y luego "transformo" la óptima en mi greedy.

No nos van a pedir que demostremos que algo es óptimo sin decirnos que **es** óptimo.

Pasos:

1. Suponer que existe una solución ... **completar con la diapo que tiene esquema de colores en morado**

en la demo ponen algo como $s(o_i) \geq f(o_{i-1})$ ahí se refieren a que el tiempo de comienzo (start) de la otra actividad **debe** ser mayor que el tiempo de finalización de la actividad anterior. Es la diapo 13.

El lema más poderoso y que hay que demostrar para poder completar la demostración principal del greedy por contradicción es:
$$
\forall i \leq min(|G|, |O|) 
$$
Hipotesis inductiva es: 

$f(g_{i-1}) \leq f(o_{i-1}) \leq s(o)$ entonces por transitividad $f(g_{i-1}) \leq s(o)$

Hacerlo por contradicción NO puede tener cosas diferentes en el medio porque siempre tomamos la que terminaba primero.

una implementación de esto en python es
```python
def fuerza_bruta(actividades: list[int, int], final_ultima_actividad: int = 0)->list[int,int]:
    
    if actividades == []:
        return 0

    lista_posibles_candidatos = [0]
    for i in range(len(actividades)):
        principio, fin = actividades[i]
        if principio >= final_ultima_actividad: # if es candidato
            cant_actividades = 1 + fuerza_bruta(actividades[:i]+ actividades[i+1:], fin)
            lista_posibles_candidatos.append(cant_actividades)
    
    return max(lista_posibles_candidatos)
```
La complejidad es n*n! porque después de elegir una actividad tengo que ver todas las demás combinaciones con las actividades que me quedaron si elegí esa, y eso con todas las demás actividades.

```python
def seleccion_de_actividades_greedy(actividades: list[int, int])->list[int,int]:

    actividades = sorted(actividades, key=lambda actividad: actividad[1]) # esta vaina me ordena la lista segun la segunda componente de cada sublista.

    cant_actividades= 0
    fin_ultima_actividad = actividades[0][1]
    for i in range(len(actividades)):
        principio, fin_nueva_actividad = actividades[i]
        if principio >= fin_ultima_actividad:
            cant_actividades += 1
    
    return cant_actividades
```
> Esta versión es diferente a la que hizo el profe, pero a mi parecer es más fácil de entender.

### Notita programación dinámica
- Programación dinámica: tengo un problema -> lo divido en subproblemas -> busco el óptimo.
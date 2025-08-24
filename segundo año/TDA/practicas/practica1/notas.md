# Divide & Conquer

## Teorema maestro
$$
T(n)=
\begin{cases}
1 \text{ , si n=1} \\
a * T(\frac{n}{2}) + f(n) \text{ , n>1}
\end{cases}
$$

Donde

- Si $f(n) = O(n^{(log_c{a})-\epsilon}) \text{ para } \epsilon >0 \text{, entonces } T(n)= \Theta(n^{log_c{a}})$
- Si $f(n) = \Theta(n^{log_c{a}}) \text{, entonces } T(n)= \Theta(n^{log_c{a}} * \log{n})$
- Si $f(n) = \Theta(n^{log_c{a}}*\log^{k}{n}) \text{ para algun } k \geq 0 \text{, entonces } T(n)= \Theta(n^{log_c{a}} * \log^{k+1}{n}) \text{ (generalizacion del caso anterior)}$ 
- Si $f(n) = \Omega(n^{(log_c{a})+\epsilon}) \text{ para } \epsilon>0 \text{ y } a*f(\frac{n}{c}) < k*f(n) \text{ para } k<1 \text{ y } n \text{ suficientemente grandes, entonces } T(n)= \Theta(f(n))$

## Ejercicio 1
1. 
    - Divide: linea 5 de merge_sort.
    - Conquer: lineas 6 y 7 de merge_sort.
    - Combine: linea 9 de merge_sort.

2. Se divide en 2 subproblemas.
3. son de tamaño $\frac{n}{2}$.
4. Es de costo $O(n)$ pues hay que hacer una pasada lineal por el subarray que tenga menor tamaño usando el algortimo de merge.
5. $$
    mergeSort(array) = 
    \begin{cases} 
    array \text{  , si largo(array) == 1} \\
    merge(\ array[:largo(array)//2]\ , \ \ array[largo(array)//2:])
    \end{cases}
    $$
6. Como se divide en 2 subproblemas, entonces nuestro $a=2$, como cada subproblema es de tamaño $\frac{n}{2}$ entonces nuestro $c=\frac{n}{2}$ y como lo que nos cuesta (computacionalmente hablando) hacer el combine es lineal en el tamaño de la entrada, entonces nuestro $f(n)=O(n)$, luego
$$
\implies T(n) = 2*T(\frac{n}{2})+O(n)
\text{, lo cual matchea con el segundo caso del teorema maestro (pues } n^{log_2{2}}=n^{1}\text{)} 
$$
$$\ \therefore \ T(n) = \Theta(n^{log_2{2}}*\log{n}) = \\ = \Theta(n^{1}*\log{n}) = \\ = \Theta(n*\log{n}) = \\ = O(n*\log{n})
$$ 

## Ejercicio 2
1. 
    - Divide: linea 5
    - Conquer: lineas 8 y 10
    - Combine: linea 7, tecnicamente no es un combine del array, es simplemente devolver un elemento del array en O(1)

2. Se divide en 2 subproblemas.
3. El tamaño de los subproblemas es $\frac{n}{2}$
4. El costo de combinar los resultados de los subproblemas es O(1).
5. $$
    busquedaBinaria(arr, objetivo, izq, der) = 
    \begin{cases} 
    objetivo \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad \ \text{ , si arr[(izq + der) // 2] = objetivo} \\
    busquedaBinaria(arr, objetivo, izq, ((izq + der) // 2)-1) \text{  , si arr[(izq + der) // 2] > objetivo} \\
    busquedaBinaria(arr, objetivo, ((izq + der) // 2)+1, der) \text{  , si arr[(izq + der) // 2] < objetivo} \\
    \end{cases}
    $$
6.  Tenemos $a= 1 \land c= 2 \land f(n) = O(1) \implies T(n) = 1*T(\frac{n}{2}) + O(1)$, esto nos indica que estamos en el segundo del teorema maestro, por lo tanto nos queda la complejidad $O(\log{n})$ (ver ejercicio 1 por si quedaron dudas de como se llego a ese resultado).

## Ejercicio 3
Para resolver esto podemos plantear un algoritmo donde dividimos al arreglo a la mitad cada vez y que cuando lleguemos al caso donde solo tenemos un arreglo de tamaño entonces comparamos si la suma de los elementos de ese arreglo es igual mayor a la suma de los elementos en el subarreglo del lado derecho.

```python
def izquierdaDominante(array: list[int])-> bool:
    if len(array)==2:
        return array[0]>=array[1]

    # Divide
    medio = len(array)//2 # Recordemos que sabemos que el largo del array es potencia de dos.

    # Conquer
    parte_izquierda=array[:medio]
    parte_derecha=array[medio:]
    
    # Combine
    es_mas_a_la_izquierda:bool = sum(parte_izquierda)>=sum(parte_derecha)

    if es_mas_a_la_izquierda:
        return izquierdaDominante(parte_izquierda)
    else:
        return False
```

En este caso 
$$
a=1 \land c=\frac{n}{2} \land f(n)=O(n) \implies T(n) = 1*T(\frac{n}{2})+O(n) \\
. \\
\text{Por teorema maestro caemos en el segundo caso } \\
\therefore \\
T(n) \in O(n*\log{n})
$$

## Ejercicio 4
Podemos pensar en un algoritmo en el que nos vamos parando en la mitad del arreglo siempre, luego nos fijamos si el arreglo en esa posicion es negativo y nos vamos a la mitad derecha... aunque la manera mas piola es irnos a la mitad del arreglo, comparar el valor del array en esa posicion junto con su indice y decidir si irnos a la mitad izquierda o derecha.

```python
def indiceEspejo(array:list[int], desde:int = 0, hasta:int = None)->int:
    if hasta==None:
        hasta=len(array)

    if desde>hasta or (desde==hasta and array[desde]!=desde):
        return None
    
    # Divide
    indice_actual:int = ((hasta - desde) // 2) + desde

    # Combine
    valor_en_posicion_actual = array[indice_actual]    
    if valor_en_posicion_actual == indice_actual:
        return indice_actual

    # Conquer
    ir_a_la_derecha = valor_en_posicion_actual < indice_actual

    if ir_a_la_derecha:
        return indiceEspejo(array=array, desde= indice_actual+1, hasta=hasta)
    else:
        return indiceEspejo(array=array, desde= 0, hasta=indice_actual-1)
```

En este caso:
$$
a=1 \land c=2 \land f(n) = O(1) \implies T(n) = 1*T(\frac{n}{2})+O(1) \\
. \\
\text{Por teorema maestro caemos en el segundo caso } \\
\therefore \\
T(n) \in O(\log{n})
$$

## Ejercicio 5
Lo que se me ocurre es que podemos hacer un algoritmo que haga una sola multiplicacion entre dos numeros y se la guarde, luego cuando le vuelva a aparecer lo que hace es reutilizar el producto que uso y que continue asi.

Para lograr eso lo que se puede hacer es fijarnos si el exponente era par o impar, pues, si era par entonces es lo mismo multiplicar $n^\frac{b}{2} * n^\frac{b}{2}$ pero con el detalle que la segunda vez que debo calcular $n^\frac{b}{2}$ ya lo tenia calculado de antes, entonces solo basta con multiplicar el resultado que obtuve consigo mismo. En caso de que el exponente sea impar, entonces solo basta llevarlo al mundo de los exponentes pares y al final multiplicar por la base original. Gracias a Dios que la multiplicacion es conmutativa jajajajaja.
```python
def potenciaLogaritmica(n:int, exponente:int)->int:

    # Conquer
    if exponente==1:
        return n
    
    # Divide
    if exponente % 2 == 0:
        potencia= potenciaLogaritmica(n=n, exponente=exponente/2)
        
        # Combine
        return potencia * potencia
    else:
        potencia= potenciaLogaritmica(n=n, exponente=exponente-1)
        
        # Combine
        return n * potencia
```
En este caso:
$$
a=1 \land c=2 \land f(n) = O(1) \implies T(n) = 1*T(\frac{n}{2})+O(1) \\
. \\
\text{Por teorema maestro caemos en el segundo caso } \\
\therefore \\
T(n) \in O(\log{n})
$$

> Nota: este ejercicio me costó mucho más que los anteriores.
## Ejercicio 6
Lo que se me ocurre es que podemos pararnos en la mitad del array y ver lo siguienteÑ
- Si el que está a mi izquierda es menor que yo y el que está a mi derecha también, entonces soy el máximo.
- Si el que está a mi izquierda es mayor que yo y el que está a mi derecha menor, entonces me muevo pa' la izquierda.
- Si el que está a mi izquierda es menor que yo y el que está a mi derecha mayor, entonces me muevo pa' la derecha.

```python
def maximoMontana(array: list[int])->int:
    largo = len(array)
    
    indice_actual = largo // 2
    
    indice_izquierda = indice_actual-1
    indice_derecha = indice_actual+1

    el_maximo_es_uno_de_los_bordes: bool = indice_derecha >= largo or (indice_izquierda<0)
    if el_maximo_es_uno_de_los_bordes:
        return array[indice_actual]
    
    soy_el_maximo: bool = (array[indice_izquierda] < array[indice_actual]) and (array[indice_derecha] < array[indice_actual])
    if soy_el_maximo:
        return array[indice_actual]
    
    debo_ir_a_la_izquierda: bool = array[indice_izquierda] > array[indice_actual] and array[indice_derecha] < array[indice_actual]
    if debo_ir_a_la_izquierda:
        new_array=array[:indice_actual]
        return maximoMontana(array=new_array)
    else:
        new_array=array[indice_actual+1:]
        return maximoMontana(array=new_array)
```

## Ejercicio 7
1. Para resolver esto hay que trabajar usando el arbol de recursión, hagamoslo via analítica del árbol de recursión:
$$
T(n) = T(n-2)+5 \\
T(n) = (T(n-4)+5)+5 \\
T(n) = ((T(n-6)+5)+5)+5 \\
T(n) = (((T(n-8)+5)+5)+5)+5 \\
T(n) = ((((T(n-8)+5)+5)+5)+5)+5 \\
. \\ 
. \\
. \\
T(n) = \sum_{k=1}^{n}{T(n-(k*2))+5} \\.\\ 
T(n) = 5*\sum_{k=1}^{n}{T(n-(k*2))}
$$
> No sé cómo justificar que esto es $n*\log{n}$ sin usar el teorema maestro.
> Me pasa esto con todos los incisos de este ejercicio. 

## Ejercicio 8
Este ejercicio es medio un quilomobo, lo hicimos en clase y la idea es la siguiente:
1. Parto al array a la mitad y me fijo si la mitad izquierda suma mas que la derecha.
2. Luego debo comparar esa suma la suma de los elementos del subarray que proviene de la concatenación del mejor subarray que me podía ofrecer el lado izquierdo con el mejor subarray que me podíá ofrecer el lado derecho.

```python
def maximaSubsecuencia(array:list[int])->int:
    largo:int = len(array)

    # Combinar
    if largo == 1:
        return array[0]
    
    # Dividir
    medio: int                = largo // 2
    parte_derecha:list[int]   = array[medio:]
    parte_izquierda:list[int] = array[:medio]

    # Conquistar
    arr_acc_parte_derecha:list[int] = [0]
    for i in range(len(parte_derecha)):
        arr_acc_parte_derecha.append(parte_derecha[i]+arr_acc_parte_derecha[i])
    arr_acc_parte_derecha=arr_acc_parte_derecha[1:]

    arr_acc_parte_izq=parte_izquierda.copy()
    for i in range(len(parte_izquierda)-2,-1,-1):
        arr_acc_parte_izq[i]=arr_acc_parte_izq[i+1]+arr_acc_parte_izq[i]

    max_parte_izquierda:int = max(arr_acc_parte_izq)
    max_parte_derecha:int   = max(arr_acc_parte_derecha)

    max_parte_del_medio: int = max_parte_izquierda + max_parte_derecha
    
    max_parte_derecha = maximaSubsecuencia(array[medio:])
    max_parte_izquierda = maximaSubsecuencia(array[:medio])

    # Combinar
    return max(max_parte_izquierda, max_parte_del_medio, max_parte_derecha)
```
> Esta es la función que más me ha costado hasta el momento, un quilombo total.

## Ejercicio 9
Esto me recuerda a potencia logarítmica, hay que hacer un poco de magia para que las sumas den bien, pero bueno... lo que se me ocurre para resolver esto es hacer algo como que 
- El caso base es cuando el exponente sea 1 y automaticamente devuelvo A.
- Si el exponente no es 1 entonces lo que tengo que hacer es devolver la suma de A_1=[matriz que vino del resultado de calcular potenciaSum con matriz con EXP=[exponente que era el logaritmo del exponente de entrada]]+[producto de A_1 con potencia(matriz=A, exponente=EXP)]

```python
def potenciaSum(matriz, exponente:int):

    if exponente == 1:
        return matriz

    # Divide
    logaritmo_en_base_dos_exponente:int = exponente // 2

    # Conquer
    potencia_izquierda = potenciaSum(matriz=matriz, exponente=logaritmo_en_base_dos_exponente)

    producto_de_las_dos_matrices_que_ya_conocia= producto_matricial(potencia_izquierda, potencia(matriz=matriz, exponente=logaritmo_en_base_dos_exponente)

    # Combine
    return suma_matricial(potencia_izquierda, producto_de_las_dos_matrices_que_ya_conocia))
```
no pide calcular la complejidad, pero como este algoritmo puede parecer que se pasa de la maxima complejidad que te dan, entonces calculemosla a ver (hasta el momento de escrito esto yo también tengo la necesidad de calcularla a ver qué ondis).

$$
a=1 \land c=2 \ f(n)=O(1) \implies T(n) = 1*T(\frac{n}{2})+O(1) \\
. \\
\text{Por teorema maestro caemos en el segundo caso } \\
\therefore \\
T(n) \in O(\log{n})
$$

> $f(n)=O(1)$ porque el tamaño de las matrices **siempre** es 4x4, entonces como es conocido el tamaño de las mismas (y porque hacer suma y producto de matrices no altera la dimensión) podemos decir que computacionalmente la complejidad de todas esas operaciones es O(1).

> $a=1$ porque siempre tomamos el resultado de la suma de las matrices de la izquierda (lo cual es una matriz) y operamos con ella sin que nos importe qué había en las matrices de la derecha (hay que convencerse de esto).

> $c=2$ porque siempre dividimos al exponente entre dos.

## Ejercicio 10
Puede sonar medio quilombo, acá el detalle es que como no es un ABB entonces la busqueda hay que hacerla por todos los nodos posibles hasta encontrar el buscado. Encuentro que no hay manera de salir de una busqueda en O(n*log(n)) donde n es la cantidad de nodos en el árbol.

```python
def distanciaMaxima(arbol, nodo_origen, nodo_destino,  cant_nodos_arbol:int, distancia=0, ir_a_la_izquierda:bool = True, ir_a_la_derecha:bool = True):

    if nodo_origen == nodo_destino:
        return distancia
    elif distancia == cant_nodos_arbol-1:
        return None

    # Divide
    padre=nodo_origen.padre
    hijo_izquierdo=nodo_origen.izq
    hijo_derecho=nodo_origen.der

    # Conquer
    if ir_a_la_izquierda:
        if hijo_izquierdo != None:
            distancia_izquierda = distanciaMaxima(
                arbol=arbol,
                nodo_origen=hijo_izquierdo,
                nodo_destino=nodo_destino,
                cant_nodos_arbol=cant_nodos_arbol-distancia,
                distancia=distancia+1,
                ir_a_la_izquierda=True,
                ir_a_la_derecha=True,
                )

            # Combine
            if distancia_izquierda != None:
                return distancia_izquierda

    # Conquer
    if ir_a_la_derecha:
        if hijo_derecho != None:
            distancia_derecha = distanciaMaxima(
                arbol=arbol,
                nodo_origen=hijo_derecho,
                nodo_destino=nodo_destino,
                distancia=distancia+1,
                cant_nodos_arbol=cant_nodos_arbol-distancia,
                ir_a_la_izquierda=True,
                ir_a_la_derecha=True,
                )
        
            # Combine
            if distancia_derecha != None:
                return distancia_izquierda
    
    # Conquer
    if padre != None:
        soy_hijo_izquierdo: bool = padre.izq == nodo_origen

        if soy_hijo_izquierdo:
            distancia_padre = distanciaMaxima(
                arbol=arbol,
                nodo_origen=hijo_derecho,
                nodo_destino=nodo_destino,
                distancia=distancia+1,
                cant_nodos_arbol=cant_nodos_arbol-(distancia+1),
                ir_a_la_izquierda= False,
                ir_a_la_derecha= True,
                )
        else:
            distancia_padre = distanciaMaxima(
                arbol=arbol,
                nodo_origen=hijo_derecho,
                nodo_destino=nodo_destino,
                distancia=distancia+1,
                cant_nodos_arbol=cant_nodos_arbol-(distancia+1),
                ir_a_la_izquierda= True,
                ir_a_la_derecha= False,
                )
        
        # Combine
        return distancia_padre
    # Combine
    return None # Creo que esta línea no es necesaria, pero la dejo por si acaso.
```
Complejidad en este caso:
$$
a=3 \land c=3 \land f(n)=O(1) \implies T(n) = 3*T(\frac{n}{3})+O(1) \\
. \\
\text{Por teorema maestro caemos en el segundo caso} \\
\therefore \\
T(n) \in O(n*\log{n})
$$

## Ejercicio 11
Cuando nos meten esos de los índices en
$$
A[1,\dots,n] \\
. \\
\text{y que luego dicen que} \\
. \\
(\forall \ i,j) \ \  1\leq i < j \leq n \ \ / \ \ A[i] > A[j] 
$$
Nos dicen que si tú te paras en la posición j del array, entonces solo te interesan las posiciones i menores a j en el array tales que el valor del array en esa posición i es mayor que el valor del array en la posición j. 

Lo que se me ocurre para resolver esto es hacer una pasada lineal viendo todas las parejas posibles pero sin tener que computar las que ya vimos antes. O sea, me voy moviendo en el array posición por posición y me fijo las parejas posibles, luego cuando avance una posición j en el array, lo que hago es sumar las parejas que habían antes más el valor de la posición j anterior en caso de ser necesario.

Sin embargo hacer una implementación de ese estilo es más una cosa de programación dinámica, voy a hacer las dos.

> Notar que el tamaño del array tiene como precondición ser al menos 2, porque sino no se cumple $i < j$ en $\\(\forall \ i,j) \ \  1\leq i < j \leq n \ \ / \ \ A[i] > A[j]$
```python
def desordenSort_programacion_dinamica(array: list,  i:int =0, j:int =1, cant_parejas:int =0) -> int:

    el_anterior_era_mayor = array[i] > array[j]
    if i==0:
        return 1 if el_anterior_era_mayor else 0
    
    if el_anterior_era_mayor:
        cant_parejas+=1
    
    return desordenSort_programacion_dinamica(array=array, i=i+1, j=j+1, cant_parejas=cant_parejas)

def desordenSort(array: list) -> int:

    largo = len(array)

    if largo == 2:
        el_anterior_era_mayor = array[0] > array[1]
        return 1 if el_anterior_era_mayor else 0
    elif largo == 1:
        return 0 
    elif largo % 2 != 0:
        largo-=1
        cant_parejas_array_con_largo_par=desordenSort(array=array[:largo])
        if array[largo] > array[largo+1]:
            cant_parejas_array_con_largo_par+=1
        return cant_parejas_array_con_largo_par
    
    medio: int = len(array) // 2

    parejas_izquierdas:int = desordenSort(array=array[:medio])
    parejas_derechas:int = desordenSort(array=array[medio:])

    return parejas_izquierdas + parejas_derechas
```
Complejidad en este caso:
$$
a=2 \land c=2 \land f(n)=O(n) \implies T(n) = 2*T(\frac{n}{2})+O(1) \\
. \\
\text{Por teorema maestro caemos en el segundo caso} \\
\therefore \\
T(n) \in O(n*\log{n})
$$

> f(n) = O(n) porque rearmar al array toma a lo sumo O(n)

## Ejercicio 12
Este no se ve tan complicado, podemos partir a la matriz en cuadro pedazos porque es cuadrada al ser de $n\times n$ entonces lo que hacemos es hallar con la funcioncita mágica que nos dice en O(1) si hay un false o no.

```python
def cazadorDeFalsos(matriz:list[list[bool]], cuarto:int = None, i:int = 0, j:int = 0)->tuple[int,int]:

    largo = len(matriz)

    # Combine
    if cuarto == 1:
        return (i, j)
    
    # Divide
    if cuarto == None:
        cuarto:int = largo // 2
    
    i_0:int = i
    i_1:int = cuarto-1
    j_0:int = j
    j_1:int = j_0+cuarto-1

    # Conquer
    hay_false:bool = conjuncionSubmatriz(i_0, i_1, j_0, j_1)

    if hay_false:
        return cazacazadorDeFalsos(matriz=matriz, cuarto=i_1+1, i=i_0, j=j_0)
    else:
        if j_0+1 + cuarto >= largo:
            i_0+=cuarto
            j_0-=cuarto
        else:
            j_0+=cuarto
        return cazacazadorDeFalsos(matriz, cuarto=cuarto+1, i=i_0, j=j_0)
```
No estoy muy seguro de que esto funcione, pero puede funcionar como esquema en caso de que no funcione.


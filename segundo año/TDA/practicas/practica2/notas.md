# Técnicas Algorítmicas

> No tengo teimpo de resolver toda la guía al 100%, solo voy a hacer algunos ejercicios medio salteados.

## SumaSubconjuntosBT

Skip

## MagiCuadrados

    - $(n^{2})!$
    - Lo que se me ocurre es hacer algo como:
        ```
        PRE:
            - Asumo que existe función que me dice si una fila/columna/diagonal es valida o no.
            - Tengo un conjunto/lista/array o estructura de datos que me dice los números que ya coloqué.
            - Existe una lista que almacena los numeros ya elegidos y que no sirvieron.
        
        POST:
            for i < n: 
                for j < n:
                    un_numero_disponible = elegirUnNumeroQueNoEstaElegidoAun() # esta función me devuelve un numero random de los disponibles y que aun no esté elegido.
                    magiCubo[i][j] = un_numero_disponible
                    while !eraValido(magiCubo, un_numero_disponible, i ,j):
                        if un_numero_disponible == None:
                            return "No se puede hacer un magicubo con esta combinación"
                        un_numero_disponible = elegirUnNumeroQueNoEstaElegidoAun() # esta función me devuelve un numero random de los disponibles y que aun no esté elegido.
                        magiCubo[i][j] = un_numero_disponible
        ```

        Te debo lo de mostrar los niveles del árbol.
    - Encontrar cada magicubo disponible implica revisar todas y cada una de las permutaciones posibles de cada magiCubo y contar unicamente aquellas que eran válidas. Como estamos en el peor caso entonces eso significa que no tenemos podas importantes o bien no tenemos podas posibles. Finalmente armar un magicubo tiene complejidad $O(n^2)$, saber cuál o cuales son las correctas implicaría ver todas sus permutaciones, por lo tanto tendríamos en total $O(n^2)!$ nodos en el árbol de backtracking en el peor caso.

    - Sí mejora mucho con esta poda.
        ```
        PRE:
            - Asumo que existe función que me dice si una fila/columna/diagonal es valida o no.
            - Tengo un conjunto/lista/array o estructura de datos que me dice los números que ya coloqué.
            - Existe una lista que almacena los numeros ya elegidos y que no sirvieron.
            - El numero mágico es un variable global. La función que me dice si era valido toma en cuenta a este número mágico haciendo uso de la suma del enunciado.

        POST:
            for i < n: 
                for j < n:
                    un_numero_disponible = elegirUnNumeroQueNoEstaElegidoAun() # esta función me devuelve un numero random de los disponibles y que aun no esté elegido.
                    magiCubo[i][j] = un_numero_disponible
                    while !eraValido(magiCubo, un_numero_disponible, i ,j):
                        if un_numero_disponible == None:
                            return "No se puede hacer un magicubo con esta combinación"
                        un_numero_disponible = elegirUnNumeroQueNoEstaElegidoAun() # esta función me devuelve un numero random de los disponibles y que aun no esté elegido.
                        magiCubo[i][j] = un_numero_disponible
        ```
    No lo pienso implementar por falta de tiempo.

    - Te la debo. Sin embargo pego lo que dice chatGPT, modelo GPT-5:

        CHATGPT:

        Perfecto, la consigna que compartiste dice lo siguiente:

        **Enunciado (item e):**
        *"Demostrar que el número mágico de un cuadrado mágico de orden $n$ es siempre $(n^3 + n)/2$. Adaptar la poda del algoritmo del ítem anterior para que tenga en cuenta esta nueva información. Modificar la implementación y comparar los tiempos obtenidos para calcular la cantidad de cuadrados mágicos."*

        ---

        ### 1. **Demostración del número mágico**

        Un **cuadrado mágico de orden $n$** es una matriz $n \times n$ que contiene los números del $1$ al $n^2$, y en la cual todas las filas, columnas y diagonales suman lo mismo. A esta constante se la llama **número mágico** $M$.

        1. La suma total de los números del $1$ al $n^2$ es:

        $$
        S = 1 + 2 + \dots + n^2 = \frac{n^2(n^2+1)}{2}
        $$

        2. Esa suma $S$ está distribuida en las $n$ filas. Como cada fila debe sumar lo mismo (el número mágico $M$):

        $$
        n \cdot M = S
        $$

        3. Sustituyendo:

        $$
        n \cdot M = \frac{n^2(n^2+1)}{2}
        $$

        4. Dividiendo entre $n$:

        $$
        M = \frac{n(n^2+1)}{2} = \frac{n^3 + n}{2}
        $$

        ✅ Queda demostrado que el número mágico de un cuadrado de orden $n$ es siempre:

        $$
        M = \frac{n^3+n}{2}
        $$

## MaxiSubconjunto

Tengo que preguntar, ni idea.

## RutaMinima

Skip

## Palabras en cadena

1. 
$$PEC_{palab}(i, \ j, \ largo, \ acc, \ valida)=\begin{cases}
-1 \text{ , si j>largo y valido=0} \\
1 + acc \text{ , si j>largo y valido=1} \\
PEC_{palab}(j+1, \ j+2, \ largo, \ acc+1) \text{ , si \text{ , si palabra(palab[i] hasta palab[j])}} \\
PEC_{palab}(i, \ j+1, \ largo, \ acc+1) \text{ , c.c.} \\
\end{cases}
$$
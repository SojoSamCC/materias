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

# print(izquierdaDominante([8, 6, 7, 4, 5, 1, 3, 2]))
#print(izquierdaDominante([8, 4, 7, 6, 5, 1, 3, 2]))

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

# print(indiceEspejo([-4,-1,2,4,7]))
# print(indiceEspejo([0,2,3,4,7]))

def potenciaLogaritmica(n:int, exponente:int)->int:

    # Conquer
    if exponente==1:
        return n
    
    # Dividir
    if exponente % 2 == 0:
        potencia= potenciaLogaritmica(n=n, exponente=exponente/2)

        # Combinar
        return potencia * potencia
    else:
        potencia= potenciaLogaritmica(n=n, exponente=exponente-1)

        # Combinar
        return n * potencia

# print(potenciaLogaritmica(2,4))

def maximoMontana(array: list[int])->int:
    largo = len(array)

    # Dividir
    indice_actual = largo // 2
    
    indice_izquierda = indice_actual-1
    indice_derecha = indice_actual+1

    # Combinar
    el_maximo_es_uno_de_los_bordes: bool = indice_derecha >= largo or (indice_izquierda<0)
    if el_maximo_es_uno_de_los_bordes:
        return array[indice_actual]
    
    # Combinar
    soy_el_maximo: bool = (array[indice_izquierda] < array[indice_actual]) and (array[indice_derecha] < array[indice_actual])
    if soy_el_maximo:
        return array[indice_actual]
    
    # Conquistar
    debo_ir_a_la_izquierda: bool = array[indice_izquierda] > array[indice_actual] and array[indice_derecha] < array[indice_actual]
    if debo_ir_a_la_izquierda:
        new_array=array[:indice_actual]
        return maximoMontana(array=new_array)
    else:
        new_array=array[indice_actual+1:]
        return maximoMontana(array=new_array)
    
# print(maximoMontana([-1,3,8,22,30,22,8,4,2,1]))

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

# print(maximaSubsecuencia([3,-1, 4, 8,-2, 2,-7, 5]))
# print(maximaSubsecuencia([-2, 2,7, 5,3,1, -4, 8]))

def potenciaSum(matriz, exponente:int):

    if exponente == 1:
        return matriz

    # Divide
    logaritmo_en_base_dos_exponente:int = exponente // 2

    # Conquer
    potencia_izquierda = potenciaSum(matriz=matriz, exponente=logaritmo_en_base_dos_exponente)

    # DESCOMENTAR ESTA LINEA E IMPLEMENTAR LAS FUNCIONES QUE FALTAN PARA PODER TESTEAR LA FUNCIÓN producto_de_las_dos_matrices_que_ya_conocia= producto_matricial(potencia_izquierda, potencia(matriz=matriz, exponente=logaritmo_en_base_dos_exponente)

    # Combine
    # DESCOMENTAR ESTA LINEA E IMPLEMENTAR LAS FUNCIONES QUE FALTAN PARA PODER TESTEAR LA FUNCIÓN return suma_matricial(potencia_izquierda, producto_de_las_dos_matrices_que_ya_conocia))

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

# print(desordenSort([1,3,2,4,4,1,5,3]))

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
    """
    Descomentar estas lineas en caso de querer testear
    """
    # hay_false:bool = conjuncionSubmatriz(i_0, i_1, j_0, j_1)

    # if hay_false:
    #     return cazacazadorDeFalsos(matriz=matriz, cuarto=i_1+1, i=i_0, j=j_0)
    # else:
    #     if j_0+1 + cuarto >= largo:
    #         i_0+=cuarto
    #         j_0-=cuarto
    #     else:
    #         j_0+=cuarto
    #     return cazacazadorDeFalsos(matriz, cuarto=cuarto+1, i=i_0, j=j_0)
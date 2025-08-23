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
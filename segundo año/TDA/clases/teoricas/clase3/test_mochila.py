import random

def generar_listas(cant_listas: int, maximo_parametro: int)->tuple[list[int], list [int]]:

    lista_pesos = []
    lista_beneficios = []

    for i in range(cant_listas):
        lista_pesos.append(random.randint(1, maximo_parametro))
        lista_beneficios.append(random.randint(0, maximo_parametro))

    return lista_pesos, lista_beneficios

def mochila(pesos: list[int], beneficios: list[int], capacidad: int):
    
    if len(pesos) == 0 or capacidad==0:
        return 0

    if pesos[0] > capacidad:
        return mochila(pesos[1:], beneficios[1:], capacidad)
    
    pongo_el_objeto = mochila(pesos[1:], beneficios[1:], capacidad-pesos[0]) + beneficios[0]
    no_pongo_el_objeto = mochila(pesos[1:], beneficios[1:], capacidad)

    el_mejor = max(pongo_el_objeto, no_pongo_el_objeto)

    return el_mejor

def mochila_fraccionaria(pesos: list[int], beneficios: list[int], capacidad: int)->int:
    lista_beneficio_por_peso = [(beneficios[i] / pesos[i], i) for i in range(len(pesos))]
    lista_beneficio_por_peso = sorted(lista_beneficio_por_peso, key=lambda tupla: tupla[0])

    beneficio_acumulado= 0
    for i in range(len(lista_beneficio_por_peso)-1, -1, -1):
        beneficio = lista_beneficio_por_peso[i][0]
        indice_en_lista_pesos = lista_beneficio_por_peso[i][1]
        if capacidad<=0:
            return beneficio_acumulado
        if pesos[indice_en_lista_pesos] <= capacidad:
            capacidad -= pesos[indice_en_lista_pesos]
            beneficio_acumulado += beneficio
    return beneficio_acumulado

def testear(cant_test:int , cant_listas: int, maximo_parametro: int):

    cant_contraejemplos = 0
    for i in range(cant_test):
        
        lista_pesos, lista_beneficios = generar_listas(cant_listas, maximo_parametro)

        maxima_capacidad = random.randint(0,maximo_parametro)

        correcto = mochila(lista_pesos, lista_beneficios, maxima_capacidad)
        tal_vez= mochila_fraccionaria(lista_pesos, lista_beneficios, maxima_capacidad)

        if correcto != tal_vez:

            print("\nSe encontró un contraejemplo\n")
            print(f"Correcto: {correcto}")
            print(f"Obtenido: {tal_vez}\n")
            print(f"Lista pesos: {lista_pesos}")
            print(f"Lista beneficios: {lista_beneficios}")
    
            cant_contraejemplos+=1
    
    print(f"cantidad de contrajemplos: {cant_contraejemplos}")
if __name__ == "__main__":
    testear(1000, 40, 100)

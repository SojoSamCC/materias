def mochila(pesos: list[int], beneficios: list[int], capacidad: int):
    
    if len(pesos) == 0 or capacidad==0:
        return 0

    if pesos[0] > capacidad:
        return mochila(pesos[1:], beneficios[1:], capacidad)
    
    pongo_el_objeto = mochila(pesos[1:], beneficios[1:], capacidad-pesos[0]) + beneficios[0]
    no_pongo_el_objeto = mochila(pesos[1:], beneficios[1:], capacidad)

    el_mejor = max(pongo_el_objeto, no_pongo_el_objeto)

    return el_mejor

pesos = [5, 3, 2, 5, 3, 1, 10]
beneficios = [15, 5, 6, 2, 5, 2, 12]
# print(mochila(pesos, beneficios, 1))


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

# print(mochila_fraccionaria(pesos, beneficios, 40))

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

# actividades = [[9, 11], [10,12], [8, 9], [8,15], [11,13]]

# print(fuerza_bruta(actividades))

def seleccion_de_actividades_greedy(actividades: list[int, int])->list[int,int]:

    actividades = sorted(actividades, key=lambda actividad: actividad[1]) # esta vaina me ordena la lista segun la segunda componente de cada sublista

    cant_actividades= 0
    fin_ultima_actividad = actividades[0][1]
    for i in range(len(actividades)):
        principio, fin_nueva_actividad = actividades[i]
        if principio >= fin_ultima_actividad:
            cant_actividades += 1
    
    return cant_actividades

actividades = [[9, 11], [10,12], [8, 9], [8,15], [11,13]]

print(seleccion_de_actividades_greedy(actividades))
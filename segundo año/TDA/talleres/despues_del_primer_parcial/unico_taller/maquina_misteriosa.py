from collections import deque

n, m = tuple(map(int, input().split(" ")))

"""
Hago la implementación con BFS medio modificado porque así evalúo todos los caminos posibles de forma 
pareja hasta encontrar a m. 
Lo tuve que modificar porque no tengo el grafo completo como entrada y de paso quiero detener 
la ejecución apenas encuentre a m.

"""

grafito:set = set()
cola:deque = deque([(n, 0,)])

while True: # Lo hago así porque tengo como requiere que los test tienen solución y me parece que va un poco más rápido.
    
    nodo_actual, pasos = cola.popleft()

    if nodo_actual == m:
        print(pasos)
        break

    if nodo_actual not in grafito:
        grafito.add(nodo_actual)
        
        menos_uno:int = nodo_actual-1
        if menos_uno >= 0 and menos_uno not in grafito:
            cola.append((menos_uno, pasos+1))
        
        por_dos:int = nodo_actual*2
        if por_dos <= m*2 and por_dos not in grafito:
            cola.append((por_dos, pasos+1))
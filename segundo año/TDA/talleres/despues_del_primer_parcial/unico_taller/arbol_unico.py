from heapq import heappush, heappop
from collections import defaultdict

"""
Inicializo variables
"""

aristas_ordenadas = []                      # O(1)
grafito_original = defaultdict(list)        # O(1)

n, m = tuple(map(int, input().split(" ")))
for _ in range(m):                          # O(m) * O(log m) = O(m log m)
    u, v, w = tuple(map(int, input().split(" ")))
    grafito_original[u].append((w, v))      # O(1)
    grafito_original[v].append((w, u))      # O(1)
    heappush(aristas_ordenadas, (w, u, v))  # O(log m)

aristas_ordenadas = [heappop(aristas_ordenadas) for _ in range(len(aristas_ordenadas))] # O(m log m)

"""
Disjoint Set
"""

representantes = [i for i in range(n+1)]
size = [1 for _ in range(n+1)]

def find_set(nodo):
    if representantes[nodo] == nodo:
        return nodo
    representantes[nodo] = find_set(representantes[nodo])
    return representantes[nodo]

def union(u, v):
    u, v = (find_set(u), find_set(v))
    if u != v:
        if size[u] < size[v]:
            u, v = v, u

        representantes[v] = u
        size[u] += size[v]
        return True # esto me sirve para saber si efectivamente hice union o no.
    return False

"""
Kruskal modificado idea: acumular #aristas_AGM que no usé Y QUE COMPARTEN PESO CON UNA DEL AGM EN LA MISMA COMPONENETE CONEXA Y QUE UNEN CON OTRA COMPONENTE CONEXA Y QUE PODÍAN REEMPLAZAR A LA DEL AGM ORIGINAL.
"""

cant_agm_diferentes = 0

i = 0
while i < m:
    arista = aristas_ordenadas[i]
    w_original, _, _ = arista
    aristas_del_mismo_peso = []
    while i < m and aristas_ordenadas[i][0] == w_original: # veo qué aristas comparten el mismo peso.
        aristas_del_mismo_peso.append(aristas_ordenadas[i])
        i+=1
    
    aristas_que_unen_subarboles = []
    for arista in aristas_del_mismo_peso: # me fijo si las aristas que comparten el mismo peso me podrían unir con otra componente conexa.
        _, u, v = arista
        if find_set(u) != find_set(v):
            aristas_que_unen_subarboles.append(arista)
            cant_agm_diferentes += 1 # si la arista me podía unir componentes conexas diferentes, me sirve.
        # no me importa si comparten componente conexa porque más abajo me encargo de seleccionar a una en la union y solo acumular las que no usé.

    for _, u, v in aristas_que_unen_subarboles:
        if union(u, v):
            cant_agm_diferentes -=1 # si usé una arista para unir componentes conexas => no la cuento más.

# hasta este punto solo deberían quedarme acumuladas la cantidad de aristas que me generaban nuevos AGMs y que no usé, que es equivalente a la cantidad de AGMs diferentes que habían!!!

"""
Por favor que sea esto
"""
print(cant_agm_diferentes)

# 8 10
# 1 2 3
# 1 3 2
# 1 4 2
# 2 5 4
# 2 6 7
# 2 7 5
# 7 8 4
# 6 7 4
# 5 8 6
# 3 5 3

# 1 0
# 1

# 1 2 3
# 1 3 2
# 1 4 2
# 2 5 4
# 2 6 7
# 2 7 5
# 7 8 4
# 6 7 4
# 5 8 6
# 3 5 3
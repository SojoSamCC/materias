from pprint import pprint
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

"""
Kruskal
"""

peso_AGM = 0
aristas_fuera_del_agm = {}
grafito_kruskal = defaultdict(list)
for w, u, v in aristas_ordenadas:
    if find_set(u) != find_set(v):
        union(u, v)
        grafito_kruskal[u].append((w, v))
        grafito_kruskal[v].append((w, u))
    else:
        aristas_fuera_del_agm[(u, v)] = w

"""
Necesito encontrar la arista máxima entre dos nodos para todo nodo en el grafo original.
"""

"""
La idea es hacer DFS desde cada nodo pero acordandome de los nodos por los que ya pasé.
"""

arista_maxima_entre_nodos = {}
arista_maxima_entre_nodos_u = [0]*n
def dfs(u, padre):
    for w, v in grafito_kruskal[u]:
        if v != padre and (v, u) not in arista_maxima_entre_nodos:
            nueva_maxima = max(w, arista_maxima_entre_nodos_u[u-1])
            arista_maxima_entre_nodos_u[v-1] = nueva_maxima
            arista_maxima_entre_nodos[(u, v)] =  arista_maxima_entre_nodos_u[v-1]
            arista_maxima_entre_nodos[(v, u)] =  arista_maxima_entre_nodos_u[v-1]
            # print()
            # print(u, v)
            # input(nueva_maxima)
            dfs(v, u)

for u in grafito_kruskal:
    dfs(u, -1)

pprint(arista_maxima_entre_nodos, indent=2)
input()

"""
Me fijo si para cada arista fuera del AGM había una arista que: me conectara los mismos nodos en algun camino, y que tuviera el mismo peso en el grafo original.
"""

cant_aristas_fuera_del_agm = 0
for arista in aristas_fuera_del_agm:
    u, v = arista
    peso = aristas_fuera_del_agm[arista]
    arista_max_entre_u_v = max(arista_maxima_entre_nodos[u-1], arista_maxima_entre_nodos[v-1])
    if arista_max_entre_u_v == peso:
        cant_aristas_fuera_del_agm +=1

"""
Por favor que sea esto
"""
print(cant_aristas_fuera_del_agm)

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
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
# print(grafito_original)
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

# print(grafito_kruskal)
# print(aristas_fuera_del_agm)
"""
Árbol único
"""
# arista_maxima_entre_nodos = {u:{} for u in grafito_kruskal}
# # def dfs(u, nodo_hasta, arista_maxima_actual):
# #     if u == nodo_hasta:
# #         return arista_maxima_actual
# #     for w, v in grafito_kruskal[u]:
# #         nueva_maxima = max(w, arista_maxima_actual)
# #         nuevo_peso = dfs(v, nodo_hasta,  nueva_maxima)
# #         arista_maxima_entre_nodos[u][nodo_hasta] = max(nueva_maxima, nuevo_peso)
# ancestro = 4
# def dfs(u, padre):
#     for w, v in grafito_kruskal[u]:
#         if v != padre:
#             nueva_maxima = max(w, arista_maxima_entre_nodos[ancestro][u])
#             # arista_maxima_entre_nodos[u][v] = nueva_maxima
#             # input(f"\nu= {u}, v={v}, padre={padre}")
#             arista_maxima_entre_nodos[ancestro][v] = nueva_maxima
#             dfs(v, u)

# arista_maxima_entre_nodos[ancestro][ancestro] = 0
# dfs(ancestro, ancestro)

# pprint(arista_maxima_entre_nodos, indent=2)
arista_maxima_entre_nodos = [0]*(n)
def dfs(u, padre):
    for w, v in grafito_kruskal[u]:
        if v != padre:
            nueva_maxima = max(w, arista_maxima_entre_nodos[u-1])
            arista_maxima_entre_nodos[v-1] = nueva_maxima
            dfs(v, u)

ancestro = 1
dfs(ancestro, ancestro)

# pprint(arista_maxima_entre_nodos, indent=2)
# pprint([i+1 for i in range(n)], indent=2)

cant_aristas_fuera_del_agm = 0
for arista in aristas_fuera_del_agm:
    u, v = arista
    peso = aristas_fuera_del_agm[arista]
    max_entre_u_v = max(arista_maxima_entre_nodos[u-1], arista_maxima_entre_nodos[v-1]) 
    if max_entre_u_v == peso:
        cant_aristas_fuera_del_agm +=1
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
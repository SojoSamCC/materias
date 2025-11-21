import random
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# --- Configuración ---
n_random = 10
STEP_MODE = "enter"   # "enter" o "click"

# --- Crear aristas aleatorias (sin self-loops) ---
edges = []
for i in range(n_random):
    nodo = str(i)
    otro_nodo = i
    while otro_nodo == i:
        otro_nodo = random.randint(0, n_random)
    otro_nodo = str(otro_nodo)
    edges.append((nodo, otro_nodo))

# --- Construir el grafo y asegurarnos de que todos los nodos existan ---
G = nx.Graph()
G.add_nodes_from([str(i) for i in range(n_random)])
G.add_edges_from(edges)

# --- Layout fijo ---
pos = nx.spring_layout(G, seed=42)
visited = set()

# --- Preparar figura ---
fig, ax = plt.subplots(figsize=(8, 6))
plt.ion()

def draw(highlight=None, queue=None):
    ax.clear()
    colors = []
    for node in G.nodes():
        if node in visited:
            colors.append("lightgreen")
        elif node == highlight:
            colors.append("orange")
        else:
            colors.append("lightgray")
    nx.draw(G, pos=pos, ax=ax, with_labels=True, node_color=colors, node_size=700)
    title = f"Visitados: {', '.join(sorted(visited))}" if visited else "Visitados: (ninguno)"
    if queue:
        title += f"\nCola: {list(queue)}"
    ax.set_title(title)
    fig.canvas.draw()
    plt.pause(0.001)

def wait_step():
    if STEP_MODE == "enter":
        try:
            s = input("Presiona Enter para continuar, 'q' + Enter para salir: ")
            if s.strip().lower() == "q":
                raise KeyboardInterrupt
        except (KeyboardInterrupt, EOFError):
            raise
    else:
        print("Presiona tecla o haz clic dentro de la figura para continuar...")
        plt.waitforbuttonpress()

def bfs(start):
    queue = deque([start])
    visited.add(start)
    draw(highlight=start, queue=queue)
    wait_step()
    while queue:
        node = queue.popleft()
        draw(highlight=node, queue=queue)
        wait_step()
        for neigh in G.neighbors(node):
            if neigh not in visited:
                visited.add(neigh)
                queue.append(neigh)
                draw(highlight=neigh, queue=queue)
                wait_step()

# --- Ejecutar BFS en todas las componentes ---
try:
    draw()
    for node in G.nodes():
        if node not in visited:
            print(f"Iniciando BFS desde nodo {node}")
            bfs(node)
    print("BFS completado.")
except KeyboardInterrupt:
    print("\nSimulación interrumpida por el usuario.")
finally:
    plt.ioff()
    plt.show()

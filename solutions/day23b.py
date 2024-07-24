import networkx as nx
import numpy as np

m = np.genfromtxt("day23input.txt", dtype=bytes, comments=None, delimiter=1).astype(str)
G = nx.Graph()
for idx, val in np.ndenumerate(m):
    if val != "#":
        target = idx
        neighbor = (idx[0] - 1, idx[1])
        if neighbor[0] >= 0 and m[neighbor] != "#":
            G.add_edge(idx, neighbor, weight=1)
        neighbor = (idx[0] + 1, idx[1])
        if neighbor[0] < m.shape[0] and m[neighbor] != "#":
            G.add_edge(idx, neighbor, weight=1)
        neighbor = (idx[0], idx[1] - 1)
        if neighbor[1] >= 0 and m[neighbor] != "#":
            G.add_edge(idx, neighbor, weight=1)
        neighbor = (idx[0], idx[1] + 1)
        if neighbor[1] < m.shape[1] and m[neighbor] != "#":
            G.add_edge(idx, neighbor, weight=1)

for node, degree in list(G.degree()):
    if degree == 2:
        neighbors = G.neighbors(node)
        n = list(G.neighbors(node))
        weight = nx.path_weight(G, [n[0], node, n[1]], "weight")
        G.remove_node(node)
        G.add_edge(*neighbors, weight=weight)

best = 0
for path in nx.all_simple_paths(G, (0, 1), target):
    best = max(best, nx.path_weight(G, path, "weight"))

# Runtime ~45s on a Mac M3
print(best)

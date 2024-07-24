import networkx as nx
import numpy as np

m = np.genfromtxt("day23input.txt", dtype=bytes, comments=None, delimiter=1).astype(str)
G = nx.DiGraph()
for idx, val in np.ndenumerate(m):
    if val == ".":
        target = idx
    if val in [".", "^"]:
        neighbor = (idx[0] - 1, idx[1])
        if neighbor[0] >= 0 and m[neighbor] != "#":
            G.add_edge(idx, neighbor)
    if val in [".", "v"]:
        neighbor = (idx[0] + 1, idx[1])
        if neighbor[0] < m.shape[0] and m[neighbor] != "#":
            G.add_edge(idx, neighbor)
    if val in [".", "<"]:
        neighbor = (idx[0], idx[1] - 1)
        if neighbor[1] >= 0 and m[neighbor] != "#":
            G.add_edge(idx, neighbor)
    if val in [".", ">"]:
        neighbor = (idx[0], idx[1] + 1)
        if neighbor[1] < m.shape[1] and m[neighbor] != "#":
            G.add_edge(idx, neighbor)

print(max([len(path) - 1 for path in nx.all_simple_paths(G, (0, 1), target)]))

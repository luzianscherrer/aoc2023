import pandas as pd
import numpy as np
import networkx as nx

con = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(0, -1), (1, 0)],
    "F": [(1, 0), (0, 1)],
}

m = np.pad(
    pd.read_csv("day10input.txt", header=None, sep="\s*", engine="python")
    .iloc[:, 1:-1]
    .to_numpy(),
    pad_width=1,
    constant_values=".",
)

G = nx.DiGraph()
for r in range(m.shape[0]):
    for c in range(m.shape[1]):
        nodeid = r * m.shape[1] + c
        if m[r, c] == "S":
            start = nodeid
        elif m[r, c] != ".":
            edges = [(nodeid, t[0] * m.shape[1] + nodeid + t[1]) for t in con[m[r, c]]]
            G.add_edges_from(edges)

neighbors = list(G.in_edges(start))
G.add_edge(start, neighbors[0][0])
path = nx.shortest_path(G, start, neighbors[1][0])
print(len(path) // 2)

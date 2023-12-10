import pandas as pd
import numpy as np
import networkx as nx
from skimage.segmentation import flood_fill

con = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(0, -1), (1, 0)],
    "F": [(1, 0), (0, 1)],
}
ext = {
    "L": [[0, 1, 0], [0, 1, 1], [0, 0, 0]],
    "J": [[0, 1, 0], [1, 1, 0], [0, 0, 0]],
    "7": [[0, 0, 0], [1, 1, 0], [0, 1, 0]],
    "F": [[0, 0, 0], [0, 1, 1], [0, 1, 0]],
    "|": [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
    "-": [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
    "S": [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    ".": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
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

mask = np.zeros(np.array(m.shape) * 3, dtype=int)
for nodeid in path:
    r = nodeid // m.shape[1]
    c = nodeid % m.shape[1]
    mask[r * 3 : r * 3 + 3, c * 3 : c * 3 + 3] = ext[m[r, c]]

fill = flood_fill(mask, (0, 0), 1)
res = 0
for r in range(m.shape[0]):
    for c in range(m.shape[1]):
        check = fill[r * 3 : r * 3 + 3, c * 3 : c * 3 + 3]
        if not check.any():
            res += 1
print(res)

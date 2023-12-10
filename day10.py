import pandas as pd, numpy as np, networkx as nx

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
for r in range(1, m.shape[0] - 1):
    for c in range(1, m.shape[1] - 1):
        nodeid = r * m.shape[0] + c
        if m[r, c] == "S":
            start = nodeid
        elif m[r, c] != ".":
            edges = [(nodeid, t[0] * m.shape[0] + nodeid + t[1]) for t in con[m[r, c]]]
            G.add_edges_from(edges)

G.add_edges_from([(edge[1], edge[0]) for edge in G.in_edges(start)])
target = list(G.edges(start))[0][1]
G.remove_edge(start, target)
path = nx.shortest_path(G, start, target)
print(len(path) // 2)

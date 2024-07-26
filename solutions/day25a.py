import networkx as nx
from itertools import combinations

filename = "day25example.txt"
with open(filename, "r") as file:
    lines = [line.replace(":", "").rstrip() for line in file]

G = nx.parse_adjlist(lines)
for edges in combinations(G.edges, 3):
    for edge in edges:
        G.remove_edge(*edge)
    if nx.number_connected_components(G) == 2:
        print(
            (len(nx.descendants(G, edge[0])) + 1)
            * (len(nx.descendants(G, edge[1])) + 1)
        )
        break
    for edge in edges:
        G.add_edge(*edge)

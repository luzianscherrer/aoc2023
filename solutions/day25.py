import networkx as nx

with open("day25input.txt", "r") as file:
    lines = [line.replace(":", "").rstrip() for line in file]

G = nx.parse_adjlist(lines)
_, partition = nx.stoer_wagner(G)
print(len(partition[0]) * len(partition[1]))

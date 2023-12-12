import numpy as np
from itertools import combinations

with open("day11input.txt", "r") as file:
    data = file.readlines()

m = np.zeros((len(data), len(data[0]) - 1))
for i, line in enumerate(data):
    m[i] = [char == "#" for char in line.strip()]

h = m.sum(axis=0) == 0
v = m.sum(axis=1) == 0

nodes = []
rp = 0
for r in range(m.shape[0]):
    if v[r]:
        rp += 1000000 - 1
    cp = 0
    for c in range(m.shape[1]):
        if h[c]:
            cp += 1000000 - 1
        if m[r, c]:
            nodes.append((rp, cp))
        cp += 1
    rp += 1

nodes = np.array(nodes)

print(int(sum([np.linalg.norm(p[0] - p[1], 1) for p in combinations(nodes, 2)])))

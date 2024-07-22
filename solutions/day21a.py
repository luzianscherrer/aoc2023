import numpy as np

m = np.genfromtxt("day21input.txt", dtype=bytes, comments=None, delimiter=1).astype(str)
m[m == "S"] = "O"


def step(m):
    for coord in np.transpose((m == "O").nonzero()):
        if coord[0] - 1 >= 0 and m[coord[0] - 1, coord[1]] != "#":
            m[coord[0] - 1, coord[1]] = "O"
        if coord[0] + 1 < m.shape[0] and m[coord[0] + 1, coord[1]] != "#":
            m[coord[0] + 1, coord[1]] = "O"
        if coord[1] - 1 >= 0 and m[coord[0], coord[1] - 1] != "#":
            m[coord[0], coord[1] - 1] = "O"
        if coord[1] + 1 < m.shape[1] and m[coord[0], coord[1] + 1] != "#":
            m[coord[0], coord[1] + 1] = "O"
        m[*coord] = "."


for i in range(64):
    step(m)
print((m == "O").sum())

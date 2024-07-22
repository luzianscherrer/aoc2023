import numpy as np

steps = 26501365
m = np.genfromtxt("day21input.txt", dtype=bytes, comments=None, delimiter=1).astype(str)
m[m == "S"] = "O"


def cut_copy(m, dist, frm, to):
    start = (m.shape[0] // 2, m.shape[0] // 2)
    n = m.copy()
    for idx, val in np.ndenumerate(n):
        if val == frm and abs(idx[0] - start[0]) + abs(idx[1] - start[1]) <= dist:
            n[idx] = to
    return n


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


for i in range(m.shape[0]):
    step(m)
full_first = int((m == "O").sum())
center_dist = m.shape[0] // 2
n = cut_copy(m, center_dist, "O", ".")
corner_first = int((n == "O").sum())

step(m)
full_second = int((m == "O").sum())
n = cut_copy(m, center_dist, "O", ".")
corner_second = int((n == "O").sum())

size = steps // m.shape[0]
print(
    (size + 1) ** 2 * full_first
    + size**2 * full_second
    - (size + 1) * corner_first
    + size * corner_second
)

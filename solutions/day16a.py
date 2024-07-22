import numpy as np

m = np.pad(
    np.genfromtxt("day16input.txt", dtype=bytes, comments=None, delimiter=1).astype(
        str
    ),
    1,
    constant_values="#",
)
m[1, 0] = "S"
ena = np.zeros_like(m, dtype=np.uint8)
vis = {}

q = [np.array([[1, 0], [0, 1]])]

while len(q):
    pos = q.pop()
    if m[tuple(pos[0])] != "#" and tuple(pos[1]) not in vis.get(tuple(pos[0]), []):
        ena[tuple(pos[0])] = 1

        v = vis.get(tuple(pos[0]), [])
        v.append(tuple(pos[1]))
        vis[tuple(pos[0])] = v

        nxtpos = pos[0] + pos[1]
        nxtsym = m[tuple(nxtpos)]
        if nxtsym == ".":
            q.append(np.array([nxtpos, pos[1]]))
        elif nxtsym == "|":
            if pos[1, 0] == 0:
                q.append(np.array([nxtpos, np.array([-1, 0])]))
                q.append(np.array([nxtpos, np.array([1, 0])]))
            else:
                q.append(np.array([nxtpos, pos[1]]))
        elif nxtsym == "-":
            if pos[1, 1] == 0:
                q.append(np.array([nxtpos, np.array([0, -1])]))
                q.append(np.array([nxtpos, np.array([0, 1])]))
            else:
                q.append(np.array([nxtpos, pos[1]]))
        elif nxtsym == "/":
            q.append(np.array([nxtpos, np.flip(pos[1]) * -1]))
        elif nxtsym == "\\":
            q.append(np.array([nxtpos, np.flip(pos[1])]))

print(np.count_nonzero(ena) - 1)

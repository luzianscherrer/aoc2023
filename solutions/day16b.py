import numpy as np

field = np.pad(
    np.genfromtxt("day16input.txt", dtype=bytes, comments=None, delimiter=1).astype(
        str
    ),
    1,
    constant_values="#",
)


def find_enabled(field, startpos, startdir):
    m = np.copy(field)
    m[tuple(startpos)] = "S"
    ena = np.zeros_like(m, dtype=np.uint8)
    vis = {}
    q = [np.array([startpos, startdir])]

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

    return np.count_nonzero(ena) - 1


opt = 0
for i in range(1, field.shape[0] - 1):
    opt = max(opt, find_enabled(field, [i, 0], [0, 1]))
for i in range(1, field.shape[0] - 1):
    opt = max(opt, find_enabled(field, [i, -1], [0, -1]))
for i in range(1, field.shape[1] - 1):
    opt = max(opt, find_enabled(field, [0, i], [1, 0]))
for i in range(1, field.shape[1] - 1):
    opt = max(opt, find_enabled(field, [-1, i], [-1, 0]))
print(opt)

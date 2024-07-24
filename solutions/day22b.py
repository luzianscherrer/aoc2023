import numpy as np
import pandas as pd

input = pd.read_csv(
    "day22input.txt", sep=r",|~", engine="python", header=None
).to_numpy()
m = np.zeros([input[:, [i, i + 3]].max() + 1 for i in range(3)], dtype=int)

m[:, :, 0] = -1

for i, coords in enumerate(input):
    m[
        coords[0] : coords[3] + 1,
        coords[1] : coords[4] + 1,
        coords[2] : coords[5] + 1,
    ] = i + 1


def fall(m, exclude_idx=None):
    falling = set()
    stable = False
    while not stable:
        stable = True
        for i in range(1, m.max() + 1):
            if exclude_idx and exclude_idx == i:
                continue
            element = m == i
            m[m == i] = 0
            stack = m != 0
            check = element.sum() + stack.sum()
            for _ in range(m.shape[2]):
                candidate = np.roll(element, -1, axis=2)
                if (candidate + stack).sum() != check:
                    break
                element = candidate
                stable = False
                falling.add(i)
            m[element] = i
    return len(falling)


fall(m)
total = 0
for i in range(1, m.max() + 1):
    n = m.copy()
    n[n == i] = 0
    total += fall(n, exclude_idx=i)

# Runtime ~450s on a Mac M3
print(total)

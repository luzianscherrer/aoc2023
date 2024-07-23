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

stable = False
while not stable:
    stable = True
    for i in range(1, m.max() + 1):
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
        m[element] = i


def is_stable(m, removed_idx):
    for i in range(1, m.max() + 1):
        if i == removed_idx:
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
            return False
        m[element] = i
    return True


removals = 0
for i in range(1, m.max() + 1):
    n = m.copy()
    n[n == i] = 0
    if is_stable(n, i):
        removals += 1

# runtime ~2.5 mins on an old intel mac
print(removals)

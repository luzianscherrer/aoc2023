import numpy as np


def mirrorpos(arr, axis=0):
    m = np.array(arr, dtype=int)
    if axis == 1:
        m = m.T
    for i in range(m.shape[0] - 1):
        upper_flipped = np.flip(m[: i + 1], axis=0)
        lower = m[i + 1 :]
        rows = min(upper_flipped.shape[0], lower.shape[0])
        if np.array_equal(upper_flipped[:rows], lower[:rows]):
            return i + 1
    return 0


with open("day13input.txt", "r") as file:
    data = file.readlines()
total = 0
arr = []
for line in data:
    row = [*line.strip().replace(".", "0").replace("#", "1")]
    if len(row) == 0:
        total += 100 * mirrorpos(arr, axis=0) + mirrorpos(arr, axis=1)
        arr = []
    else:
        arr.append(row)
total += 100 * mirrorpos(arr, axis=0) + mirrorpos(arr, axis=1)
print(total)

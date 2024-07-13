import pandas as pd
import numpy as np
from skimage.segmentation import flood_fill

directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

df = pd.read_csv("day18input.txt", header=None, sep=" ", engine="python")

maxrow, minrow, maxcol, mincol, col, row = 0, 0, 0, 0, 0, 0
for i, entry in df.iterrows():
    if entry.iloc[0] == "R":
        col += entry.iloc[1]
        maxcol = max(maxcol, col)
    elif entry.iloc[0] == "L":
        col -= entry.iloc[1]
        mincol = min(mincol, col)
    elif entry.iloc[0] == "U":
        row -= entry.iloc[1]
        minrow = min(minrow, row)
    elif entry.iloc[0] == "D":
        row += entry.iloc[1]
        maxrow = max(maxrow, row)

m = np.zeros((abs(minrow) + maxrow + 1, abs(mincol) + maxcol + 1), dtype=np.uint8)
pos = (abs(minrow), abs(mincol))

m[pos] = 1
for i, entry in df.iterrows():
    for j in range(entry.iloc[1]):
        pos = tuple(np.array(pos) + np.array(directions[entry.iloc[0]]))
        m[pos] = 1

print(np.count_nonzero(flood_fill(m, (m.shape[0] // 2, m.shape[1] // 2), 1)))

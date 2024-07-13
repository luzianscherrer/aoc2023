import pandas as pd
import numpy as np

df = pd.read_csv("day18input.txt", header=None, sep=" ")

maxrow, minrow, maxcol, mincol, col, row = 0, 0, 0, 0, 0, 0
for i, entry in df.iterrows():
    dir = entry.iloc[2][-2]
    dist = int(entry.iloc[2][2:-2], 16)
    if dir == "0":
        col += dist
        maxcol = max(maxcol, col)
    elif dir == "2":
        col -= dist
        mincol = min(mincol, col)
    elif dir == "3":
        row -= dist
        minrow = min(minrow, row)
    elif dir == "1":
        row += dist
        maxrow = max(maxrow, row)

m = np.zeros((abs(minrow) + maxrow + 1, abs(mincol) + maxcol + 1), dtype=np.uint8)
pos = (abs(minrow), abs(mincol))

turns = [pos]
perimeter = 0
for i, entry in df.iterrows():
    length = int(entry.iloc[2][2:-2], 16)
    direction = int(entry.iloc[2][-2])
    if direction == 0:
        m[pos[0], pos[1] : length + 1] = 1
        pos = (pos[0], pos[1] + length)
        perimeter += length
    elif direction == 1:
        m[pos[0] : length + 1, pos[1]] = 1
        pos = (pos[0] + length, pos[1])
        perimeter += length
    elif direction == 2:
        m[pos[0], pos[1] - length : length + 1] = 1
        pos = (pos[0], pos[1] - length)
    elif direction == 3:
        m[pos[0] - length : length + 1, pos[1]] = 1
        pos = (pos[0] - length, pos[1])
    turns.append(pos)

turns = np.array(turns).reshape(-1, 2)
x = turns[:, 0]
y = turns[:, 1]
xs = np.sum(x * np.roll(y, -1))
ys = np.sum(y * np.roll(x, -1))

print(int(perimeter + 1 + 0.5 * np.abs(xs - ys)))

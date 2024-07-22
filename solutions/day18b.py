import pandas as pd
import numpy as np

df = pd.read_csv("day18input.txt", header=None, sep=" ")

pos = (0, 0)

turns = [pos]
perimeter = 0
for i, entry in df.iterrows():
    length = int(entry.iloc[2][2:-2], 16)
    direction = int(entry.iloc[2][-2])
    if direction == 0:
        pos = (pos[0], pos[1] + length)
        perimeter += length
    elif direction == 1:
        pos = (pos[0] + length, pos[1])
        perimeter += length
    elif direction == 2:
        pos = (pos[0], pos[1] - length)
    elif direction == 3:
        pos = (pos[0] - length, pos[1])
    turns.append(pos)

turns = np.array(turns).reshape(-1, 2)
x = turns[:, 0]
y = turns[:, 1]
xs = np.sum(x * np.roll(y, -1))
ys = np.sum(y * np.roll(x, -1))

print(int(perimeter + 1 + 0.5 * np.abs(xs - ys)))

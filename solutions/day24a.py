import pandas as pd
import numpy as np
from itertools import combinations

test = [200000000000000, 400000000000000]
m = pd.read_csv(
    "day24input.txt", sep=r", | @ ", engine="python", header=None
).to_numpy()
count = 0
for a, b in combinations(m, 2):
    res, _, rank = np.linalg.lstsq(
        np.array([a[3:5], -b[3:5]]).T, b[0:2] - a[0:2], rcond=None
    )[:3]
    if rank == 2:
        x, y = a[3:5] * res[0] + a[0:2]
        if (
            test[0] <= x <= test[1]
            and test[0] <= y <= test[1]
            and res[0] > 0
            and res[1] > 0
        ):
            count += 1
print(count)

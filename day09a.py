import pandas as pd
import numpy as np

m = pd.read_csv("day09input.txt", header=None, sep=" ").to_numpy()
sum = 0
while m.any():
    sum += np.sum(m[:, -1])
    m = np.diff(m, axis=1)
print(sum)

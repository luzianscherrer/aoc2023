import pandas as pd
import numpy as np

m = pd.read_csv("day09input.txt", header=None, sep=" ").to_numpy()
x = m[:, 0]
while m.any():
    m = np.diff(m, axis=1)
    x = np.vstack((x, m[:, 0]))
d = x[-1]
for i in reversed(range(x.shape[0])):
    d = x[i] - d
print(np.sum(d))

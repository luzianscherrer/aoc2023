import pandas as pd

df = pd.read_csv("day06input.txt", header=None, sep="\s+")
total = 1
for t, d in df.iloc[:, 1:].values.T:
    total *= sum([1 if i * (t - i) > d else 0 for i in range(1, t)])
print(total)

import pandas as pd
import numpy as np

df = pd.read_csv("day04input.txt", header=None, sep="\s+")
margin = (df.iloc[0, :] == "|").idxmax()
win = df.iloc[:, 2:margin].to_numpy()
card = df.iloc[:, margin + 1 :].to_numpy()
wins = np.array([np.sum(np.isin(win[i], card[i])) for i in range(win.shape[0])])

pile = [[wins[i]] for i in range(len(wins))]
for i, cs in enumerate(pile):
    for c in cs:
        for j in range(c):
            pile[i + j + 1].append(wins[i + j + 1])

print(len([i for sl in pile for i in sl]))

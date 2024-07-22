import pandas as pd
import numpy as np

df = pd.read_csv("day04input.txt", header=None, sep="\s+")
margin = (df.iloc[0, :] == "|").idxmax()
win = df.iloc[:, 2:margin].to_numpy()
card = df.iloc[:, margin + 1 :].to_numpy()
wins = np.array([np.sum(np.isin(win[i], card[i])) for i in range(win.shape[0])])

piles = np.ones(len(wins), dtype=int)
for i, cs in enumerate(piles):
    for w in range(wins[i]):
        piles[i + 1 + w] += cs

print(sum(piles))

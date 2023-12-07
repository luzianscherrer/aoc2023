import pandas as pd
import itertools

symbols = {"A": 0xE, "K": 0xD, "Q": 0xC, "J": 0x1, "T": 0xA}
values = {
    (5,): 0xF,
    (1, 4): 0xE,
    (2, 3): 0xD,
    (1, 1, 3): 0xC,
    (1, 2, 2): 0xB,
    (1, 1, 1, 2): 0xA,
    (1, 1, 1, 1, 1): 0x9,
}


def typescore(hand):
    cards = {}
    for c in hand:
        cards[c] = cards.get(c, 0) + 1
    return values[tuple(sorted(cards.values()))] << 20


def conv(hand):
    value = 0
    indexes = []
    for i, c in enumerate(hand):
        c == "J" and indexes.append(i)
    if len(indexes):
        best = 0
        for p in list(itertools.product("AKQT98765432", repeat=len(indexes))):
            pi = iter(p)
            test = ""
            for i, c in enumerate(hand):
                test += next(pi) if i in indexes else c
            score = typescore(test)
            best = max(score, best)
        value = best
    else:
        value = typescore(hand)
    for i, c in enumerate(hand[::-1]):
        value += int(symbols.get(c, c)) << i * 4
    return value


df = pd.read_csv("day07input.txt", header=None, sep=" ", converters={0: conv})
print(sum([v * (i + 1) for i, v in enumerate(df.sort_values(0)[1])]))

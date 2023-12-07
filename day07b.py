import pandas as pd
import itertools

symbols = {"A": 0xE, "K": 0xD, "Q": 0xC, "J": 0x1, "T": 0xA}


def typescore(hand):
    value = 0
    cards = {}
    for c in hand[::-1]:
        cards[c] = cards.get(c, 0) + 1
    if len(cards.keys()) == 1:
        value += 0xF00000
    elif len(cards.keys()) == 2:
        if list(cards.values())[0] in (1, 4):
            value += 0xE00000
        else:
            value += 0xD00000
    elif len(cards.keys()) == 4:
        value += 0xA00000
    elif len(cards.keys()) == 5:
        value += 0x900000
    elif list(cards.values())[0] == 2 or list(cards.values())[1] == 2:
        value += 0xB00000
    else:
        value += 0xC00000
    return value


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

import pandas as pd

symbols = {"A": 0xE, "K": 0xD, "Q": 0xC, "J": 0xB, "T": 0xA}


def conv(hand):
    value = 0
    cards = {}
    for i, c in enumerate(hand[::-1]):
        cards[c] = cards.get(c, 0) + 1
        value += int(symbols.get(c, c)) << i * 4
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


df = pd.read_csv("day07input.txt", header=None, sep=" ", converters={0: conv})
print(sum([v * (i + 1) for i, v in enumerate(df.sort_values(0)[1])]))

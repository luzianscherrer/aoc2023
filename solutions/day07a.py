import pandas as pd

symbols = {"A": 0xE, "K": 0xD, "Q": 0xC, "J": 0xB, "T": 0xA}
values = {
    (5,): 0xF,
    (1, 4): 0xE,
    (2, 3): 0xD,
    (1, 1, 3): 0xC,
    (1, 2, 2): 0xB,
    (1, 1, 1, 2): 0xA,
    (1, 1, 1, 1, 1): 0x9,
}


def conv(hand):
    value = 0
    cards = {}
    for i, c in enumerate(hand[::-1]):
        cards[c] = cards.get(c, 0) + 1
        value += int(symbols.get(c, c)) << i * 4
    value += values[tuple(sorted(cards.values()))] << 20
    return value


df = pd.read_csv("day07input.txt", header=None, sep=" ", converters={0: conv})
print(sum([v * (i + 1) for i, v in enumerate(df.sort_values(0)[1])]))

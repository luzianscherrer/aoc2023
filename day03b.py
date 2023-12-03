import re
import math

f = open("day03input.txt", "r")

numbers = [[]]
symbols = [[]]
for line in f.read().split("\n"):
    number = []
    symbol = []
    for match in re.finditer(r"\d+", line):
        number.append(match)
    for match in re.finditer(r"[*]", line):
        symbol.append(match)
    numbers.append(number)
    symbols.append(symbol)
numbers.append([])
symbols.append([])

total = 0
for si in range(len(symbols)):
    for symbol in symbols[si]:
        x1, x2 = symbol.span()
        matches = set()
        for number in [number for sl in numbers[si - 1 : si + 2] for number in sl]:
            y1, y2 = number.span()
            if max(x1, y1) <= min(x2, y2):
                matches.add(number)
        if len(matches) == 2:
            total += math.prod([int(i.group()) for i in matches])
print(total)

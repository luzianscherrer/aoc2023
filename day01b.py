import re

f = open("day01input.txt", "r")

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

values = []
p = re.compile(r"(?=(" + "|".join(numbers) + "|.))")
for line in f.read().split("\n"):
    matches = p.finditer(line)
    results = [match.group(1) for match in matches]
    lineprime = ""
    for token in results:
        if token in numbers:
            lineprime += numbers[token]
        else:
            lineprime += token
    lineprime = re.sub(r"[^\d]", "", lineprime)
    values.append(int(f"{lineprime[0]}{lineprime[-1]}"))
print(sum(values))

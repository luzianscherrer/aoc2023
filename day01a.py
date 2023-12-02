import re

f = open("day01input.txt", "r")

values = []
for line in f.read().split("\n"):
    line = re.sub(r"[^\d]", "", line)
    values.append(int(f"{line[0]}{line[-1]}"))
print(sum(values))

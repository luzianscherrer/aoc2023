import itertools, re

with open("day12input.txt", "r") as file:
    data = file.readlines()

total = 0
for line in data:
    pattern, setup = line.strip().split(" ")
    candidates = []

    parts = [int(x) for x in setup.split(",")]
    for part in parts:
        if len(candidates):
            candidates[-1] += "."
        candidates.append(f"{'#'*part}")

    patternre = pattern.replace(".", "\.").replace("?", ".")
    length = len(pattern) - sum(parts) + 1

    for x in itertools.combinations_with_replacement(range(length), len(candidates)):
        if len(set(x)) == len(candidates):
            checklist = ["."] * length
            for i, pos in enumerate(x):
                checklist[pos] = candidates[i]
            checkstr = "".join(checklist)
            if re.search(patternre, checkstr):
                total += 1
print(total)

with open("day05input.txt", "r") as file:
    data = file.readlines()

mappings = []
for i, line in enumerate(data):
    line = line.strip()
    if i == 0:
        seeds = [int(i) for i in line.split(": ")[1].split(" ")]
    elif i > 1:
        if line.endswith(":"):
            mappings.append([])
        elif len(line) > 0:
            mappings[-1].append([int(i) for i in line.split(" ")])

[m.sort(key=lambda x: x[1]) for m in mappings]

res = 2**32
for x in seeds:
    for typemappings in mappings:
        for mapping in typemappings:
            if x >= mapping[1] and x < mapping[1] + mapping[2]:
                x = x - mapping[1] + mapping[0]
                break
    res = min(x, res)
print(res)

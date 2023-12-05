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

res = 2**64
for s, o in zip(seeds[::2], seeds[1::2]):
    ranges = [(s, s + o - 1)]
    for typemappings in mappings:
        newranges = []
        for l, h in ranges:
            found = False
            for map in typemappings:
                if l >= map[1] and h < map[1] + map[2]:
                    newranges.append((l - map[1] + map[0], h - map[1] + map[0]))
                    found = True
                elif l < map[1] and h >= map[1] and h < map[1] + map[2]:
                    ranges.append((l, map[1] - 1))
                    newranges.append((map[0], map[0] + h - map[1]))
                    found = True
                elif l < map[1] + map[2] and h >= map[1] + map[2] and l >= map[1]:
                    ranges.append((map[1] + map[2], h))
                    newranges.append((map[0] + l - map[1], map[0] + map[2] - 1))
                    found = True
                elif l < map[1] and h >= map[1] + map[2]:
                    ranges.append((l, map[1] - 1))
                    newranges.append((map[0], map[0] + map[2] - 1))
                    ranges.append((map[1] + map[2], h))
                    found = True
                if found == True:
                    break
            if found == False:
                newranges.append((l, h))
        ranges = newranges.copy()
    res = min(res, min(ranges)[0])
print(res)

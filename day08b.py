import math, itertools, pandas as pd

filename = "day08input.txt"
with open(filename, "r") as file:
    instructions = [*file.readlines()[0].strip()]

df = pd.read_csv(
    filename,
    sep="[^A-Z]+",
    engine="python",
    index_col=0,
    skiprows=2,
    usecols=[0, 1, 2],
    names=["P", "L", "R"],
    header=None,
)


ends = []
for pos in df.loc[df.index.str.contains(r"..A")].index:
    for i, inst in enumerate(itertools.cycle(instructions)):
        pos = df.loc[pos][inst]
        if pos[2] == "Z":
            break
    ends.append(i + 1)
print(math.lcm(*ends))

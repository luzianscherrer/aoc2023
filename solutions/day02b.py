import numpy as np

f = open("day02input.txt", "r")

colors = ["red", "green", "blue"]

games = []
for line in f.read().split("\n"):
    _, reveals = line.split(":")
    game = []
    for reveal in reveals.split(";"):
        cubes = [0, 0, 0]
        for cube in reveal.split(","):
            for i, color in enumerate(colors):
                if cube.endswith(color):
                    cubes[i] = int(cube.split(" ")[1])
        game.append(cubes)
    games.append(game)

print(sum([np.prod(np.array(g).max(axis=0)) for g in games]))

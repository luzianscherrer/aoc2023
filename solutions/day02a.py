f = open("day02input.txt", "r")

limits = [12, 13, 14]
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

sum = 0
for i, game in enumerate(games):
    take = True
    for cubes in game:
        if cubes[0] > limits[0] or cubes[1] > limits[1] or cubes[2] > limits[2]:
            take = False
            break
    if take:
        sum += i + 1
print(sum)

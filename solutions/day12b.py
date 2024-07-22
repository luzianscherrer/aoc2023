import functools

with open("day12input.txt", "r") as file:
    data = file.readlines()

repetitions = 5


@functools.cache
def count(pattern, setup):
    if pattern == "":
        return len(setup) == 0
    if len(setup) == 0:
        return not "#" in pattern
    if pattern[0] == ".":
        return count(pattern[1:], setup)
    if pattern[0] == "#":
        length = setup[0]
        if (
            len(pattern) >= length
            and not "." in pattern[:length]
            and (len(pattern) == length or pattern[length] != "#")
        ):
            return count(pattern[length + 1 :], setup[1:])
        else:
            return 0
    if pattern[0] == "?":
        return count("#" + pattern[1:], setup) + count("." + pattern[1:], setup)


total = 0
for line in data:
    pattern, setup = line.strip().split(" ")
    pattern += "?"
    pattern *= repetitions
    pattern = pattern[:-1]

    setup = [int(i) for i in setup.split(",")]
    setup *= repetitions

    total += count(pattern, tuple(setup))
print(total)

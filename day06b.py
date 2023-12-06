import re

with open("day06input.txt", "r") as file:
    data = file.readlines()

t = int(re.sub("[^\d]", "", data[0]))
d = int(re.sub("[^\d]", "", data[1]))

print(sum([1 if i * (t - i) > d else 0 for i in range(1, t)]))

import re

with open("day06input.txt", "r") as file:
    data = file.readlines()

t, d = [int(re.sub("[^\d]", "", d)) for d in data]
print(sum([i * (t - i) > d for i in range(1, t)]))

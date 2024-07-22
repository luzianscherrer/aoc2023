with open("day15input.txt", "r") as file:
    data = file.read().split(",")

total = 0
for element in data:
    value = 0
    for part in [*element]:
        value = ((value + ord(part)) * 17) % 256
    total += value
print(total)

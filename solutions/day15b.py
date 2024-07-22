with open("day15input.txt", "r") as file:
    data = file.read().split(",")

boxes = {}
for element in data:
    if "=" in element:
        label, lens = element.split("=")
        lens = int(lens)
        operation = "="
    else:
        operation = "-"
        label = element[:-1]
    box = 0
    for part in [*label]:
        box = ((box + ord(part)) * 17) % 256

    currentbox = boxes.get(box, [])
    if operation == "=":
        idx = next(
            filter(lambda i: currentbox[i][0] == label, range(len(currentbox))),
            None,
        )
        if idx != None:
            currentbox[idx] = (label, lens)
        else:
            currentbox.append((label, lens))
    elif operation == "-":
        currentbox = list(filter(lambda a: a[0] != label, currentbox))
    boxes[box] = currentbox

total = 0
for key in boxes:
    for i, content in enumerate(boxes[key]):
        value = (key + 1) * (i + 1) * content[1]
        total += value
print(total)

nodes = {}
queue = []

f = open("day20input.txt", "r")
for line in f.read().split("\n"):
    left, right = line.split(" -> ")
    rights = right.split(", ")
    if left[0] == "%":
        nodes[left[1:]] = {"type": left[0], "state": False, "out": rights}
    elif left[0] == "&":
        nodes[left[1:]] = {"type": left[0], "memory": {}, "out": rights}
    else:
        nodes[left] = {"type": "b", "out": rights}

for conjunction in [key for key, val in nodes.items() if val["type"] == "&"]:
    for key, value in nodes.items():
        if conjunction in value["out"]:
            nodes[conjunction]["memory"][key] = "low"

count = {"low": 0, "high": 0}
for _ in range(1000):
    count["low"] += 1
    for node in nodes["broadcaster"]["out"]:
        queue.append([node, "low", "broadcaster"])
        count["low"] += 1
    while len(queue):
        pulse = queue.pop(0)
        if pulse[0] in nodes:
            if nodes[pulse[0]]["type"] == "%" and pulse[1] == "low":
                nodes[pulse[0]]["state"] = not nodes[pulse[0]]["state"]
                for node in nodes[pulse[0]]["out"]:
                    queue.append(
                        [node, "high" if nodes[pulse[0]]["state"] else "low", pulse[0]]
                    )
                    count["high" if nodes[pulse[0]]["state"] else "low"] += 1
            elif nodes[pulse[0]]["type"] == "&":
                nodes[pulse[0]]["memory"][pulse[2]] = pulse[1]
                for node in nodes[pulse[0]]["out"]:
                    count[
                        "high" if "low" in nodes[pulse[0]]["memory"].values() else "low"
                    ] += 1
                    queue.append(
                        [
                            node,
                            "high"
                            if "low" in nodes[pulse[0]]["memory"].values()
                            else "low",
                            pulse[0],
                        ]
                    )

print(count["low"] * count["high"])

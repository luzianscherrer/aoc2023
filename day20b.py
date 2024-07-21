import math

nodes = {}
queue = []


def load():
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
        if rights[0] == "rx":
            start = left[1:]

    for conjunction in [key for key, val in nodes.items() if val["type"] == "&"]:
        for key, value in nodes.items():
            if conjunction in value["out"]:
                nodes[conjunction]["memory"][key] = "low"
    return start


def pulses(base, check):
    load()
    press = 0
    while True:
        press += 1
        for node in nodes["broadcaster"]["out"]:
            queue.append([node, "low", "broadcaster"])
        while len(queue):
            if nodes[base]["memory"][check] == "high":
                return press
            pulse = queue.pop(0)
            if pulse[0] in nodes:
                if nodes[pulse[0]]["type"] == "%" and pulse[1] == "low":
                    nodes[pulse[0]]["state"] = not nodes[pulse[0]]["state"]
                    for node in nodes[pulse[0]]["out"]:
                        queue.append(
                            [
                                node,
                                "high" if nodes[pulse[0]]["state"] else "low",
                                pulse[0],
                            ]
                        )
                elif nodes[pulse[0]]["type"] == "&":
                    nodes[pulse[0]]["memory"][pulse[2]] = pulse[1]
                    for node in nodes[pulse[0]]["out"]:
                        queue.append(
                            [
                                node,
                                "high"
                                if "low" in nodes[pulse[0]]["memory"].values()
                                else "low",
                                pulse[0],
                            ]
                        )


start = load()
memories = [pulses(start, key) for key in nodes[start]["memory"].keys()]
print(math.lcm(*memories))

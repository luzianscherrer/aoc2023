import re
import copy
import math

rules = {}
ranges = []


def apply_rule(rule, item):
    for instruction in rule:
        if "goto" in instruction:
            if instruction["goto"] == "A":
                ranges.append(item)
            elif instruction["goto"] != "R":
                apply_rule(rules[instruction["goto"]], item)
            return
        elif instruction["operator"] == "<":
            item1 = copy.deepcopy(item)
            item1[instruction["variable"]][1] = instruction["value"] - 1
            item[instruction["variable"]][0] = instruction["value"]
        elif instruction["operator"] == ">":
            item1 = copy.deepcopy(item)
            item1[instruction["variable"]][0] = instruction["value"] + 1
            item[instruction["variable"]][1] = instruction["value"]
        if instruction["destination"] == "A":
            ranges.append(item1)
        elif instruction["destination"] != "R":
            apply_rule(rules[instruction["destination"]], item1)


f = open("day19input.txt", "r")
for line in f.read().split("\n"):
    if len(line) and line[0] != "{":
        rule = []
        match = re.match(r"(.+){(.+)}", line)
        label = match.group(1)
        content = match.group(2)
        for match in re.finditer(r"(.)([<>])(\d+):([^,]+)", content):
            rule.append(
                {
                    "variable": match.group(1),
                    "operator": match.group(2),
                    "value": int(match.group(3)),
                    "destination": match.group(4),
                }
            )
        rule.append({"goto": content.split(",")[-1]})
        rules[label] = rule

apply_rule(
    rules["in"],
    {
        "x": [1, 4000],
        "m": [1, 4000],
        "a": [1, 4000],
        "s": [1, 4000],
    },
)

print(sum([math.prod([v[1] - v[0] + 1 for v in r.values()]) for r in ranges]))

import re
import operator

items = []
rules = {}


def apply_rule(rule, item):
    for instruction in rule:
        if "goto" in instruction:
            return instruction["goto"]
        for key in item:
            if instruction["variable"] == key and instruction["operator"](
                item[key], instruction["value"]
            ):
                return instruction["destination"]


f = open("day19input.txt", "r")
for line in f.read().split("\n"):
    if len(line):
        if line[0] == "{":
            item = {}
            for match in re.finditer(r".=\d+", line):
                item[match.group(0)[0]] = int(match.group(0)[2:])
            items.append(item)
        else:
            rule = []
            match = re.match(r"(.+){(.+)}", line)
            label = match.group(1)
            content = match.group(2)
            for match in re.finditer(r"(.)([<>])(\d+):([^,]+)", content):
                rule.append(
                    {
                        "variable": match.group(1),
                        "operator": operator.lt
                        if match.group(2) == "<"
                        else operator.gt,
                        "value": int(match.group(3)),
                        "destination": match.group(4),
                    }
                )
            rule.append({"goto": content.split(",")[-1]})
            rules[label] = rule

res = 0
for item in items:
    ret = "in"
    while ret not in ["A", "R"]:
        ret = apply_rule(rules[ret], item)
    if ret == "A":
        res += sum(item.values())
print(res)

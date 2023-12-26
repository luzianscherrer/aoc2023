import heapq, numpy as np

opposites = {"U": "D", "D": "U", "L": "R", "R": "L"}
directions = [((-1, 0), "U"), ((0, 1), "R"), ((1, 0), "D"), ((0, -1), "L")]
prohibits = ["U", "R", "D", "L"]

m = np.pad(np.genfromtxt("day17input.txt", dtype=np.uint8, delimiter=1), 1)


def neighbors(idx, exclude=[]):
    neighbors = []
    for i in directions:
        pos = tuple(np.array(idx) + np.array(i[0]))
        value = m[tuple(np.array(pos) + np.array([1, 1]))]
        if value != 0 and i[1] not in exclude:
            neighbors.append((pos, m[tuple(np.array(pos) + np.array([1, 1]))], i[1]))

    return neighbors


def solve(idx, target):
    distances = {(idx, tuple([])): 0}
    queue = [(0, idx, [])]
    while len(queue):
        curdist, curidx, curdir = heapq.heappop(queue)

        if len(curdir) and (len(curdir[-4:]) != 4 or len(set(curdir[-4:])) != 1):
            excl = prohibits[:]
            excl.remove(curdir[-1])
        else:
            excl = []

        if len(curdir) == 10 and len(set(curdir)) == 1:
            excl.append(curdir[0])

        for neighbor in neighbors(curidx, exclude=excl):
            distance = curdist + neighbor[1]
            nextdir = curdir[-9:]
            nextdir.append(neighbor[2])

            if neighbor[0] == target:
                return distance
            elif (neighbor[0], tuple(nextdir)) not in distances:
                distances[(neighbor[0], tuple(nextdir))] = distance
                heapq.heappush(queue, (distance, neighbor[0], nextdir))

    return None


print(solve((0, 0), tuple(np.array(m.shape) - np.array([3, 3]))))

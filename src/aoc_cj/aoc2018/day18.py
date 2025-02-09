import copy
from collections import Counter


class LumberArea:
    def __init__(self, lines):
        self.area = [[x for x in line] for line in lines]

    def adj_in_area(self, x, y):
        s = {(x + _x, y + _y) for _x in range(-1, 2) for _y in range(-1, 2)}
        if x - 1 < 0:
            s -= {(x - 1, y + _y) for _y in range(-1, 2)}
        if y - 1 < 0:
            s -= {(x + _x, y - 1) for _x in range(-1, 2)}
        if x + 1 >= len(self.area):
            s -= {(x + 1, y + _y) for _y in range(-1, 2)}
        if y + 1 >= len(self.area):
            s -= {(x + _x, y + 1) for _x in range(-1, 2)}
        s.remove((x, y))
        return s

    def magic(self):
        start = copy.deepcopy(self.area)
        for y, row in enumerate(self.area):
            for x, acre in enumerate(row):
                adj_counts = {".": 0, "#": 0, "|": 0}
                for a in self.adj_in_area(x, y):
                    adj_counts[start[a[1]][a[0]]] += 1
                if acre == "." and adj_counts["|"] >= 3:
                    self.area[y][x] = "|"
                elif acre == "|" and adj_counts["#"] >= 3:
                    self.area[y][x] = "#"
                elif acre == "#" and not (adj_counts["#"] >= 1 and adj_counts["|"] >= 1):
                    self.area[y][x] = "."

    def __str__(self):
        return "\n".join(["".join([acre for acre in row]) for row in self.area])


def part_1(txt):
    lumber = LumberArea(txt.splitlines())
    for _ in range(10):
        lumber.magic()
    count = Counter(str(lumber))
    return count["|"] * count["#"]


def part_2(txt):
    lumber = LumberArea(txt.splitlines())
    seen = []
    minutes = 1000000000
    for i in range(minutes):
        lumber.magic()
        str_l = str(lumber)
        if str_l in seen:
            seen_at = seen.index(str_l)
            cycle_size = i - seen_at
            remaining_minutes = minutes - i - 1
            value_at_end = seen[seen_at + ((remaining_minutes) % cycle_size)]
            count = Counter(value_at_end)
            return count["|"] * count["#"]
        else:
            seen.append(str_l)
    count = Counter(str_l)
    return count["|"] * count["#"]


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

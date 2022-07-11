from collections import Counter, defaultdict
from collections.abc import Iterable, Sequence
from typing import Callable

Path = Sequence[str]
Edges = dict[str, set[str]]


def parta(txt: str) -> int:
    edges = parse(txt)

    def can_explore(path: Path, cave: str) -> bool:
        return cave.isupper() or cave not in path

    return count_paths(edges, can_explore)


def partb(txt: str) -> int:
    edges = parse(txt)

    def can_explore(path: Path, cave: str) -> bool:
        if cave.isupper():
            return True
        counts = Counter(path)
        if counts[cave] == 0:
            return True
        visited_any_small_cave_more_than_once = any(counts[c] > 1 for c in counts if c.islower())
        return not visited_any_small_cave_more_than_once

    return count_paths(edges, can_explore)


def parse(txt: str) -> Edges:
    edges = defaultdict(set)
    for begin, end in (line.split("-") for line in txt.splitlines()):
        if end != "start":  # can't go back to start
            edges[begin].add(end)
        if begin != "start":  # can't go back to start
            edges[end].add(begin)
    return edges


def count_paths(edges: Edges, can_explore: Callable[[Path, str], bool]) -> Iterable[Path]:
    count = 0
    to_explore: set[Path] = {("start",)}
    while to_explore:
        exploring = to_explore.pop()
        current_pos = exploring[-1]

        if current_pos == "end":
            count += 1
            continue

        for new_pos in edges[current_pos]:
            if can_explore(exploring, new_pos):
                to_explore.add((*exploring, new_pos))

    return count


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)

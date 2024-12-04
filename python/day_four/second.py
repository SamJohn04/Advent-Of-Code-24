from collections import namedtuple
import sys


Index = namedtuple("Index", ["x", "y"])


def index_shift(index: Index, x: int = 0, y: int = 0) -> Index:
    return Index(x=index.x + x, y=index.y + y)


def get_indices(a_index: Index, max_index: Index, min_index: Index | None = None) -> list[tuple[Index, Index, Index, Index]]:
    if min_index is None:
        min_index = Index(0, 0)
    
    if a_index.x <= min_index.x or a_index.y <= min_index.y or a_index.x >= max_index.x or a_index.y >= max_index.y:
        return []

    indices = []

    # M . M
    # . A .
    # S . S
    indices.append((
        index_shift(a_index, x=-1, y=-1),
        index_shift(a_index, x=1, y=-1),
        index_shift(a_index, x=1, y=1),
        index_shift(a_index, x=-1, y=1),
        ))

    # S . S
    # . A .
    # M . M
    indices.append((
        index_shift(a_index, x=1, y=1),
        index_shift(a_index, x=-1, y=1),
        index_shift(a_index, x=-1, y=-1),
        index_shift(a_index, x=1, y=-1),
        ))

    # M . S
    # . A .
    # M . S
    indices.append((
        index_shift(a_index, x=-1, y=-1),
        index_shift(a_index, x=-1, y=1),
        index_shift(a_index, x=1, y=1),
        index_shift(a_index, x=1, y=-1),
        ))

    # S . M
    # . A .
    # S . M
    indices.append((
        index_shift(a_index, x=1, y=1),
        index_shift(a_index, x=1, y=-1),
        index_shift(a_index, x=-1, y=-1),
        index_shift(a_index, x=-1, y=1),
        ))

    return indices


def count_xmas(puzzle_input: str):
    count = 0
    lines = puzzle_input.splitlines()
    max_index = Index(x=len(lines[0]) - 1, y=len(lines) - 1)

    for i in range(max_index.y + 1):
        for j in range(max_index.x + 1):
            if lines[i][j] != 'A':
                continue
            for m1, m2, s1, s2 in get_indices(Index(x=j, y=i), max_index):
                if lines[m1.y][m1.x] != 'M' or lines[m2.y][m2.x] != 'M':
                    continue
                if lines[s1.y][s1.x] != 'S' or lines[s2.y][s2.x] != 'S':
                    continue
                count += 1

    return count


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        print(count_xmas(file.read()))


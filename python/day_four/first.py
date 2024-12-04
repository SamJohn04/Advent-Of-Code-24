from collections import namedtuple
import sys


Index = namedtuple("Index", ["x", "y"])


def index_shift(index: Index, x: int = 0, y: int = 0) -> Index:
    return Index(x=index.x + x, y=index.y + y)


def get_indices(start_index: Index, max_index: Index, min_index: Index | None = None) -> list[tuple[Index, Index, Index]]:
    if min_index is None:
        min_index = Index(0, 0)

    indices = []

    # W
    if start_index.x > min_index.x + 2:
        indices.append((
            index_shift(start_index, x=-1),
            index_shift(start_index, x=-2),
            index_shift(start_index, x=-3)
            ))

    # NW
    if start_index.y > min_index.y + 2 and start_index.x > min_index.x + 2:
        indices.append((
            index_shift(start_index, x=-1, y=-1),
            index_shift(start_index, x=-2, y=-2),
            index_shift(start_index, x=-3, y=-3)
            ))

    # N
    if start_index.y > min_index.y + 2:
        indices.append((
            index_shift(start_index, y=-1),
            index_shift(start_index, y=-2),
            index_shift(start_index, y=-3)
            ))

    # NE
    if start_index.y > min_index.y + 2 and start_index.x < max_index.x - 2:
        indices.append((
            index_shift(start_index, x=1, y=-1),
            index_shift(start_index, x=2, y=-2),
            index_shift(start_index, x=3, y=-3)
            ))

    # E
    if start_index.x < max_index.x - 2:
        indices.append((
            index_shift(start_index, x=1),
            index_shift(start_index, x=2),
            index_shift(start_index, x=3)
            ))

    # SE
    if start_index.y < max_index.y - 2 and start_index.x < max_index.x - 2:
        indices.append((
            index_shift(start_index, x=1, y=1),
            index_shift(start_index, x=2, y=2),
            index_shift(start_index, x=3, y=3)
            ))

    # S
    if start_index.y < max_index.y - 2:
        indices.append((
            index_shift(start_index, y=1),
            index_shift(start_index, y=2),
            index_shift(start_index, y=3)
            ))

    # SW
    if start_index.y < max_index.y - 2 and start_index.x > min_index.x + 2:
        indices.append((
            index_shift(start_index, x=-1, y=1),
            index_shift(start_index, x=-2, y=2),
            index_shift(start_index, x=-3, y=3)
            ))

    return indices


def count_xmas(puzzle_input: str):
    count = 0
    lines = puzzle_input.splitlines()
    max_index = Index(x=len(lines[0]) - 1, y=len(lines) - 1)

    for i in range(max_index.y + 1):
        for j in range(max_index.x + 1):
            if lines[i][j] != 'X':
                continue
            for indices in get_indices(Index(x=j, y=i), max_index):
                if lines[indices[0].y][indices[0].x] != 'M':
                    continue
                if lines[indices[1].y][indices[1].x] != 'A':
                    continue
                if lines[indices[2].y][indices[2].x] != 'S':
                    continue
                count += 1

    return count


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        print(count_xmas(file.read()))


from collections import namedtuple
import sys


Position = namedtuple("Position", ["row", "col"])


def next_position(curr_position: Position, orientation: str) -> Position:
    match orientation:
        case '^':
            return Position(row=curr_position.row - 1, col=curr_position.col)
        case '>':
            return Position(row=curr_position.row, col=curr_position.col + 1)
        case 'v':
            return Position(row=curr_position.row + 1, col=curr_position.col)
        case '<':
            return Position(row=curr_position.row, col=curr_position.col - 1)
        case _:
            raise Exception("Unexpected orientation!")


def next_orientation(orientation: str) -> str:
    match orientation:
        case '^':
            return '>'
        case '>':
            return 'v'
        case 'v':
            return '<'
        case '<':
            return '^'
        case _:
            raise Exception("Unexpected orientation!")


def traveled_ground(lines: list[str], starting_position: Position) -> int:
    visited = {starting_position}

    curr_position = starting_position
    orientation = '^'
    while fits(curr_position.row, 0, len(lines) - 1) and fits(curr_position.col, 0, len(lines[0]) - 1):
        new_position = next_position(curr_position, orientation)
        if not (fits(new_position.row, 0, len(lines) - 1) and fits(new_position.col, 0, len(lines[0]) - 1)):
            break
        if lines[new_position.row][new_position.col] == '#':
            orientation = next_orientation(orientation)
        else:
            curr_position = new_position
            visited.add(new_position)

    return len(visited)


def find_guard(lines: list[str]) -> Position:
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c == '^':
                return Position(row, col)

    raise Exception("Guard not found!")


def fits(val: int, lower_bound: int, upper_bound: int):
    return val <= upper_bound and val >= lower_bound


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        lines = file.read().splitlines()
    guard_position = find_guard(lines)

    print(traveled_ground(lines, guard_position))


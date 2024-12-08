import sys


def antinodes(first_point: tuple[int, int], second_point: tuple[int, int]) -> list[tuple[int, int]]:
    distance = first_point[0] - second_point[0], first_point[1] - second_point[1]
    anti_nodes = [first_point, second_point]
    next_point = first_point[0] + distance[0], first_point[1] + distance[1]
    while point_fits(next_point):
        anti_nodes.append(next_point)
        next_point = next_point[0] + distance[0], next_point[1] + distance[1]

    next_point = second_point[0] - distance[0], second_point[1] - distance[1]
    while point_fits(next_point):
        anti_nodes.append(next_point)
        next_point = next_point[0] - distance[0], next_point[1] - distance[1]

    return anti_nodes


def point_fits(point: tuple[int, int]) -> bool:
    return (
            point[0] >= min_point[0] and
            point[1] >= min_point[1] and
            point[0] <= max_point[0] and
            point[1] <= max_point[1]
            )


def all_anti_nodes_of_antenna(points: list[tuple[int, int]]) -> set[tuple[int, int]]:
    all_anti_nodes = set()
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            all_anti_nodes.update(antinodes(points[i], points[j]))
    return all_anti_nodes


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        lines = file.read().splitlines()

    antennas = {}

    min_point = 0, 0
    max_point = len(lines) - 1, len(lines[0]) - 1

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j].isalnum():
                antennas[lines[i][j]] = [(i, j)] + antennas.get(lines[i][j], [])

    anti_nodes = set()
    for c in antennas:
        anti_nodes.update(all_anti_nodes_of_antenna(antennas[c]))

    print(len(anti_nodes))


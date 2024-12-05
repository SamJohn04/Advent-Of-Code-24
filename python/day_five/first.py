import sys


def parse_rules(file):
    must_be_before_map: dict[str, set[str]] = {}
    line = file.readline()
    while len(line.strip()) != 0:
        a, b = line.strip().split('|')
        if b not in must_be_before_map:
            must_be_before_map[b] = set()
        must_be_before_map[b].add(a)
        line = file.readline()

    return must_be_before_map


def get_summable_value(pages_line: str, must_be_before_map: dict[str, set[str]]):
    pages = pages_line.split(',')
    invalid_pages = set()

    for page in pages:
        if page in invalid_pages:
            return 0
        invalid_pages.update(must_be_before_map.get(page, []))

    if len(pages) % 2 == 1:
        return int(pages[len(pages) // 2])
    print("even number of pages")
    return (int(pages[len(pages) // 2]) + int(pages[len(pages) // 2 + 1])) / 2


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        must_be_before_map = parse_rules(file)
        # print(must_be_before_map)
        value = 0
        for line in file.read().splitlines():
            value += get_summable_value(line, must_be_before_map)

    print(value)


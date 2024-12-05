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


def fix_pages(pages: list[str], must_be_before_map: dict[str, set[str]]):
    remaining_pages = set(pages)
    fixed_pages = []

    while len(pages) > len(fixed_pages):
        for page in remaining_pages:
            if page in fixed_pages:
                continue
            for needed_page in must_be_before_map.get(page, []):
                if needed_page not in fixed_pages and needed_page in remaining_pages:
                    break
            else:
                fixed_pages.append(page)

    return int(fixed_pages[len(fixed_pages) // 2])


def get_summable_value(pages_line: str, must_be_before_map: dict[str, set[str]]):
    pages = pages_line.split(',')
    invalid_pages = set()

    for page in pages:
        if page in invalid_pages:
            return fix_pages(pages, must_be_before_map)
        invalid_pages.update(must_be_before_map.get(page, []))
    
    return 0


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        must_be_before_map = parse_rules(file)
        # print(must_be_before_map)
        value = 0
        for line in file.read().splitlines():
            value += get_summable_value(line, must_be_before_map)

    print(value)


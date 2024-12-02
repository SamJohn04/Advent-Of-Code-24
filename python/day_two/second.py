import sys


def is_increasing(levels: list[int], prev_index: int = 0, next_index: int = 1, has_skipped: bool = False):
    if next_index == len(levels):
        return True
    if prev_index < 0:
        return False
    diff = levels[next_index] - levels[prev_index]
    if diff < 1 or diff > 3:
        if has_skipped:
            return False
        return is_increasing(levels, prev_index - 1, next_index, True) or is_increasing(levels, prev_index, next_index + 1, True)
    return is_increasing(levels, next_index, next_index + 1, has_skipped)


def is_decreasing(levels: list[int], prev_index: int = 0, next_index: int = 1, has_skipped: bool = False):
    if next_index == len(levels):
        return True
    if prev_index < 0:
        return False
    diff = levels[prev_index] - levels[next_index]
    if diff < 1 or diff > 3:
        if has_skipped:
            return False
        return is_decreasing(levels, prev_index - 1, next_index, True) or is_decreasing(levels, prev_index, next_index + 1, True)
    return is_decreasing(levels, next_index, next_index + 1, has_skipped)


def report_is_ok(report: str):
    levels = [int(level) for level in report.split()]
    return is_increasing(levels) or is_decreasing(levels) or is_increasing(levels[1:], has_skipped=True) or is_decreasing(levels[1:], has_skipped=True)


if __name__ == '__main__':
    total_count = 0
    with open(sys.argv[1]) as file:
        for report in file.readlines():
            if report_is_ok(report):
                total_count += 1
    print(total_count)


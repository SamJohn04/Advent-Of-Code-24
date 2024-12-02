import sys


def report_is_ok(report: str):
    levels = [int(level) for level in report.split()]
    all_increasing = levels[0] < levels[1]
    for i in range(1, len(levels)):
        if levels[i] == levels[i - 1]:
            return False
        if levels[i] < levels[i - 1]:
            if all_increasing or levels[i - 1] - levels[i] > 3:
                return False
        else:
            if not all_increasing or levels[i] - levels[i - 1] > 3:
                return False
    return True


if __name__ == '__main__':
    total_count = 0
    with open(sys.argv[1]) as file:
        for report in file.readlines():
            if report_is_ok(report):
                total_count += 1
    print(total_count)


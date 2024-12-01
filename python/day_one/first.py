import sys


def parse(input_content: str):
    left_list, right_list = [], []

    for line in input_content.splitlines():
        left_val, right_val = line.split()
        left_list.append(int(left_val))
        right_list.append(int(right_val))

    return left_list, right_list


if __name__ == '__main__':
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else input("Input File Name: ")

    with open(input_file_path) as input_file:
        input_content = input_file.read()

    left_list, right_list = parse(input_content)
    left_list.sort()
    right_list.sort()

    difference = 0

    for a, b in zip(left_list, right_list):
        difference += abs(a - b)

    print(difference)


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

    counts = {}
    similarity_score = 0

    for number in left_list:
        if number not in counts:
            counts[number] = right_list.count(number)
        similarity_score += number * counts[number]
    
    print(similarity_score)


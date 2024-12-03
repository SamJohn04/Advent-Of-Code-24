import sys


def parse_memory(memory: str):
    result = 0

    index = 0
    do = 1
    while index + 7 < len(memory):
        if memory[index] == 'd' and memory[index+1] == 'o':
            if memory[index+2] == '(' and memory[index+3] == ')':
                do = 1
                index += 4
                continue
            elif memory[index+2] == 'n' and memory[index+3] == '\'' and memory[index+4] == 't' and memory[index+5] == '(' and memory[index+6] == ')':
                do = 0
                index += 7
                continue

        if memory[index] != 'm':
            index += 1
            continue
        if memory[index + 1] != 'u':
            index += 1
            continue
        if memory[index + 2] != 'l':
            index += 2
            continue
        if memory[index + 3] != '(':
            index += 3
            continue
        index += 4

        a, b = '', ''
        while index < len(memory) and memory[index].isdigit():
            if len(a) == 3:
                break
            a += memory[index]
            index += 1
        if index >= len(memory) or memory[index] != ',' or len(a) == 0:
            continue
        index += 1
        while index < len(memory) and memory[index].isdigit():
            if len(b) == 3:
                break
            b += memory[index]
            index += 1
        if index >= len(memory) or memory[index] != ')' or len(b) == 0:
            continue

        result += int(a) * int(b) * do
        index += 1

    return result


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        print(parse_memory(file.read()))


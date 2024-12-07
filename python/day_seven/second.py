import sys


def can_concatonate(result: int, operand: int) -> bool:
    return str(result).endswith(str(operand))


def un_concatenated_result(result: int, operand: int) -> int:
    return int(str(result)[:-len(str(operand))])


def is_valid_equation(needed_result: int, operands: list[int]) -> bool:
    if len(operands) == 1:
        return operands[0] == needed_result
    return (
            needed_result > operands[-1] and is_valid_equation(needed_result - operands[-1], operands[:-1]) or
            needed_result % operands[-1] == 0 and is_valid_equation(needed_result // operands[-1], operands[:-1]) or
            can_concatonate(needed_result, operands[-1]) and is_valid_equation(un_concatenated_result(needed_result, operands[-1]), operands[:-1])
            )


def summable_from_equation(equation: str) -> int:
    needed_result, remaining = equation.split(':')
    needed_result = int(needed_result)
    operands = list(map(int, remaining.strip().split()))

    return needed_result if is_valid_equation(needed_result, operands) else 0


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        print(sum(map(summable_from_equation, file.read().splitlines())))


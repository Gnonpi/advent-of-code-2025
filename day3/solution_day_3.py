from collections import namedtuple
from loguru import logger
from advent_interaction import get_problem_input

CURRENT_DAY = 3

ValueAndPosition = namedtuple("ValueAndPosition", ["value", "position"])


def line_to_digits(line: str) -> list[int]:
    return [int(c) for c in line.strip()]


def parse_problem(input_string: str) -> list[list[int]]:
    records = []
    for line in input_string.split():
        if line == "":
            continue
        records.append(line_to_digits(line))
    return records


def find_highest(record: list[int]) -> ValueAndPosition:
    max_val = max(record)
    max_pos = record.index(max_val)
    return ValueAndPosition(value=max_val, position=max_pos)


def find_couple_in_record(record: list[int]) -> int:
    first_digit = find_highest(record[:-1])
    second_digit = find_highest(record[first_digit.position + 1 :])
    return first_digit.value * 10 + second_digit.value


def solve_part_1(input_string: str) -> int:
    records = parse_problem(input_string)

    sum_couple = 0
    for record in records:
        sum_couple += find_couple_in_record(record)
    return sum_couple


def find_twelve_numbers_in_record(record: list[int]) -> int:
    previous_position = 0
    current_sum = ""
    for i in reversed(range(1, 12 + 1)):
        if i == 1:
            # if i== 1, index become 0 -> not negative and giving an empty list
            current = find_highest(record[previous_position:])
        else:
            current = find_highest(record[previous_position : -i + 1])

        current_sum += str(current.value)
        previous_position = previous_position + current.position + 1
    return int(current_sum)


def solve_part_2(input_string: str) -> int:
    records = parse_problem(input_string)

    sum_couple = 0
    for record in records:
        sum_couple += find_twelve_numbers_in_record(record)
    return sum_couple


def main():
    input_string = get_problem_input(CURRENT_DAY)
    solution_part_1 = solve_part_1(input_string)
    logger.info(f"Solution part 1: {solution_part_1}")
    solution_part_2 = solve_part_2(input_string)
    logger.info(f"Solution part 2: {solution_part_2}")


if __name__ == "__main__":
    main()

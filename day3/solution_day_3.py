from collections import namedtuple
from loguru import logger
from advent_interaction import get_problem_input

CURRENT_DAY = 3

ValueAndPosition = namedtuple("ValueAndPosition", ["value", "position"])


def parse_problem(input_string: str) -> list[list[int]]:
    records = []
    for line in input_string.split():
        if line == "":
            continue
        records.append([int(c) for c in line.strip()])
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


def solve_part_2(input_string: str) -> int:
    raise NotImplementedError


def main():
    input_string = get_problem_input(CURRENT_DAY)
    solution_part_1 = solve_part_1(input_string)
    logger.info(f"Solution part 1: {solution_part_1}")
    solution_part_2 = solve_part_2(input_string)
    logger.info(f"Solution part 2: {solution_part_2}")


if __name__ == "__main__":
    main()

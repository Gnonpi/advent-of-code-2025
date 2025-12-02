from loguru import logger
from advent_interaction import get_problem_input

CURRENT_DAY = 1

START_DIAL = 50
TOTAL_DIAL = 100


def parse_problem(input_string: str) -> list[int]:
    result = []
    for line in input_string.split("\n"):
        line = line.strip()
        if line == "":
            continue
        number = int(line[1:])
        if line.startswith("L"):
            result.append(-1 * number)
        elif line.startswith("R"):
            result.append(number)
        else:
            raise RuntimeError
    return result


def solve_part_1(input_string: str) -> int:
    records = parse_problem(input_string)

    current = START_DIAL
    cnt_zero = 0
    for rec in records:
        current += rec
        current = current % TOTAL_DIAL
        if current == 0:
            cnt_zero += 1
    return cnt_zero


def solve_part_2(input_string: str) -> int:
    records = parse_problem(input_string)

    current = START_DIAL
    cnt_over_zero = 0
    for rec in records:
        quotient = (current + rec) // TOTAL_DIAL
        remainder = (current + rec) % TOTAL_DIAL
        cnt_over_zero += abs(quotient)
        # don't count twice from 0
        if current == 0 and rec < 0:
            cnt_over_zero -= 1
        # if we go left and end on 0
        if remainder == 0 and rec < 0:
            cnt_over_zero += 1
        current = remainder
    return cnt_over_zero


def main():
    input_string = get_problem_input(CURRENT_DAY)
    solution_part_1 = solve_part_1(input_string)
    logger.info(f"Solution part 1: {solution_part_1}")
    solution_part_2 = solve_part_2(input_string)
    logger.info(f"Solution part 2: {solution_part_2}")


if __name__ == "__main__":
    main()

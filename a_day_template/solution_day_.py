from loguru import logger
from advent_interaction import get_problem_input

CURRENT_DAY = None


def parse_problem(input_string: str) -> :
    raise NotImplementedError

def solve_part_1(input_string: str) -> int:
    raise NotImplementedError


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

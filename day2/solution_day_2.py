import itertools
import math
from advent_interaction import get_problem_input

from loguru import logger

CURRENT_DAY = 2

RangeNumber = tuple[int, int]


def parse_problem(input_string: str) -> list[RangeNumber]:
    records = []
    for line in input_string.split(","):
        start, end = line.split("-")
        records.append((int(start), int(end)))
    return records


def split_range_bound(range_bound: int) -> int:
    # there's something to do with log10
    len_range = len(str(range_bound))
    if len_range % 2 == 0:
        bound = int(len_range / 2)
        return int(str(range_bound)[:bound])
    else:
        bound = math.ceil(len_range / 2)
        return int(str(range_bound)[:bound])


def find_invalid_in_range(start: int, end: int) -> list[int]:
    split_start = split_range_bound(start)
    split_end = split_range_bound(end)
    invalid_ids = []

    if split_start > split_end:
        split_start = int(split_start / 10)

    # logger.debug(f"from {split_start} to {split_end}")
    for left in range(split_start, split_end + 1):
        # logger.debug(f"{left=}")
        constructed = int(str(left) + str(left))
        if start <= constructed <= end:
            invalid_ids.append(constructed)
    return invalid_ids


def solve_part_1(input_string: str) -> int:
    records = parse_problem(input_string)
    sum_invalid = 0
    for range_num in records:
        invalid_ids = find_invalid_in_range(range_num[0], range_num[1])
        sum_invalid += sum(invalid_ids)
    return sum_invalid


def find_repeated_invalid_ids(start: int, end: int) -> list[int]:
    # let's brute force
    invalid_ids = []
    for current in range(start, end + 1):
        power_current = math.ceil(math.log10(current))
        for i in range(1, math.ceil(power_current / 2) + 1):
            if power_current % i != 0:
                continue
            split_current = [
                "".join(tee_iter) for tee_iter in itertools.batched(str(current), i)
            ]
            # print(f"{current=} , {i=} : {split_current=}")
            if len(set(split_current)) == 1:
                invalid_ids.append(current)
                break
    return invalid_ids


def solve_part_2(input_string: str) -> int:
    records = parse_problem(input_string)
    sum_invalid = 0
    for range_num in records:
        invalid_ids = find_repeated_invalid_ids(range_num[0], range_num[1])
        sum_invalid += sum(invalid_ids)
    return sum_invalid


def main():
    input_string = get_problem_input(CURRENT_DAY)
    solution_part_1 = solve_part_1(input_string)
    logger.info(f"Solution part 1: {solution_part_1}")
    solution_part_2 = solve_part_2(input_string)
    logger.info(f"Solution part 2: {solution_part_2}")


if __name__ == "__main__":
    main()

import copy
from itertools import combinations
from typing import NamedTuple
from dataclasses import dataclass
from loguru import logger

CURRENT_DAY = 5


class RangeIds(NamedTuple):
    start: int
    end: int


@dataclass(frozen=True)
class Ingredients:
    fresh: list[RangeIds]
    available: list[int]


def parse_problem(input_string: str) -> Ingredients:
    fresh = []
    available = []

    for line in input_string.split("\n"):
        s_line = line.strip()
        if s_line == "":
            continue
        if "-" in s_line:
            start, end = s_line.split("-")
            fresh.append(
                RangeIds(
                    int(start),
                    int(end),
                )
            )
        else:
            available.append(int(s_line))
    return Ingredients(
        fresh=fresh,
        available=available,
    )


def ingredient_id_in_any_fresh_range(ingredients: Ingredients, ingr_id: int) -> bool:
    for fresh_range in ingredients.fresh:
        if fresh_range.start <= ingr_id <= fresh_range.end:
            return True
    return False


def solve_part_1(input_string: str) -> int:
    ingredients = parse_problem(input_string)

    count_fresh = 0
    for ingr_id in ingredients.available:
        if ingredient_id_in_any_fresh_range(ingredients, ingr_id):
            count_fresh += 1

    return count_fresh


def is_overlapping_range(range_a: RangeIds, range_b: RangeIds) -> bool:
    if range_a.end < range_b.start:
        return False
    if range_a.start > range_b.end:
        return False
    return True


def fuse_ranges(range_a: RangeIds, range_b: RangeIds) -> RangeIds:
    return RangeIds(
        start=min(range_a.start, range_b.start), end=max(range_a.end, range_b.end)
    )


def combine_fresh_ranges(fresh_ranges: list[RangeIds]) -> list[RangeIds]:
    new_fresh_ranges = copy.deepcopy(fresh_ranges)

    i = 0
    max_iter = 100
    combined_last = True
    while i < max_iter and combined_last:
        combined_last = False
        for comb_range in combinations(copy.deepcopy(new_fresh_ranges), 2):
            range_a, range_b = comb_range
            if is_overlapping_range(range_a, range_b):
                # print(f"{range_a=} ; {range_b=}")
                fused_range = fuse_ranges(range_a, range_b)
                new_fresh_ranges.remove(range_a)
                new_fresh_ranges.remove(range_b)
                new_fresh_ranges.append(fused_range)
                combined_last = True
                break
    return new_fresh_ranges


def solve_part_2(input_string: str) -> int:
    ingredients = parse_problem(input_string)
    # Combine any overlapping ranges
    combined_ranges = combine_fresh_ranges(ingredients.fresh)
    # Sum size of all ranges
    cnt_range = 0
    for fresh_range in combined_ranges:
        # print(f"{fresh_range=}")
        cnt_range += fresh_range.end - fresh_range.start + 1
    return cnt_range


def main():
    input_string = get_problem_input(CURRENT_DAY)
    solution_part_1 = solve_part_1(input_string)
    logger.info(f"Solution part 1: {solution_part_1}")
    solution_part_2 = solve_part_2(input_string)
    logger.info(f"Solution part 2: {solution_part_2}")


if __name__ == "__main__":
    main()

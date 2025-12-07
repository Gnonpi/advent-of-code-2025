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

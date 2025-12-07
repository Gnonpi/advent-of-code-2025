from day5.advent_interaction import get_problem_input
from day5.solution_day_5 import (
    CURRENT_DAY,
    solve_part_1,
    solve_part_2,
    parse_problem,
    Ingredients,
    RangeIds,
)

SAMPLE = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def test_parse_problem():
    assert parse_problem(SAMPLE) == Ingredients(
        fresh=[
            RangeIds(3, 5),
            RangeIds(10, 14),
            RangeIds(16, 20),
            RangeIds(12, 18),
        ],
        available=[1, 5, 8, 11, 17, 32],
    )


class TestPart1:
    def test_solve_sample(self):
        expected = 3
        assert solve_part_1(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(CURRENT_DAY)
        accepted_value = 885
        assert solve_part_1(input_string) == accepted_value


class TestPart2:
    def test_solve_sample(self):
        expected = None
        assert solve_part_2(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(CURRENT_DAY)
        accepted_value = None
        assert solve_part_2(input_string) == accepted_value

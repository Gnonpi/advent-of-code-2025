import pytest
from day3.advent_interaction import get_problem_input
from day3.solution_day_3 import (
    CURRENT_DAY,
    solve_part_1,
    solve_part_2,
    find_twelve_numbers_in_record,
    line_to_digits,
    parse_problem,
)

SAMPLE = """
987654321111111
811111111111119
234234234234278
818181911112111
"""


def test_parse_problem():
    sample = """
    987654321111111
    811111111111119
    """
    assert parse_problem(sample) == [
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    ]


class TestPart1:
    def test_solve_sample(self):
        expected = 357
        assert solve_part_1(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(CURRENT_DAY)
        accepted_value = 16993
        assert solve_part_1(input_string) == accepted_value


class TestPart2:
    @pytest.mark.parametrize(
        "start, expected",
        [
            (line_to_digits("987654321111111"), 987654321111),
            (line_to_digits("234234234234278"), 434234234278),
            (line_to_digits("818181911112111"), 888911112111),
        ],
    )
    def test_find_twelve_numbers_in_record(self, start, expected):
        assert find_twelve_numbers_in_record(start) == expected

    def test_solve_sample(self):
        expected = 3121910778619
        assert solve_part_2(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(CURRENT_DAY)
        accepted_value = None
        assert solve_part_2(input_string) == accepted_value

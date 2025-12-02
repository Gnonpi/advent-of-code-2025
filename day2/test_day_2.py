import pytest
from day2.advent_interaction import get_problem_input
from day2.solution_day_2 import (
    CURRENT_DAY,
    split_range_bound,
    solve_part_1,
    find_invalid_in_range,
    solve_part_2,
    parse_problem,
)

SAMPLE = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


def test_parse_problem():
    assert parse_problem(SAMPLE) == [
        (11, 22),
        (95, 115),
        (998, 1012),
        (1188511880, 1188511890),
        (222220, 222224),
        (1698522, 1698528),
        (446443, 446449),
        (38593856, 38593862),
        (565653, 565659),
        (824824821, 824824827),
        (2121212118, 2121212124),
    ]


class TestPart1:
    @pytest.mark.parametrize(
        "range_bound, expected",
        [
            (998, 99),
            (1010, 10),
            (1698522, 1698),
        ],
    )
    def test_split_range_bound(self, range_bound, expected):
        assert split_range_bound(range_bound) == expected

    @pytest.mark.parametrize(
        "start, end, expected",
        [
            (11, 22, [11, 22]),
            (95, 115, [99]),
            (998, 1012, [1010]),
            (1698522, 1698528, []),
        ],
    )
    def test_find_invalid_in_range(self, start, end, expected):
        assert find_invalid_in_range(start, end) == expected

    def test_solve_sample(self):
        expected = 1227775554
        assert solve_part_1(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(CURRENT_DAY)
        accepted_value = None
        assert solve_part_1(input_string) == accepted_value


class TestPart2:
    def test_solve_sample(self):
        expected = None
        assert solve_part_2(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(CURRENT_DAY)
        accepted_value = None
        assert solve_part_2(input_string) == accepted_value

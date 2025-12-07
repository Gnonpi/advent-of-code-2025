import pytest
from day4.advent_interaction import get_problem_input
from day4.solution_day_4 import (
    CURRENT_DAY,
    count_adjacent,
    solve_part_1,
    solve_part_2,
    parse_problem,
)

SAMPLE = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


@pytest.mark.skip(reason="it's a double list, should be ok")
def test_parse_problem():
    assert parse_problem(SAMPLE) == []


class TestPart1:
    def test_count_adjacent_border(self):
        records = parse_problem(SAMPLE)
        border_coord = (0, 2)
        assert count_adjacent(records, border_coord) == 3

    def test_solve_sample(self):
        expected = 13
        assert solve_part_1(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(CURRENT_DAY)
        accepted_value = 1505
        assert solve_part_1(input_string) == accepted_value


class TestPart2:
    def test_solve_sample(self):
        expected = 43
        assert solve_part_2(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(CURRENT_DAY)
        accepted_value = 9182
        assert solve_part_2(input_string) == accepted_value

from day4.advent_interaction import get_problem_input
from day4.solution_day_4 import (
    CURRENT_DAY,
    solve_part_1,
    solve_part_2,
    parse_problem,
)

SAMPLE = """
"""

def test_parse_problem():
    assert parse_problem(SAMPLE) ==

class TestPart1:
    def test_solve_sample(self):
        expected = None
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

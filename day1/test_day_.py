from day1.advent_interaction import get_problem_input
from day1.solution_day_ import (
    CURRENT_DAY,
    solve_part_1,
    solve_part_2,
    parse_problem,
)

SAMPLE = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def test_parse_problem():
    assert parse_problem(SAMPLE) == [-68, -30, 48, -5, 60, -55, -1, -99, 14, -82]


class TestPart1:
    def test_solve_sample(self):
        expected = 3
        assert solve_part_1(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(CURRENT_DAY)
        accepted_value = 1092
        assert solve_part_1(input_string) == accepted_value


class TestPart2:
    def test_solve_sample(self):
        expected = 6
        assert solve_part_2(SAMPLE) == expected

    def test_r1000(self):
        expected = 10
        sample = "R1000"
        assert solve_part_2(sample) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(CURRENT_DAY)
        # 6591 is incorrect
        accepted_value = 6616
        assert solve_part_2(input_string) == accepted_value

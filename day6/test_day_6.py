from day6.advent_interaction import get_problem_input
from day6.solution_day_6 import (
    CURRENT_DAY,
    solve_part_1,
    solve_part_2,
    parse_problem,
    Problem,
    ProblemColumn,
)

SAMPLE = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""


def test_parse_problem():
    assert parse_problem(SAMPLE) == Problem(
        columns=[
            ProblemColumn(
                numbers=[123, 45, 6],
                operation="*",
            ),
            ProblemColumn(
                numbers=[328, 64, 98],
                operation="+",
            ),
            ProblemColumn(
                numbers=[51, 387, 215],
                operation="*",
            ),
            ProblemColumn(
                numbers=[64, 23, 314],
                operation="+",
            ),
        ]
    )


class TestPart1:
    def test_solve_sample(self):
        expected = 4_277_556
        assert solve_part_1(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(CURRENT_DAY)
        accepted_value = 5361735137219
        assert solve_part_1(input_string) == accepted_value


class TestPart2:
    def test_solve_sample(self):
        expected = None
        assert solve_part_2(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(CURRENT_DAY)
        accepted_value = None
        assert solve_part_2(input_string) == accepted_value

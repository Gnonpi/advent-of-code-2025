from day8.advent_interaction import get_problem_input
from day8.solution_day_8 import (
    CURRENT_DAY,
    solve_part_1,
    solve_part_2,
    parse_problem,
    build_circuits,
    Coord,
)

SAMPLE = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""


def test_parse_problem():
    assert parse_problem(SAMPLE)[:3] == [
        Coord(0, 162, 817, 812),
        Coord(1, 57, 618, 57),
        Coord(2, 906, 360, 560),
    ]


class TestPart1:
    def test_solve_sample(self):
        expected = 40
        assert solve_part_1(SAMPLE) == expected

    def test_build_circuits(self):
        circuits = build_circuits(parse_problem(SAMPLE), 10)
        size_circuits = sorted((c.size for c in circuits), reverse=True)
        # seven_ones = [*[1] * 7]
        # assert size_circuits == [5, 4, 2, 2, *seven_ones]
        assert size_circuits == [5, 4, 2, 2]

    def test_solve_real_problem(self):
        input_string = get_problem_input(CURRENT_DAY)
        accepted_value = 83520
        assert solve_part_1(input_string) == accepted_value


class TestPart2:
    def test_solve_sample(self):
        expected = 25272
        assert solve_part_2(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(CURRENT_DAY)
        accepted_value = 1131823407
        assert solve_part_2(input_string) == accepted_value

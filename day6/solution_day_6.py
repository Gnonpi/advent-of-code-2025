import re
from typing import Self
from dataclasses import dataclass
from loguru import logger

CURRENT_DAY = 6

RE_ANY_SPACE = re.compile(r"\s{1,}")


@dataclass
class ProblemColumn:
    numbers: list[int]
    operation: str

    def resolve(self) -> int:
        if self.operation == "*":
            result = self.numbers[0]
            for val in self.numbers[1:]:
                result *= val
            return result
        elif self.operation == "+":
            return sum(self.numbers)
        else:
            raise RuntimeError(f"Unknown operation: {self.operation}")

    @classmethod
    def from_buffer(cls, values: list[str]) -> Self:
        numbers = values[:-1]
        operation = values[-1]
        assert operation in {"+", "*"}

        return cls(
            numbers=[int(c) for c in numbers],
            operation=operation,
        )


@dataclass
class Problem:
    columns: list[ProblemColumn]

    def resolve(self) -> int:
        result = 0
        for col in self.columns:
            result += col.resolve()
        return result


def split_line_in_symbols(line: str) -> list[str]:
    split_line = RE_ANY_SPACE.split(line.strip())
    return [c for c in split_line if c != ""]


def parse_problem(input_string: str) -> Problem:
    buffer: list[list[str]] = []
    n_cols: int | None = None
    for line in input_string.split("\n"):
        if line.strip() == "":
            continue
        split_line = split_line_in_symbols(line)
        if n_cols is None:
            n_cols = len(split_line)
            buffer = [list() for i in range(n_cols)]
        print(f"{split_line=}")
        for i, val in enumerate(split_line):
            buffer[i].append(val)
    return Problem(
        columns=[ProblemColumn.from_buffer(buff_line) for buff_line in buffer]
    )


def solve_part_1(input_string: str) -> int:
    problem = parse_problem(input_string)
    return problem.resolve()


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

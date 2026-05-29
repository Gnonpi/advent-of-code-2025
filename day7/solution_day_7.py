from loguru import logger
from advent_interaction import get_problem_input

CURRENT_DAY = 7

RowsOfTachyon = list[list[int]]


def parse_problem(input_string: str) -> RowsOfTachyon:
    rows = []
    for line in input_string.split("\n"):
        if line.strip() == "":
            continue
        current_row = []
        for i, char in enumerate(line):
            if char in {"S", "^"}:
                current_row.append(i)
        if current_row:
            rows.append(current_row)
    return rows

def solve_part_1(input_string: str) -> int:
    rows_of_tachyon = parse_problem(input_string)
    current_rays = {rows_of_tachyon[0][0]}
    hit_count = 0
    for row in rows_of_tachyon[1:]:
        new_rays = current_rays.difference(row)
        hit_splitters = set(row).intersection(current_rays)
        for hit_split in hit_splitters:
            hit_count += 1
            new_rays.add(hit_split - 1)
            new_rays.add(hit_split + 1)

        current_rays = new_rays
    return hit_count

def solve_part_2(input_string: str) -> int:
    """
    When a particle hits a splitter, it creates 2 timelines.
    We must keep track of how many timelines are behind each particle.
    """
    rows_of_splitters = parse_problem(input_string)
    current_rays = {rows_of_splitters[0][0]: 1}
    for row in rows_of_splitters[1:]:
        non_hit = set(current_rays.keys()).difference(row)
        hit_splitters = set(row).intersection(set(current_rays.keys()))
        new_rays = {
            ray: current_rays[ray]
            for ray in non_hit
        }
        split_timelines = []
        for hit_split in hit_splitters:
            split_timelines.append((hit_split - 1, current_rays.get(hit_split, 0)))
            split_timelines.append((hit_split + 1, current_rays.get(hit_split, 0)))
        for (pos, cnt) in split_timelines:
            if pos in new_rays:
                new_rays[pos] += cnt
            else:
                new_rays[pos] = cnt

        current_rays = new_rays
    return sum(current_rays.values())


def main():
    input_string = get_problem_input(CURRENT_DAY)
    solution_part_1 = solve_part_1(input_string)
    logger.info(f"Solution part 1: {solution_part_1}")
    solution_part_2 = solve_part_2(input_string)
    logger.info(f"Solution part 2: {solution_part_2}")


if __name__ == "__main__":
    main()

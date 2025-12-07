from loguru import logger

CURRENT_DAY = 4

ROLL_SYM = "@"
Coord = tuple[int, int]
MapRolls = list[list[bool]]


def parse_problem(input_string: str) -> MapRolls:
    clean_lines = [line for line in input_string.split("\n") if line.strip()]

    records = []
    for line in clean_lines:
        records.append([c == ROLL_SYM for c in line])
    return records


def find_roll_coords(map_rolls: MapRolls) -> list[Coord]:
    result = []
    for i, line in enumerate(map_rolls):
        for j, cell in enumerate(line):
            if cell:
                result.append((i, j))
    return result


def generate_8_adjacent_coords(coord: Coord) -> list[Coord]:
    """
    a | b | c
    d | _ | e
    f | g | h
    """
    x, y = coord
    return [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]


def is_out_of_bound(map_rolls: MapRolls, coord: Coord) -> bool:
    x, y = coord
    if x < 0 or y < 0:
        return True
    return False


def count_adjacent(map_rolls: MapRolls, coord: Coord) -> int:
    cnt_adj = 0
    for adj_coord in generate_8_adjacent_coords(coord):
        if is_out_of_bound(map_rolls, adj_coord):
            continue
        try:
            adj_x, adj_y = adj_coord
            value = map_rolls[adj_x][adj_y]
            print(f"({adj_x},{adj_y}) = {int(value)}")
            cnt_adj += int(value)
        except IndexError:
            pass
    return cnt_adj


def solve_part_1(input_string: str) -> int:
    records = parse_problem(input_string)
    size_y = len(records)
    size_x = len(records[0])
    logger.debug(f"Grid: {size_x} x {size_y}")

    movable_coords = []
    count_movable = 0
    for roll_coord in find_roll_coords(records):
        cnt_adj = count_adjacent(records, roll_coord)
        if cnt_adj < 4:
            count_movable += 1
            movable_coords.append(roll_coord)

    # print_recs = [["." for c in range(size_x)] for _ in range(size_y)]
    # for roll_coord in find_roll_coords(records):
    #     x, y = roll_coord
    #     print_recs[x][y] = ROLL_SYM
    # for move_coord in movable_coords:
    #     x, y = move_coord
    #     print_recs[x][y] = "x"
    # print_tot = ["".join(line) for line in print_recs]
    # print_tot = "\n".join(print_tot)
    # print(print_tot)

    return count_movable


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

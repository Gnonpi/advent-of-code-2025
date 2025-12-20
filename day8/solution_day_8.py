import math
from typing import Self
from dataclasses import dataclass
from loguru import logger
from advent_interaction import get_problem_input

CURRENT_DAY = 8


@dataclass(frozen=True)
class Coord:
    idx: int
    x: int
    y: int
    z: int

    @classmethod
    def from_line(cls, idx: int, line: str) -> Self:
        x, y, z = line.split(",")
        return cls(
            idx,
            int(x),
            int(y),
            int(z),
        )

    def euclidean_distance(self, other: Self) -> float:
        return math.sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )


@dataclass
class Circuit:
    coords: set[Coord]

    @property
    def size(self) -> int:
        return len(self.coords)


def parse_problem(input_string: str) -> list[Coord]:
    result = []
    for i, line in enumerate(input_string.split("\n")):
        if line:
            result.append(Coord.from_line(i, line))
    return sorted(result, key=lambda c: c.idx)


def build_circuits(coords: list[Coord], connected_pairs: int) -> list[Circuit]:
    # building distance "matrix"
    nb_coords = len(coords)
    distance_to_indices: dict[float, tuple[int, int]] = {}
    for i in range(nb_coords):
        for j in range(nb_coords):
            if i == j:
                break
            dist = coords[i].euclidean_distance(coords[j])
            distance_to_indices[dist] = (i, j)
    # iterate over distances
    circuits: list[Circuit] = []
    sorted_distances = sorted(distance_to_indices.keys())
    nb_pairs = 0
    for i, s_dist in enumerate(sorted_distances):
        if i == connected_pairs:
            break
        idx_coord_a, idx_coord_b = distance_to_indices[s_dist]
        coord_a = coords[idx_coord_a]
        coord_b = coords[idx_coord_b]

        c_circuit_a = [c for c in circuits if coord_a in c.coords]
        c_circuit_b = [c for c in circuits if coord_b in c.coords]
        circuit_a = c_circuit_a[0] if c_circuit_a else None
        circuit_b = c_circuit_b[0] if c_circuit_b else None

        # 4 cases:
        # A. none of them are in a circuit -> create a new one
        # B. one of the two is in a circuit -> add the other to it
        # C. both are in same circuit -> no change
        # D. both are in different circuits -> merge circuits
        if circuit_a is None and circuit_b is None:
            circuits.append(Circuit(coords={coord_a, coord_b}))
            nb_pairs += 1
        elif circuit_a is None and circuit_b:
            circuit_b.coords.add(coord_a)
            nb_pairs += 1
        elif circuit_a and circuit_b is None:
            circuit_a.coords.add(coord_b)
            nb_pairs += 1
        # [union-attr] - we know both are non-None
        elif circuit_a.coords == circuit_b.coords:  # type: ignore
            pass
        else:
            assert circuit_a is not None
            assert circuit_b is not None
            circuit_a.coords.update(circuit_b.coords)
            circuits.remove(circuit_b)
            nb_pairs += 1
    return circuits


def solve_part_1(input_string: str) -> int:
    coords = parse_problem(input_string)

    if len(coords) < 100:
        connected_pairs = 10
    else:
        connected_pairs = 1000

    circuits = build_circuits(coords, connected_pairs)
    three_biggest = sorted(circuits, key=lambda c: c.size, reverse=True)[:3]
    return three_biggest[0].size * three_biggest[1].size * three_biggest[2].size


def build_circuits_until_one(
    coords: list[Coord]
) -> tuple[tuple[int, int], list[Circuit]]:
    # building distance "matrix"
    nb_coords = len(coords)
    distance_to_indices: dict[float, tuple[int, int]] = {}
    for i in range(nb_coords):
        for j in range(nb_coords):
            if i == j:
                break
            dist = coords[i].euclidean_distance(coords[j])
            distance_to_indices[dist] = (i, j)

    # iterate over distances
    circuits: list[Circuit] = []
    remaining_coords = set(coords)
    sorted_distances = sorted(distance_to_indices.keys())
    last_pair = 0, 0
    for i, s_dist in enumerate(sorted_distances):
        idx_coord_a, idx_coord_b = distance_to_indices[s_dist]
        coord_a = coords[idx_coord_a]
        coord_b = coords[idx_coord_b]

        c_circuit_a = [c for c in circuits if coord_a in c.coords]
        c_circuit_b = [c for c in circuits if coord_b in c.coords]
        circuit_a = c_circuit_a[0] if c_circuit_a else None
        circuit_b = c_circuit_b[0] if c_circuit_b else None

        # 4 cases:
        # A. none of them are in a circuit -> create a new one
        # B. one of the two is in a circuit -> add the other to it
        # C. both are in same circuit -> no change
        # D. both are in different circuits -> merge circuits
        if circuit_a is None and circuit_b is None:
            circuits.append(Circuit(coords={coord_a, coord_b}))
        elif circuit_a is None and circuit_b:
            circuit_b.coords.add(coord_a)
        elif circuit_a and circuit_b is None:
            circuit_a.coords.add(coord_b)
        # [union-attr] - we know both are non-None
        elif circuit_a.coords == circuit_b.coords:  # type: ignore
            pass
        else:
            assert circuit_a is not None
            assert circuit_b is not None
            circuit_a.coords.update(circuit_b.coords)
            circuits.remove(circuit_b)

        remaining_coords.discard(coord_a)
        remaining_coords.discard(coord_b)
        last_pair = coord_a.x, coord_b.x
        if len(remaining_coords) == 0:
            break

    return last_pair, circuits


def solve_part_2(input_string: str) -> int:
    coords = parse_problem(input_string)

    last_pair, circuits = build_circuits_until_one(coords)
    logger.debug(f"{last_pair=}")
    return last_pair[0] * last_pair[1]


def main():
    input_string = get_problem_input(CURRENT_DAY)
    solution_part_1 = solve_part_1(input_string)
    logger.info(f"Solution part 1: {solution_part_1}")
    solution_part_2 = solve_part_2(input_string)
    logger.info(f"Solution part 2: {solution_part_2}")


if __name__ == "__main__":
    main()

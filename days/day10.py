from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other: "Position") -> "Position":
        return Position(self.x + other.x, self.y + other.y)


class Grid:
    DIRECTIONS = [
        Position(-1, 0),  # up
        Position(0, 1),  # right
        Position(1, 0),  # down
        Position(0, -1),  # left
    ]

    def __init__(self, data):
        self.data = data
        self.height = len(data)
        self.width = len(data[0]) if self.height > 0 else 0

    def is_inside(self, pos: Position) -> bool:
        return 0 <= pos.x < self.height and 0 <= pos.y < self.width

    def get_cell(self, pos: Position) -> str:
        return self.data[pos.x][pos.y]

    def get_valid_next_positions(self, current_pos: Position):
        current_value = self.get_cell(current_pos)
        valid_positions = []

        for direction in self.DIRECTIONS:
            new_pos = current_pos + direction
            if self.is_inside(new_pos) and self.get_cell(new_pos) - current_value == 1:
                valid_positions.append(new_pos)

        return valid_positions


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = puzzle_input.strip().split("\n")
    grid_data = []
    trailheads = []

    for x, row in enumerate(lines):
        row_data = [int(char) for char in row]
        grid_data.append(row_data)

        for y, value in enumerate(row_data):
            if value == 0:
                trailheads.append(Position(x, y))

    return Grid(grid_data), trailheads


def find_paths(grid, start, path):
    if grid.get_cell(start) == 9:
        return [path]

    paths = []
    for next_pos in grid.get_valid_next_positions(start):
        new_path = path + [next_pos]
        paths.extend(find_paths(grid, next_pos, new_path))

    return paths


def part1(grid, trailheads) -> int:
    """Solve part 1."""
    total_unique_scores = 0

    for start in trailheads:
        paths = find_paths(grid, start, [start])
        unique_scores = set(path[-1] for path in paths)
        total_unique_scores += len(unique_scores)

    return total_unique_scores


def part2(grid, trailheads) -> int:
    """Solve part 2."""
    return sum(len(find_paths(grid, start, [start])) for start in trailheads)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    grid, trailheads = parse(puzzle_input)
    solution1 = part1(grid, trailheads)
    solution2 = part2(grid, trailheads)
    return solution1, solution2

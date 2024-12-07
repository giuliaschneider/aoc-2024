from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other: "Position") -> "Position":
        return Position(self.x + other.x, self.y + other.y)

    def rotate_right(self, current_direction: int) -> int:
        return (current_direction + 1) % 4


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

    def set_cell(self, pos: Position, value: str):
        self.data[pos.x][pos.y] = value


class GridSolver:
    def __init__(self, grid: Grid, start: Position):
        self.grid = grid
        self.position = start
        self.current_direction = 0  # Start facing up
        self.visited_states = {(self.position, self.current_direction)}
        self.found_loop = False

    def next_step(self):
        direction = self.current_direction
        for _ in range(4):  # Try all possible directions
            next_pos = self.position + self.grid.DIRECTIONS[direction]

            if not self.grid.is_inside(next_pos):
                return None, self.current_direction

            if self.grid.get_cell(next_pos) != "#":
                return next_pos, direction

            direction = self.position.rotate_right(direction)

        return None, self.current_direction

    def walk(self) -> bool:
        while True:
            next_pos, new_direction = self.next_step()

            if next_pos is None:
                break

            state = (next_pos, new_direction)
            if state in self.visited_states:
                self.found_loop = True
                break

            self.position = next_pos
            self.current_direction = new_direction
            self.visited_states.add(state)

    @property
    def visited_positions(self):
        return {pos for pos, _ in self.visited_states}


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = puzzle_input.split("\n")
    grid = []
    for x, row in enumerate(lines):
        grid.append(list(row))
        if "^" in row:
            starting_position = Position(x, row.index("^"))
    return Grid(grid), starting_position


def part1(grid: Grid, start: Position) -> int:
    solver = GridSolver(grid, start)
    solver.walk()
    return len(set(solver.visited_positions))


def part2(grid: Grid, start: Position) -> int:
    # Get initial path
    solver = GridSolver(grid, start)
    solver.walk()

    obstacle_positions = set()
    for pos in solver.visited_positions:
        if pos == start:
            continue

        original_value = grid.get_cell(pos)
        grid.set_cell(pos, "#")

        test_solver = GridSolver(grid, start)
        test_solver.walk()
        if test_solver.found_loop:
            obstacle_positions.add(pos)

        grid.set_cell(pos, original_value)

    return len(obstacle_positions)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    grid, starting_position = parse(puzzle_input)
    solution1 = part1(grid, starting_position)
    solution2 = part2(grid, starting_position)
    return solution1, solution2

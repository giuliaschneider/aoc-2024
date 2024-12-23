from utils.grid import Position, Grid


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = puzzle_input.split("\n")
    positions = [
        Position(int(x), int(y)) for line in lines for x, y in [line.split(",")]
    ]
    return positions


def part1(grid_length, obstacles, num_obstacles) -> int:
    """Solve part 1."""
    grid = Grid(grid_length, grid_length, obstacles[:num_obstacles])
    path_length, _ = grid.astar_search(
        Position(0, 0), Position(grid_length - 1, grid_length - 1)
    )
    return path_length


def part2(grid_length, obstacles, num_obstacles) -> str:
    """Solve part 2."""

    grid = Grid(grid_length, grid_length, obstacles[:num_obstacles])
    _, path = grid.astar_search(
        Position(0, 0), Position(grid_length - 1, grid_length - 1)
    )

    for i in range(num_obstacles + 1, len(obstacles)):
        pos = obstacles[i - 1]
        if pos not in path:
            continue
        grid = Grid(grid_length, grid_length, obstacles[:i])
        _, path = grid.astar_search(
            Position(0, 0), Position(grid_length - 1, grid_length - 1)
        )
        if path is None:
            return f"{pos.x},{pos.y}"


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    obstacles = parse(puzzle_input)
    solution1 = part1(71, obstacles, 1024)
    solution2 = part2(71, obstacles, 1024)
    return solution1, solution2

from collections import defaultdict
from itertools import combinations
from utils.grid import Position, Grid


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = puzzle_input.strip().split("\n")
    height = len(lines)
    width = len(lines[0])

    obstacles = set()
    start = None
    end = None

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                obstacles.add(Position(x, y))
            elif char == "S":
                start = Position(x, y)
            elif char == "E":
                end = Position(x, y)

    return obstacles, start, end, width, height


def get_cheat_canditates(path, max_distance=2, min_save=100):
    candidates = defaultdict(int)
    for i, next_index in combinations(range(len(path)), 2):
        diff = path[next_index] - path[i]
        distance = abs(diff.x) + abs(diff.y)
        save = (next_index - i) - distance
        if (distance) <= max_distance and save >= min_save:
            candidates[save] += 1
    return candidates


def part1(path, min_save=100) -> int:
    """Solve part 1."""
    canditates = get_cheat_canditates(path, min_save=min_save)
    return sum(value for key, value in canditates.items())


def part2(path, min_save=100) -> int:
    """Solve part 2."""
    canditates = get_cheat_canditates(path, 20, min_save=min_save)
    return sum(value for key, value in canditates.items())


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    obstacles, start, end, width, height = parse(puzzle_input)
    grid = Grid(height, width, obstacles)
    _, path = grid.astar_search(start, end)
    solution1 = part1(path)
    solution2 = part2(path)
    return solution1, solution2

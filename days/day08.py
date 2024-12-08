from dataclasses import dataclass
from collections import defaultdict
import itertools


@dataclass(frozen=True)
class Position:
    """Represents a 2D position with vector operations."""

    x: int
    y: int

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Position(self.x * scalar, self.y * scalar)


class Grid:
    def __init__(self, data):
        self.data = data
        self.height = len(data)
        self.width = len(data[0]) if self.height > 0 else 0
        self._antenna_positions = self._find_antenna_positions()

    def _find_antenna_positions(self):
        """Find all antenna positions in the grid."""
        positions = defaultdict(list)
        for x, row in enumerate(self.data):
            for y, char in enumerate(row):
                if char != ".":
                    positions[char].append(Position(x, y))
        return dict(positions)

    def is_inside(self, pos):
        """Check if a position is within grid boundaries."""
        return 0 <= pos.x < self.height and 0 <= pos.y < self.width

    @property
    def antenna_positions(self):
        """Get antenna positions (cached)."""
        return self._antenna_positions

    @property
    def max_dimension(self):
        """Get the maximum dimension of the grid."""
        return max(self.height, self.width)


def parse(puzzle_input: str):
    grid = puzzle_input.split("\n")
    grid = [list(row) for row in grid]
    grid = Grid(grid)
    return grid


def calculate_antinodes(grid, pos1, pos2, multiples):
    diff = pos2 - pos1
    candidates = set()

    for multiple in multiples:
        candidates.add(pos2 + diff * multiple)
        candidates.add(pos1 - diff * multiple)

    return {pos for pos in candidates if grid.is_inside(pos)}


def find_all_antinodes(grid, multiples):
    antinodes = []
    for key, values in grid.antenna_positions.items():
        for pair in itertools.combinations(values, 2):
            antinodes.extend(calculate_antinodes(grid, pair[0], pair[1], multiples))
    return antinodes


def part1(grid) -> int:
    """Solve part 1."""
    return len(set(find_all_antinodes(grid, [1])))


def part2(grid) -> int:
    """Solve part 2."""
    return len(set(find_all_antinodes(grid, range(grid.max_dimension))))


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

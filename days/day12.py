from collections import deque
from dataclasses import dataclass
from collections import defaultdict

from utils.grid import Position

class Grid:
    UP = Position(-1, 0)
    RIGHT = Position(0, 1)
    DOWN = Position(1, 0)
    LEFT = Position(0, -1)
    DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

    def __init__(self, data):
        self.data = data
        self.height = len(data)
        self.width = len(data[0]) if self.height > 0 else 0

    def is_inside(self, pos: Position) -> bool:
        return 0 <= pos.x < self.height and 0 <= pos.y < self.width

    def get_cell(self, pos: Position) -> str:
        return self.data[pos.x][pos.y]

    def get_valid_next_positions(self, pos: Position):
        return [pos + d for d in self.DIRECTIONS if self.is_inside(pos + d)]


def flood_fill(grid, start, visited):
    region = {start}
    queue = deque([start])
    target_value = grid.get_cell(start)

    while queue:
        current = queue.popleft()
        if grid.get_cell(current) != target_value:
            continue

        for next_pos in grid.get_valid_next_positions(current):
            if (
                next_pos not in region
                and next_pos not in visited
                and grid.get_cell(next_pos) == target_value
            ):
                visited.add(next_pos)
                queue.append(next_pos)
                region.add(next_pos)

    return region


def find_regions(grid, grid_data):
    starting_points = {
        Position(x, y) for x, row in enumerate(grid_data) for y, _ in enumerate(row)
    }

    regions = []
    visited = set()

    while starting_points:
        start = starting_points.pop()
        region = flood_fill(grid, start, visited)
        regions.append(region)
        visited.update(region)
        starting_points -= region

    return regions


def calculate_area(region):
    return len(region)


def calculate_perimeter(grid, region):
    return sum(
        4 - len(set(grid.get_valid_next_positions(pos)).intersection(region))
        for pos in region
    )


def get_horizontal_edges(region):
    edges = defaultdict(list)
    for pos in region:
        if pos + Grid.UP not in region:
            edges[pos.x, "up"].append(pos.y)
        if pos + Grid.DOWN not in region:
            edges[pos.x + 1, "down"].append(pos.y)
    return edges


def get_vertical_edges(region):
    edges = defaultdict(list)
    for pos in region:
        if pos + Grid.LEFT not in region:
            edges[pos.y, "left"].append(pos.x)
        if pos + Grid.RIGHT not in region:
            edges[pos.y + 1, "right"].append(pos.x)
    return edges


def count_edges(edges):
    count = len(edges)
    for coordinates in edges.values():
        coordinates.sort()
        count += sum(1 for c1, c2 in zip(coordinates, coordinates[1:]) if c2 - c1 > 1)
    return count


def calculate_sides(region):
    horizontal_edges = get_horizontal_edges(region)
    vertical_edges = get_vertical_edges(region)
    return count_edges(horizontal_edges) + count_edges(vertical_edges)


def parse(puzzle_input):
    lines = puzzle_input.strip().split("\n")
    grid_data = [list(line) for line in lines]
    grid = Grid(grid_data)
    regions = find_regions(grid, grid_data)
    return grid, regions


def part1(grid, regions) -> int:
    """Solve part 1."""
    total = 0
    for region in regions:
        total += calculate_area(region) * calculate_perimeter(grid, region)
    return total


def part2(grid, regions) -> int:
    """Solve part 2."""
    total = 0
    for region in regions:
        total += calculate_area(region) * calculate_sides(region)
    return total


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    grid, regions = parse(puzzle_input)
    solution1 = part1(grid, regions)
    solution2 = part2(grid, regions)
    return solution1, solution2

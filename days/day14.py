import math
import numpy as np
from scipy.spatial import cKDTree
import matplotlib.pyplot as plt
from utils.grid import Position


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    parsed_data = []
    for line in puzzle_input.strip().split("\n"):
        pos_part, vel_part = line.split(" v=")
        p_x, p_y = map(int, pos_part.split("p=")[1].split(","))
        v_x, v_y = map(int, vel_part.split(","))
        pos = Position(p_x, p_y)
        vel = Position(v_x, v_y)
        parsed_data.append((pos, vel))
    return parsed_data


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.midline_vertical = height // 2
        self.midline_horizontal = width // 2


def robot_move(grid: Grid, pos: Position, vel: Position):
    pos += vel

    new_x = pos.x
    new_y = pos.y

    if pos.x < 0:
        new_x = grid.width + pos.x
    if pos.x >= grid.width:
        new_x = pos.x - grid.width

    if pos.y < 0:
        new_y= grid.height + pos.y
    if pos.y >= grid.height:
        new_y = pos.y - grid.height

    return Position(new_x, new_y)


def create_numpy_grid(width, height, positions):
    grid = np.zeros((height, width), dtype=int)
    for pos in positions:
        grid[pos.y, pos.x] = 1
    return grid


def save_numpy_grid_as_png(grid, filename="numpy_grid.png", cmap="binary"):
    plt.figure(figsize=(10, 8))
    plt.imshow(grid, cmap=cmap, interpolation="nearest")
    plt.colorbar(label="Point Presence")
    plt.title("Grid Visualization")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Grid saved as {filename}")


def calculate_nearest_neighbors(positions):
    points = [[pos.x, pos.y] for pos in positions]
    points_array = np.array(points)
    tree = cKDTree(points_array)
    distances, _ = tree.query(points_array, k=2)
    nearest_distances = distances[:, 1]
    return nearest_distances


def simulate_movement(grid: Grid, positions_velocities: list, seconds: int):
    for time in range(0, seconds):
        for i, (pos, vel) in enumerate(positions_velocities):
            pos = robot_move(grid, pos, vel)
            positions_velocities[i] = (pos, vel)

        positions = [pos for pos, _ in positions_velocities]
        nearest_distances = calculate_nearest_neighbors(positions)

        if np.median(nearest_distances) <= 1:
            print(time + 1)
            print(np.median(nearest_distances))
            np_grid = create_numpy_grid(grid.width, grid.height, positions=positions)
            save_numpy_grid_as_png(np_grid, filename=f"img/numpy_grid_{time+1}.png")
            break

    return positions_velocities


def calculate_quadrands(grid, positions):
    quadrants = [0, 0, 0, 0]

    for pos, _ in positions:
        if pos.x < grid.midline_horizontal and pos.y < grid.midline_vertical:
            quadrants[0] += 1
        elif pos.x < grid.midline_horizontal and pos.y > grid.midline_vertical:
            quadrants[2] += 1
        elif pos.x > grid.midline_horizontal and pos.y < grid.midline_vertical:
            quadrants[1] += 1
        elif pos.x > grid.midline_horizontal and pos.y > grid.midline_vertical:
            quadrants[3] += 1

    print(quadrants)
    return quadrants


def part1(positions, height, width, seconds) -> int:
    """Solve part 1."""
    grid = Grid(height, width)
    positions = simulate_movement(grid, positions, seconds)
    quadrants = calculate_quadrands(grid, positions)
    return math.prod(quadrants)


def part2(positions, height, width, seconds) -> int:
    """Solve part 1."""
    grid = Grid(height, width)
    positions = simulate_movement(grid, positions, seconds)
    quadrants = calculate_quadrands(grid, positions)
    return math.prod(quadrants)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    positions = parse(puzzle_input)
    solution1 = part1(positions, 103, 101, 100)
    solution2 = part2(positions, 103, 101, 10000)
    return solution1, solution2

from utils.grid import Position
import heapq


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = puzzle_input.split("\n")
    positions = [
        Position(int(x), int(y)) for line in lines for x, y in [line.split(",")]
    ]
    return positions


class Grid:
    UP = Position(-1, 0)
    RIGHT = Position(0, 1)
    DOWN = Position(1, 0)
    LEFT = Position(0, -1)
    DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

    def __init__(self, height, width, obstacles):
        self.height = height
        self.width = width
        self.obstacles = obstacles

    def get_cell(self, pos: Position) -> str:
        return self.data[pos.y][pos.x]

    def set_cell(self, pos: Position, value: str):
        self.data[pos.y][pos.x] = value

    def is_inside(self, pos: Position) -> bool:
        return 0 <= pos.y < self.height and 0 <= pos.x < self.width

    def is_wall(self, pos: Position) -> bool:
        return pos in self.obstacles

    def print_grid(self):
        for row in self.data:
            print("".join(row))

    def get_valid_next_steps(self, position):
        next_steps = []
        for direction in self.DIRECTIONS:
            next_position = position + direction
            if self.is_inside(next_position) and not self.is_wall(next_position):
                next_steps.append(next_position)
        return next_steps


def heuristic(start, end) -> int:
    return abs(start.x - end.x) + abs(start.y - end.y)


def astart(grid, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        f_score, pos = heapq.heappop(open_set)
        if pos == end:
            path = []
            current = pos
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return g_score[pos], path

        for next_pos in grid.get_valid_next_steps(pos):
            new_g_score = g_score[pos] + 1
            if next_pos not in g_score or new_g_score < g_score[next_pos]:
                came_from[next_pos] = pos
                g_score[next_pos] = new_g_score
                f_score = new_g_score + heuristic(next_pos, end)
                heapq.heappush(open_set, (f_score, next_pos))


def part1(grid_length, obstacles, num_obstacles) -> int:
    """Solve part 1."""
    grid = Grid(grid_length, grid_length, obstacles[:num_obstacles])
    path_length, _ = astart(
        grid, Position(0, 0), Position(grid_length - 1, grid_length - 1)
    )
    return path_length


def part2(grid_length, obstacles, num_obstacles) -> str:
    """Solve part 2."""

    grid = Grid(grid_length, grid_length, obstacles[:num_obstacles])
    _, path = astart(
        grid, Position(0, 0), Position(grid_length - 1, grid_length - 1)
    )

    for i in range(num_obstacles + 1, len(obstacles)):
        print(i)
        pos = obstacles[i - 1]

        if pos not in path:
            continue

        grid = Grid(grid_length, grid_length, obstacles[:i])
        result = astart(
            grid, Position(0, 0), Position(grid_length - 1, grid_length - 1)
        )
        if result is None:
            return f"{pos.x},{pos.y}"
        else:
            _, path = result


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    obstacles = parse(puzzle_input)
    solution1 = part1(71, obstacles, 1024)
    solution2 = part2(71, obstacles, 1024)
    return solution1, solution2

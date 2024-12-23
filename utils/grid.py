from dataclasses import dataclass
import heapq


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

    def __lt__(self, other):
        # Required for heapq
        return False

    def manhattan_distance(self, other) -> int:
        """Calculate Manhattan distance to another position."""
        return abs(self.x - other.x) + abs(self.y - other.y)


class Grid:
    """
    The coordinate system is:
        x: horizontal position (increases from left to right)
        y: vertical position (increases from top to bottom)
        Origin (0,0) is at the top-left corner
    """

    UP = Position(0, -1)
    RIGHT = Position(1, 0)
    DOWN = Position(0, 1)
    LEFT = Position(-1, 0)
    DEFAULT_DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

    def __init__(self, height, width, obstacles, directions=None):
        self.height = height
        self.width = width
        self.obstacles = obstacles
        self.directions = (
            directions if directions is not None else self.DEFAULT_DIRECTIONS
        )

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

    def get_neighbors(self, position):
        return [
            position + direction
            for direction in self.directions
            if self.is_inside(position + direction)
        ]

    def get_valid_next_steps(self, position):
        return [
            neighbor
            for neighbor in self.get_neighbors(position)
            if not self.is_wall(neighbor)
        ]

    def find_all_shortest_path(self, start, goal):
        """Find the shortest path between two positions using BFS.

        Returns:
            List of positions representing the shortest path from start to goal,
            or None if no path exists.
        """
        if start == goal:
            return [[start]]

        paths = []
        min_length = float("inf")
        visited = set()

        def dfs(current, path):
            nonlocal min_length

            if len(path) > min_length:
                return

            if current == goal:
                if len(path) < min_length:
                    min_length = len(path)
                    paths.clear()
                    paths.append(path[:])
                elif len(path) == min_length:
                    paths.append(path[:])
                return

            visited.add(current)
            for next_pos in self.get_valid_next_steps(current):
                if next_pos not in visited:
                    path.append(next_pos)
                    dfs(next_pos, path)
                    path.pop()
            visited.remove(current)

        dfs(start, [start])
        return paths

    def astar_search(self, start: Position, end: Position, heuristic=None):
        """
        A* pathfinding algorithm.
        Returns:
            Tuple of (path_cost, path) or (None, None) if no path exists
        """
        if heuristic is None:
            heuristic = lambda pos: pos.manhattan_distance(end)

        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}

        while open_set:
            f_score, current = heapq.heappop(open_set)

            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return g_score[end], path

            for next_pos in self.get_valid_next_steps(current):
                tentative_g_score = g_score[current] + 1

                if next_pos not in g_score or tentative_g_score < g_score[next_pos]:
                    came_from[next_pos] = current
                    g_score[next_pos] = tentative_g_score
                    f_score = tentative_g_score + heuristic(next_pos)
                    heapq.heappush(open_set, (f_score, next_pos))

        return None, None

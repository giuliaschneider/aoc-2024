from utils.grid import Position


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    grid_part, moves_part = puzzle_input.strip().split("\n\n")
    grid = [list(row) for row in grid_part.split("\n")]
    grid = Grid(grid)
    moves = "".join(moves_part.split("\n"))
    return grid, moves


def find_starting_position(grid) -> Position:
    for x, row in enumerate(grid.data):
        for y, cell in enumerate(row):
            if cell == "@":
                return Position(x, y)


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

    def get_cell(self, pos: Position) -> str:
        return self.data[pos.x][pos.y]

    def set_cell(self, pos: Position, value: str):
        self.data[pos.x][pos.y] = value

    def is_inside(self, pos: Position) -> bool:
        return 0 <= pos.x < self.height and 0 <= pos.y < self.width

    def is_wall(self, pos: Position) -> bool:
        return self.get_cell(pos) == "#"

    def is_object(self, pos: Position) -> bool:
        return (
            self.get_cell(pos) == "O"
            or self.get_cell(pos) == "["
            or self.get_cell(pos) == "]"
        )

    def print_grid(self):
        for row in self.data:
            print("".join(row))

    def calculate_gps_coordinates(self) -> int:
        total = 0
        for y, row in enumerate(self.data):
            for x, cell in enumerate(row):
                if cell == "O" or cell == "[":
                    total += x + 100 * y
        return total


class Robot:
    UP = Position(-1, 0)
    RIGHT = Position(0, 1)
    DOWN = Position(1, 0)
    LEFT = Position(0, -1)
    DIRECTIONS = {"^": UP, ">": RIGHT, "v": DOWN, "<": LEFT}

    def __init__(self, grid: Grid, start: Position):
        self.grid = grid
        self.position = start

    def move(self, next_move: str):
        direction = self.DIRECTIONS[next_move]
        next_pos_robot = self.position + direction
        next_pos = next_pos_robot

        objects_to_move = []

        while self.grid.is_object(next_pos):
            objects_to_move.append(next_pos)
            next_pos += direction

        if self.grid.is_wall(next_pos):
            return

        self.position = next_pos_robot

        if objects_to_move:
            self.grid.set_cell(next_pos_robot, ".")
            self.grid.set_cell(objects_to_move[-1] + direction, "O")

    def move_double_grid(self, next_move: str):
        direction = self.DIRECTIONS[next_move]
        next_pos_robot = self.position + direction
        next_pos_list = [next_pos_robot]

        objects_to_move = set()

        if any(
            [
                not self.grid.is_inside(pos) or self.grid.is_wall(pos)
                for pos in next_pos_list
            ]
        ):
            return

        if next_move == ">" or next_move == "<":
            while any(
                [
                    (not self.grid.is_inside(pos)) or self.grid.is_object(pos)
                    for pos in next_pos_list
                ]
            ):
                next_pos = next_pos_list[0]
                if self.grid.get_cell(next_pos) == "[":
                    objects_to_move.add((next_pos, next_pos + self.DIRECTIONS[">"]))
                else:
                    objects_to_move.add((next_pos + self.DIRECTIONS["<"], next_pos))

                next_pos_list = [next_pos + direction * 2]

                if not self.grid.is_inside(next_pos_list[0]) or self.grid.is_wall(
                    next_pos_list[0]
                ):
                    return

        if next_move == "^" or next_move == "v":
            while any([self.grid.is_object(pos) for pos in next_pos_list]):
                new_objects = set()
                for pos in next_pos_list:
                    if self.grid.is_object(pos):
                        if self.grid.get_cell(pos) == "[":
                            new_objects.add((pos, pos + self.DIRECTIONS[">"]))
                        else:
                            new_objects.add((pos + self.DIRECTIONS["<"], pos))

                next_pos_list = []
                for object in new_objects:
                    if self.grid.is_wall(object[0] + direction) or self.grid.is_wall(
                        object[1] + direction
                    ):
                        return
                    next_pos_list.append(object[0] + direction)
                    next_pos_list.append(object[1] + direction)

                objects_to_move = objects_to_move.union(new_objects)

        self.position = next_pos_robot

        if objects_to_move:
            all_object_pos = [
                item + direction for tup in objects_to_move for item in tup
            ]

            self.grid.set_cell(next_pos_robot, ".")
            for object in objects_to_move:
                if object[0] not in all_object_pos:
                    self.grid.set_cell(object[0], ".")
                if object[1] not in all_object_pos:
                    self.grid.set_cell(object[1], ".")
                self.grid.set_cell(object[0] + direction, "[")
                self.grid.set_cell(object[1] + direction, "]")

    def run_robot_sequence(self, sequence: str, function):
        for move in sequence:
            function(move)
        return self.grid.calculate_gps_coordinates()


def part1(grid, moves) -> int:
    """Solve part 1."""
    starting_position = find_starting_position(grid)
    grid.set_cell(starting_position, ".")
    grid.print_grid()
    robot = Robot(grid, starting_position)
    return robot.run_robot_sequence(moves, robot.move)


def double_grid(grid):
    new_grid = []
    for x, row in enumerate(grid.data):
        new_row = []
        for y, cell in enumerate(row):
            if grid.is_object(Position(x, y)):
                new_row.extend(["[", "]"])
            elif grid.get_cell(Position(x, y)) == "@":
                new_row.extend(["@", "."])
            else:
                new_row.extend([cell] * 2)
        new_grid.append(new_row)
    return Grid(new_grid)


def part2(grid, moves) -> int:
    """Solve part 2."""
    grid = double_grid(grid)
    starting_position = find_starting_position(grid)
    grid.set_cell(starting_position, ".")
    robot = Robot(grid, starting_position)
    return robot.run_robot_sequence(moves, robot.move_double_grid)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    grid, moves = parse(puzzle_input)
    solution1 = part1(grid, moves)
    grid, moves = parse(puzzle_input)
    solution2 = part2(grid, moves)
    return solution1, solution2

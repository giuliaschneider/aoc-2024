from collections import Counter


def word_search(grid, word, directions):
    rows = len(grid)
    cols = len(grid[0])

    def is_valid(x, y):
        """Check if coordinates are within grid bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def search_from_point(start_x, start_y):
        """
        Search for word starting from a given point in all directions.

        Returns:
        - bool: True if word is found from this starting point
        """
        count = 0
        for dx, dy in directions:
            x, y = start_x, start_y
            found = True

            for letter in word:
                if not is_valid(x, y) or grid[x][y] != letter:
                    found = False
                    break

                x += dx
                y += dy

            if found:
                count += 1

        return count

    count = 0
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == word[0]:
                count_found_from_point = search_from_point(x, y)
                count += count_found_from_point
    return count


def word_search_positions(grid, word, directions):
    rows = len(grid)
    cols = len(grid[0])

    def is_valid(x, y):
        """Check if coordinates are within grid bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def find_word_positions(target_word):
        """
        Find all possible positions and directions of the word.

        Returns:
        - List[Tuple]: List of (start_x, start_y, dx, dy, positions)
        """
        letter_a_positions = []

        for start_x in range(rows):
            for start_y in range(cols):
                for dx, dy in directions:
                    positions = []
                    x, y = start_x, start_y
                    match = True

                    for letter in target_word:
                        if not is_valid(x, y) or grid[x][y] != letter:
                            match = False
                            break

                        positions.append((x, y))
                        x += dx
                        y += dy

                    if match:
                        letter_a_positions.append((x - dx - dx, y - dy - dy))

        return letter_a_positions

    return find_word_positions(word)


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = puzzle_input.split("\n")
    return [list(line) for line in lines]


def part1(data: any) -> int:
    """Solve part 1."""
    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
        (1, 1),  # down-right diagonal
        (1, -1),  # down-left diagonal
        (-1, 1),  # up-right diagonal
        (-1, -1),  # up-left diagonal
    ]
    return word_search(data, "XMAS", directions)


def part2(data: any) -> int:
    """Solve part 2."""
    directios = [
        (1, 1),  # down-right diagonal
        (1, -1),  # down-left diagonal
        (-1, 1),  # up-right diagonal
        (-1, -1),  # up-left diagonal
    ]

    a_positions = word_search_positions(data, "MAS", directios)
    return sum(1 for k, v in Counter(a_positions).items() if v > 1)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

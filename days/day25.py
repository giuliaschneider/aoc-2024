def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    patterns = puzzle_input.split("\n\n")
    locks = []
    keys = []
    for i, pattern in enumerate(patterns, 1):
        if pattern.startswith("#"):
            locks.append(parse_pattern(pattern, pattern_type="lock"))
        else:
            keys.append(parse_pattern(pattern, pattern_type="key"))
        print(pattern)
    return locks, keys


def parse_pattern(pattern, pattern_type="lock"):
    lines = [line for line in pattern.strip().split("\n") if line]
    height = len(lines)
    width = len(lines[0])

    heights = []

    for col in range(width):
        column_height = 0

        if pattern_type == "lock":
            for row in range(1, height):
                if lines[row][col] == ".":
                    column_height = row - 1
                    break
                if row == height - 1:
                    column_height = row - 1

        else:  # key
            for row in range(height - 2, -1, -1):
                if lines[row][col] == ".":
                    column_height = height - row - 2
                    break

        heights.append(column_height)

    return heights


def fit(lock, keys, avaialble_space=5):
    for lock_heights, key_heights in zip(lock, keys):
        if lock_heights + key_heights > avaialble_space:
            return False
    return True


def part1(locks, keys) -> int:
    """Solve part 1."""
    total = 0
    for lock in locks:
        for key in keys:
            total += int(fit(lock, key))
    return total


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    locks, keys = parse(puzzle_input)
    solution1 = part1(locks, keys)
    return solution1, None

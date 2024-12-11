from collections import defaultdict


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    stones = defaultdict(int)
    first_line = puzzle_input.split("\n")[0]
    for stone in first_line.split():
        stones[int(stone)] += 1
    return stones


def stone_change(value):
    if value == 0:
        return [1]

    value_str = str(value)
    digit_count = len(value_str)

    if digit_count % 2 == 0:
        mid_point = digit_count // 2
        left_value = int(value_str[:mid_point])
        right_value = int(value_str[mid_point:])
        return [left_value, right_value]

    return [value * 2024]


def blink(stone_dict):
    total_stones = 0
    new_stones = defaultdict(int)

    for stone_value, count in stone_dict.items():
        for new_value in stone_change(stone_value):
            new_stones[new_value] += count
            total_stones += count

    return new_stones, total_stones


def simulate_rounds(stones, num_rounds):
    for _ in range(num_rounds):
        stones, total_stones = blink(stones)
    return total_stones


def part1(data: any) -> int:
    """Solve part 1."""
    return simulate_rounds(data, 25)


def part2(data: any) -> int:
    """Solve part 2."""
    return simulate_rounds(data, 75)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

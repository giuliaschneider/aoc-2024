from collections import defaultdict


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = [line.strip() for line in puzzle_input.split("\n") if line.strip()]

    available_towels = lines[0].split(", " if ", " in lines[0] else " ")
    designs = lines[1:]

    return available_towels, designs


def find_combinations(design, available_towels):
    n = len(design)
    dp = defaultdict(int)
    dp[0] = 1

    for i in range(n):
        if i not in dp:
            continue

        for towel in available_towels:
            if i + len(towel) > n:
                continue

            if design[i : i + len(towel)] == towel:
                new_pos = i + len(towel)
                dp[new_pos] += dp[i]

    return dp[n]


def part1(available_towels, designs) -> int:
    sorted_towels = sorted(available_towels, key=len, reverse=True)
    count = 0
    for design in designs:
        if find_combinations(design, sorted_towels):
            count += 1

    return count


def part2(available_towels, designs) -> int:
    """Solve part 1."""
    sorted_towels = sorted(available_towels, key=len, reverse=True)
    count = 0
    for design in designs:
        result = find_combinations(design, sorted_towels)
        if result:
            count += result
    return count


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    available_towels, designs = parse(puzzle_input)
    # solution1 = part1(available_towels, designs)
    solution2 = part2(available_towels, designs)
    return "solution1", solution2

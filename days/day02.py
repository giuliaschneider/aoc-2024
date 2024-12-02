def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = puzzle_input.split("\n")
    return [list(map(int, line.split())) for line in lines]


def is_report_safe(report: list[int]) -> bool:
    """So, a report only counts as safe if both of the following are true:
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three."""
    is_increasing = report[0] < report[1]
    if is_increasing:
        return all(1 <= b - a <= 3 for a, b in zip(report, report[1:]))
    else:
        return all(1 <= a - b <= 3 for a, b in zip(report, report[1:]))


def is_report_safe_with_dampener(report: list[int]) -> bool:
    """Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe."""
    if is_report_safe(report):
        return True
    # Try removing each element and check if the resulting list is safe
    # any short circuits
    return any(is_report_safe(report[:i] + report[i + 1 :]) for i in range(len(report)))


def part1(data: any) -> int:
    return sum(is_report_safe(report) for report in data)


def part2(data: any) -> int:
    """Solve part 2."""
    return sum(is_report_safe_with_dampener(report) for report in data)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

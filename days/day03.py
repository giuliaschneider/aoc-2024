import re


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    numbers = []
    for result in re.findall(regex, puzzle_input):
        numbers.append((int(result[0]), int(result[1])))
    return numbers


def parse2(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    result = []
    dos = puzzle_input.split("do()")
    for part in dos:
        result += parse(part.split("don't()")[0])
    return result


def part1(data: any) -> int:
    """Solve part 1."""
    return sum(x[0] * x[1] for x in data)


def part2(puzzle_input: any) -> int:
    """Solve part 2."""
    data = parse2(puzzle_input)
    return sum(x[0] * x[1] for x in data)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(puzzle_input)
    return solution1, solution2

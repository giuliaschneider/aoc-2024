from itertools import product


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    parsed_input = {}
    for line in puzzle_input.strip().split("\n"):
        parts = line.split(": ")
        key = int(parts[0])
        values = [int(val) for val in parts[1].split()]
        parsed_input[key] = values
    return parsed_input


def evaluate_left_to_right(nums, ops) -> int:
    result = nums[0]
    operations = {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "||": lambda x, y: int(str(x) + str(y)),
    }

    for i, op in enumerate(ops):
        result = operations[op](result, nums[i + 1])
    return result


def find_valid_combinations(data, operators):
    valid_results = []
    for target, values in data.items():
        num_operators_needed = len(values) - 1
        for ops in product(operators, repeat=num_operators_needed):
            if evaluate_left_to_right(values, ops) == target:
                valid_results.append(target)
                break
    return valid_results


def part1(data: any) -> int:
    """Solve part 1."""
    valid_results = find_valid_combinations(data, ["+", "*"])
    return sum(valid_results)


def part2(data: any) -> int:
    """Solve part 2."""
    valid_results = find_valid_combinations(data, ["+", "*", "||"])
    return sum(valid_results)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

from functools import cache


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = puzzle_input.split("\n")
    return list(map(int, lines))


@cache
def mix(value, secret_number):
    return value ^ secret_number


@cache
def prune(secret_number):
    return secret_number % 16777216


@cache
def calculate_new_secret_number(secret_number):
    result = secret_number * 64
    secret_number = mix(result, secret_number)
    secret_number = prune(secret_number)
    result = secret_number // 32
    secret_number = mix(result, secret_number)
    secret_number = prune(secret_number)
    result = secret_number * 2048
    secret_number = mix(result, secret_number)
    secret_number = prune(secret_number)
    return secret_number


def get_price(secret_number):
    return secret_number % 10


def part1(data: any) -> int:
    """Solve part 1."""
    total = 0
    for secret_number in data:
        for _ in range(2000):
            secret_number = calculate_new_secret_number(secret_number)
        total += secret_number
    return total


def calculate_price_sequence(secret_number):
    """Calculate price sequence and differences for a secret number."""
    prices = []
    diffs = []

    for i in range(2000):
        secret_number = calculate_new_secret_number(secret_number)
        current_price = get_price(secret_number)
        prices.append(current_price)
        if i != 0:
            diffs.append(current_price - prices[i - 1])

    return prices, diffs


def part2(data: any) -> int:
    """Solve part 2."""
    prices_per_change = {}

    for secret_number in data:
        prices, diffs = calculate_price_sequence(secret_number)
        changes_seen = set()
        for i in range(0, len(diffs) - 4):
            sequence = tuple(diffs[i : i + 4])
            if sequence in changes_seen:
                continue

            changes_seen.add(sequence)
            if sequence not in prices_per_change:
                prices_per_change[sequence] = 0
            prices_per_change[sequence] += prices[i + 4]

    return max(prices_per_change.values())


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

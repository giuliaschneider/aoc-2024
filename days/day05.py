from functools import cmp_to_key


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = puzzle_input.split("\n")
    rules, updates = [], []
    for line in lines:
        if not line:
            continue
        if "|" in line:
            rules.append(list(map(int, line.split("|"))))
        else:
            updates.append(list(map(int, line.split(","))))
    return rules, updates


def check_order(rules, update):
    """Check if update respect all relevant rules."""
    positions = {num: i for i, num in enumerate(update)}

    for before, after in rules:
        if before in positions and after in positions:
            if positions[before] > positions[after]:
                return False
    return True


def midpoint_of_list(update):
    return update[len(update) // 2]


def sort_update(rules, update):
    def sort_key(a, b):
        if check_order(rules, [a, b]):
            return -1
        return 1

    return sorted(update, key=cmp_to_key(sort_key))


def part1(rules, updates) -> int:
    """What do you get if you add up the middle page number from those correctly-ordered updates?"""
    midpoints = []
    for update in updates:
        if check_order(rules, update):
            midpoints.append(midpoint_of_list(update))
    return sum(midpoints)


def part2(rules, updates: any) -> int:
    """Solve part 2."""
    midpoints = []
    for update in updates:
        if not check_order(rules, update):
            update = sort_update(rules, update)
            midpoints.append(midpoint_of_list(update))
    return sum(midpoints)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    (rules, updates) = parse(puzzle_input)
    solution1 = part1(rules, updates)
    solution2 = part2(rules, updates)
    return solution1, solution2

from collections import Counter


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    list_1, list_2 = [], []
    for line in puzzle_input.strip().split("\n"):
        if line.strip():
            number_1, number_2 = map(int, line.split())
            list_1.append(number_1)
            list_2.append(number_2)
    return [list_1, list_2]


def distance(position_1: int, position_2: int) -> int:
    return abs(position_1 - position_2)


def part1(data: any) -> int:
    """Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on."""
    sorted_list1 = sorted(data[0])
    sorted_list2 = sorted(data[1])
    return sum(
        distance(sorted_list1[i], sorted_list2[i]) for i in range(len(sorted_list1))
    )


def part2(data: any) -> int:
    """Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list."""
    count_ids = Counter(data[1])
    return sum(id * count_ids[id] for id in data[0])


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

from days.day05 import parse, part1, part2, solve

EXAMPLE_INPUT = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip()


def test_parse():
    (rules, updates) = parse(EXAMPLE_INPUT)
    assert rules[:2] == [
        [47, 53],
        [97, 13],
    ]
    assert updates == [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ]


def test_part1():
    (rules, updates) = parse(EXAMPLE_INPUT)
    result = part1(rules, updates)
    assert result == 143


def test_part2():
    (rules, updates) = parse(EXAMPLE_INPUT)
    result = part2(rules, updates)
    assert result == 123


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)

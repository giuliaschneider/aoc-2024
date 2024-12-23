from days.day23 import parse, part1, part2, solve

EXAMPLE_INPUT = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""".strip()


def test_parse():
    data = parse(EXAMPLE_INPUT)
    assert data["td"] == set(["yn", "wh", "tc", "qp"])


def test_part1():
    data = parse(EXAMPLE_INPUT)
    result = part1(data)
    assert result == 7


def test_part2():
    data = parse(EXAMPLE_INPUT)
    result = part2(data)
    assert result == "co,de,ka,ta"


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)

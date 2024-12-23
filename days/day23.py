from collections import defaultdict
from utils.graphs import find_cycles, bron_kerbosch


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    graph = defaultdict(set)
    for line in puzzle_input.strip().split("\n"):
        node1, node2 = line.strip().split("-")
        graph[node1].add(node2)
        graph[node2].add(node1)
    return graph


def find_max_clique(graph):
    cliques = []
    bron_kerbosch(set(), set(graph.keys()), set(), graph, cliques)
    return max(cliques, key=len) if cliques else set()


def part1(data: any) -> int:
    """Solve part 1."""
    cycles = find_cycles(data, 3, 3)
    return sum(1 for cycle in cycles if any(node.startswith("t") for node in cycle))


def part2(data: any) -> int:
    """Solve part 2."""
    max_clique = find_max_clique(data)
    return ",".join(sorted(list(max_clique)))


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

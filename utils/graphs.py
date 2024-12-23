import copy


def find_cycles(graph, min_length=3, max_length=None):
    def dfs(current, start, path, visited, cycles):
        path.append(current)

        if max_length and len(path) > max_length:
            return

        for neighbor in graph[current]:
            if neighbor == start and len(path) >= min_length:
                cycle = tuple(sorted(path))
                cycles.add(cycle)
            elif neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor, start, copy.deepcopy(path), visited, cycles)
                visited.remove(neighbor)

    cycles = set()
    visited = set()
    for node in graph.keys():
        dfs(node, node, [], visited, cycles)
    return cycles


def bron_kerbosch(clique, candidates, excluded, graph, cliques):
    if not candidates and not excluded:
        cliques.append(clique.copy())
        return

    for candidate in candidates:
        neighbors = graph[candidate]
        bron_kerbosch(
            clique | {candidate},
            neighbors & candidates,
            neighbors & excluded,
            graph,
            cliques,
        )
        candidates = candidates - {candidate}
        excluded = excluded | {candidate}

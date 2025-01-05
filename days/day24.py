from collections import defaultdict


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = puzzle_input.strip().split("\n")

    # Parse inputs
    inputs = {}
    i = 0
    while i < len(lines) and ":" in lines[i]:
        var, value = lines[i].split(":")
        inputs[var.strip()] = int(value.strip())
        i += 1

    # Skip empty line
    i += 1

    # Parse operations
    operations = []
    while i < len(lines):
        parts = lines[i].split("->")
        inputs_op = parts[0].strip().split()
        output = parts[1].strip()

        if len(inputs_op) == 3:
            operations.append(
                {
                    "inputs": [inputs_op[0], inputs_op[2]],
                    "operation": inputs_op[1],
                    "output": output,
                }
            )
        i += 1

    return inputs, operations


def build_dependency_graph(operations):
    graph = defaultdict(list)
    dependencies = {}
    for i, op in enumerate(operations):
        for input_var in op["inputs"]:
            graph[input_var].append(i)
        dependencies[op["output"]] = (op["operation"], op["inputs"])
    return dependencies, graph


def evaluate_operation(operation, inputs, values):
    a = values[inputs[0]]
    b = values[inputs[1]]
    if operation == "AND":
        return a & b
    elif operation == "OR":
        return a | b
    elif operation == "XOR":
        return a ^ b


def evaluate_graph(inputs, operations):
    values = inputs.copy()
    dependencies, graph = build_dependency_graph(operations)
    ready = set()

    for output, dependency in dependencies.items():
        dependency_inputs = dependency[1]
        if all(input in inputs for input in dependency_inputs):
            ready.add(output)

    while ready:
        output = ready.pop()
        operation, inputs = dependencies[output][0], dependencies[output][1]
        values[output] = evaluate_operation(operation, inputs, values)
        for dependent_operation in graph[output]:
            dependency_inputs = operations[dependent_operation]["inputs"]
            if all(input in values for input in dependency_inputs):
                ready.add(operations[dependent_operation]["output"])

    return values


def part1(inputs, operations) -> int:
    """Solve part 1."""
    values = evaluate_graph(inputs, operations)
    z_values = {k: v for k, v in values.items() if k.startswith("z")}
    z_values_concatenated = "".join(
        str(v) for k, v in sorted(z_values.items(), reverse=True)
    )
    return int(z_values_concatenated, 2)


def part2(inputs, operations) -> int:
    pass


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    inputs, operations = parse(puzzle_input)
    solution1 = part1(inputs, operations)
    return solution1, None

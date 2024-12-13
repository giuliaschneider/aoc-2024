from scipy.optimize import linprog


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = [line.strip() for line in puzzle_input.split("\n") if line.strip()]
    systems = []

    for i in range(0, len(lines), 3):
        button_a_match = lines[i].replace("Button A: ", "").split(", ")
        a_x_coeff = int(button_a_match[0].split("+")[1])
        a_y_coeff = int(button_a_match[1].split("+")[1])

        # Parse Button B coefficients
        button_b_match = lines[i + 1].replace("Button B: ", "").split(", ")
        b_x_coeff = int(button_b_match[0].split("+")[1])
        b_y_coeff = int(button_b_match[1].split("+")[1])

        # Parse Prize values
        prize_match = lines[i + 2].replace("Prize: ", "").split(", ")
        prize_x = int(prize_match[0].split("=")[1])
        prize_y = int(prize_match[1].split("=")[1])

        systems.append(
            {
                "button_a": (a_x_coeff, a_y_coeff),
                "button_b": (b_x_coeff, b_y_coeff),
                "prize_x": prize_x,
                "prize_y": prize_y,
            }
        )

    return systems


def check_solution(system, test_a, test_b):
    if test_a < 0 or test_b < 0:
        return False

    x_test = test_a * system["button_a"][0] + test_b * system["button_b"][0]
    y_test = test_a * system["button_a"][1] + test_b * system["button_b"][1]

    return x_test == system["prize_x"] and y_test == system["prize_y"]


def calculate_score(a, b, weights=(3, 1)):
    return weights[0] * a + weights[1] * b


def solve_system(system):
    """Solve a single game system using linear programming."""
    weights = [3, 1]
    bounds = [(0, 10000000000000), (0, 10000000000000)]

    A_eq = [
        [system["button_a"][0], system["button_b"][0]],
        [system["button_a"][1], system["button_b"][1]],
    ]
    b_eq = [system["prize_x"], system["prize_y"]]
    result = linprog(weights, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")

    if not result.success:
        return 0

    # Check nearby integer solutions
    base_a, base_b = int(result.x[0]), int(result.x[1])
    for da in range(-2, 2):
        for db in range(-2, 2):
            test_a = base_a + da
            test_b = base_b + db

            if check_solution(system, test_a, test_b):
                return calculate_score(test_a, test_b)

    return 0


def part1(systems) -> int:
    """Solve part 1."""
    return sum(solve_system(system) for system in systems)


def part2(data: any) -> int:
    """Solve part 2."""
    total = 0
    for system in data:
        system["prize_x"] += 10000000000000
        system["prize_y"] += 10000000000000
        total += solve_system(system)
    return total


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

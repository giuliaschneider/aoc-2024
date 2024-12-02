import sys
import time
from importlib import import_module
from typing import Callable

from utils.parsing import read_input


def load_solution(day: int) -> Callable:
    """Load solution module for given day."""
    module = import_module(f"days.day{day:02d}")
    return module.solve


def main():
    if len(sys.argv) != 2:
        print("Usage: python run.py <day>")
        sys.exit(1)

    day = int(sys.argv[1])

    try:
        solve_puzzle = load_solution(day)
        puzzle_input = read_input(day)

        print(f"\nSolving Day {day}")
        print("=" * 40)

        start = time.perf_counter()
        solution1, solution2 = solve_puzzle(puzzle_input)
        end = time.perf_counter()

        print(f"\nPart 1: {solution1}")
        print(f"Part 2: {solution2}")
        print(f"\nTime: {(end - start)*1000:.2f}ms")

    except FileNotFoundError:
        print(f"Error: Input file for day {day} not found!")
    except ImportError:
        print(f"Error: Solution for day {day} not found!")


if __name__ == "__main__":
    main()

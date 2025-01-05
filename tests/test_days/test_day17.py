from days.day17 import parse, part1, Program
import pytest


EXAMPLE_INPUT = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""".strip()

EXAMPLE_INPUT_2 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0""".strip()


def test_parse():
    data = parse(EXAMPLE_INPUT)
    assert data is not None


@pytest.mark.parametrize(
    "register, instructions, expected_out, expected_register",
    [
        (
            {"A": 2024, "B": 0, "C": 0},
            "015430",
            "4,2,5,6,7,7,7,7,3,1,0",
            {"A": 0, "B": 0, "C": 0},
        ),
        ({"A": 0, "B": 29, "C": 0}, "17", "", {"A": 0, "B": 26, "C": 0}),
        ({"A": 0, "B": 2024, "C": 43690}, "40", "", {"A": 0, "B": 44354, "C": 43690}),
    ],
)
def test_run_program(register, instructions, expected_out, expected_register):
    program = Program(instructions, register)
    output = program.run_program()
    assert output == expected_out
    assert program.register == expected_register


def test_part1():
    registers, program = parse(EXAMPLE_INPUT)
    result = part1(registers, program)
    assert result == "4,6,3,5,6,3,5,2,1,0"

from copy import deepcopy


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = [line.strip() for line in puzzle_input.split("\n") if line.strip()]

    registers = {}

    # Parse register lines
    for line in lines:
        if line.startswith("Register"):
            parts = line.split(":")
            register = parts[0].split()[1]
            value = int(parts[1].strip())
            registers[register] = value

    # Parse program line
    program_line = [line for line in lines if line.startswith("Program:")][0]
    program = program_line.split(":")[1].strip().replace(",", "")

    return registers, program


class Program:
    def __init__(self, instructions, register):
        self.instructions = instructions
        self.register = register
        self.instruction_pointer = 0

    def get_operand_value(self, operand):
        if operand in range(4):
            return operand
        elif operand == 4:
            return self.register["A"]
        elif operand == 5:
            return self.register["B"]
        elif operand == 6:
            return self.register["C"]

        raise RuntimeError("Invalid operand")

    def perform_instruction(self, instruction, operand):
        out = []
        increase_pointer = True

        if instruction == 0:
            self.adv(operand)
        elif instruction == 1:
            self.bxl(operand)
        elif instruction == 2:
            self.bst(operand)
        elif instruction == 3:
            increase_pointer = self.jnz(operand)
        elif instruction == 4:
            self.bxc(operand)
        elif instruction == 5:
            out.append(self.out(operand))
        elif instruction == 6:
            self.bdv(operand)
        elif instruction == 7:
            self.cdv(operand)

        if increase_pointer:
            self.instruction_pointer += 2

        return out

    def adv(self, operand):
        value = self.get_operand_value(operand)
        self.register["A"] = self.register["A"] // 2**value

    def bxl(self, operand):
        self.register["B"] = self.register["B"] ^ operand

    def bst(self, operand):
        value = self.get_operand_value(operand)
        self.register["B"] = value % 8

    def jnz(self, literal_value):
        if self.register["A"] == 0:
            return True
        self.instruction_pointer = literal_value
        return False

    def bxc(self, operand):
        self.register["B"] = self.register["B"] ^ self.register["C"]

    def out(self, operand):
        value = self.get_operand_value(operand)
        return str(value % 8)

    def bdv(self, operand):
        value = self.get_operand_value(operand)
        self.register["B"] = self.register["A"] // 2**value

    def cdv(self, operand):
        value = self.get_operand_value(operand)
        self.register["C"] = self.register["A"] // 2**value

    def run_program(self):
        out = []
        while self.instruction_pointer < len(self.instructions):
            instruction = int(self.instructions[self.instruction_pointer])
            operand = int(self.instructions[self.instruction_pointer + 1])
            out += self.perform_instruction(instruction, operand)

        return ",".join(out)


def part1(registers, program) -> int:
    """Solve part 1."""
    program = Program(program, registers)
    return program.run_program()


def part2(registers, program) -> int:
    """Solve part 2."""
    original = deepcopy(registers)
    final_a = 0
    for i, value in enumerate(program):
        for a in range(8):
            register = deepcopy(original)
            temp_a = final_a * 8 + a
            register["A"] = temp_a

            output = Program(program, register).run_program()
            if output == ",".join(program[-i - 1 :]):
                print(output)
                print(final_a)
                final_a = temp_a
    return final_a


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    registers, program = parse(puzzle_input)
    solution1 = part1(registers, program)
    solution2 = part2(registers, program)
    return solution1, solution2

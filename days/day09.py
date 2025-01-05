from collections import deque


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = puzzle_input.split("\n")
    first_line = lines[0] if lines else ""

    memory_space = []
    free = deque()
    files = deque()

    for i, char in enumerate(first_line):
        if (i % 2) == 0:  # files
            index = int(i / 2)
            files.append((len(memory_space), index, int(char)))
            memory_space += [index] * int(char)
        else:  # free
            free.append((len(memory_space), int(char)))
            memory_space += ["."] * int(char)

    return memory_space, free, files


def calculate_checksum(memeory_space) -> int:
    checksum = 0
    for i, value in enumerate(memeory_space):
        if value == ".":
            continue
        checksum += value * i
    return checksum


def part1(memeory_space, free) -> int:
    """Solve part 1."""
    index_last_file = len(memeory_space) - 1
    while free:
        index, value = free.popleft()
        for i in range(value):
            index_next_free_space = index + i
            while memeory_space[index_last_file] == "." and index_last_file > index:
                index_last_file -= 1
            while (
                memeory_space[index_next_free_space] != "."
                and index_next_free_space < index_last_file
            ):
                index_next_free_space += 1
            memeory_space[index_next_free_space] = memeory_space[index_last_file]
            if index_last_file > index_next_free_space:
                memeory_space[index_last_file] = "."

            if index_last_file == index_next_free_space:
                break

    return calculate_checksum(memeory_space)


def find_free_spaces(memeory_space):
    free_spaces = []
    i = 0
    while i < len(memeory_space):
        if memeory_space[i] == ".":
            start_index = i
            count = 0
            while i < len(memeory_space) and memeory_space[i] == ".":
                count += 1
                i += 1
            free_spaces.append((start_index, count))
        else:
            i += 1
    return free_spaces


def part2(memeory_space, free, files) -> int:
    """Solve part 2."""
    free_list = []
    while free:
        free_list.append(free.popleft())

    while files:
        file_index, _, file_space = files.pop()

        for index, free_space in free_list:
            if free_space >= file_space:
                free_list.remove((index, free_space))
                break


        if file_index <= index:
            continue

        for i in range(free_space):
            if i > file_space - 1:
                break

            index_next_free_space = index + i
            index_file_space = file_index + i
            memeory_space[index_next_free_space] = memeory_space[index_file_space]
            memeory_space[index_file_space] = "."

        free_list = find_free_spaces(memeory_space)

    return calculate_checksum(memeory_space)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    memeory_space, free, files = parse(puzzle_input)
    solution1 = part1(memeory_space, free)
    memeory_space, free, files = parse(puzzle_input)
    solution2 = part2(memeory_space, free, files)
    return solution1, solution2

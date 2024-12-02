def read_input(day: int) -> str:
    """Read the input file for a given day"""
    with open(f"inputs/day{day:02d}.txt") as f:
        return f.read().strip()

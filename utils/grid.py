from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    """Represents a 2D position with vector operations."""

    x: int
    y: int

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Position(self.x * scalar, self.y * scalar)

"""
Liskov Substitution Principle (LSP)
-------------------------------------
Objects of a superclass should be replaceable with objects of a subclass
without breaking the correctness of the program.

CLASSIC PITFALL: Modelling a Square as a subclass of Rectangle. A Square
"is-a" Rectangle geometrically, but forcing width == height breaks any
code that expects a Rectangle's width and height to be independently
settable -> LSP violation.

FIX: Use a common abstraction (Shape) instead of inheriting Square from
Rectangle.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Square(Shape):
    """Square no longer pretends to be a Rectangle; it independently
    satisfies the Shape contract, so it can safely substitute for any
    Shape without surprising callers."""

    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side * self.side


def print_area(shape: Shape) -> None:
    """Works correctly no matter which Shape subclass is passed in --
    that's LSP in action."""
    print(f"{type(shape).__name__} area: {shape.area()}")


if __name__ == "__main__":
    shapes = [Rectangle(4, 5), Square(4)]
    for s in shapes:
        print_area(s)

    assert Rectangle(4, 5).area() == 20
    assert Square(4).area() == 16
    print("All LSP checks passed.")

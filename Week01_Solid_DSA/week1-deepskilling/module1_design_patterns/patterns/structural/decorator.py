"""
Structural Pattern: Decorator
--------------------------------
Attaches additional responsibilities to an object dynamically.
Decorators provide a flexible alternative to subclassing for extending
functionality.

Example: a basic Coffee object, decorated with Milk / Sugar add-ons,
each adding to cost and description without modifying the Coffee class
itself.
"""

from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def cost(self) -> float:
        ...

    @abstractmethod
    def description(self) -> str:
        ...


class Coffee(Beverage):
    def cost(self) -> float:
        return 50.0

    def description(self) -> str:
        return "Coffee"


class BeverageDecorator(Beverage):
    """Base decorator: wraps a Beverage and delegates to it."""

    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def cost(self) -> float:
        return self._beverage.cost()

    def description(self) -> str:
        return self._beverage.description()


class MilkDecorator(BeverageDecorator):
    def cost(self) -> float:
        return self._beverage.cost() + 10.0

    def description(self) -> str:
        return f"{self._beverage.description()} + Milk"


class SugarDecorator(BeverageDecorator):
    def cost(self) -> float:
        return self._beverage.cost() + 5.0

    def description(self) -> str:
        return f"{self._beverage.description()} + Sugar"


if __name__ == "__main__":
    order = SugarDecorator(MilkDecorator(Coffee()))
    print(f"{order.description()} costs Rs.{order.cost()}")

    assert order.cost() == 65.0
    assert order.description() == "Coffee + Milk + Sugar"
    print("Decorator checks passed.")

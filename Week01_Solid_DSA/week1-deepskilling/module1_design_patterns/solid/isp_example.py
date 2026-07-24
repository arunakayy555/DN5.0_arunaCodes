"""
Interface Segregation Principle (ISP)
----------------------------------------
Clients should not be forced to depend on methods/interfaces they do
not use. Prefer several small, specific interfaces over one large,
general-purpose interface.

BAD: A single "Worker" interface with work() and eat() forces a Robot
(which doesn't eat) to implement a meaningless eat() method.

GOOD: Split into smaller interfaces (Workable, Eatable) and let each
class implement only what applies to it.
"""

from abc import ABC, abstractmethod


class Workable(ABC):
    @abstractmethod
    def work(self) -> str:
        ...


class Eatable(ABC):
    @abstractmethod
    def eat(self) -> str:
        ...


class HumanWorker(Workable, Eatable):
    def work(self) -> str:
        return "Human is working."

    def eat(self) -> str:
        return "Human is eating lunch."


class RobotWorker(Workable):
    """Robot only implements the interface that's relevant to it --
    it is never forced to define a meaningless eat() method."""

    def work(self) -> str:
        return "Robot is working."


if __name__ == "__main__":
    human = HumanWorker()
    robot = RobotWorker()

    print(human.work())
    print(human.eat())
    print(robot.work())

    assert isinstance(human, Workable) and isinstance(human, Eatable)
    assert isinstance(robot, Workable) and not isinstance(robot, Eatable)
    print("All ISP checks passed.")

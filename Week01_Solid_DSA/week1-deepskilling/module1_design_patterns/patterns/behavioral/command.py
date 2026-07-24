"""
Behavioral Pattern: Command
------------------------------
Encapsulates a request as an object, letting you parameterize clients
with different requests, queue/log requests, and support undoable
operations.

Example: a simple text editor supporting Type / Undo via Command
objects, orchestrated by an Invoker (CommandManager).
"""

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        ...

    @abstractmethod
    def undo(self) -> None:
        ...


class TextDocument:
    def __init__(self):
        self.content = ""


class TypeTextCommand(Command):
    def __init__(self, document: TextDocument, text: str):
        self._document = document
        self._text = text

    def execute(self) -> None:
        self._document.content += self._text

    def undo(self) -> None:
        self._document.content = self._document.content[: -len(self._text)]


class CommandManager:
    """The Invoker: executes commands and keeps a history for undo."""

    def __init__(self):
        self._history = []

    def execute(self, command: Command) -> None:
        command.execute()
        self._history.append(command)

    def undo_last(self) -> None:
        if self._history:
            command = self._history.pop()
            command.undo()


if __name__ == "__main__":
    doc = TextDocument()
    manager = CommandManager()

    manager.execute(TypeTextCommand(doc, "Hello, "))
    manager.execute(TypeTextCommand(doc, "World!"))
    print(repr(doc.content))

    manager.undo_last()
    print(repr(doc.content))

    assert doc.content == "Hello, "
    manager.undo_last()
    assert doc.content == ""
    print("Command checks passed.")

"""
Dependency Inversion Principle (DIP)
----------------------------------------
High-level modules should not depend on low-level modules; both should
depend on abstractions. Abstractions should not depend on details;
details should depend on abstractions.

BAD: A NotificationService that directly instantiates and depends on a
concrete EmailSender. Swapping in SMS later means editing
NotificationService itself.

GOOD: NotificationService depends only on a MessageSender abstraction.
Concrete senders (Email, SMS) are "injected" -- easy to add new
channels without touching NotificationService.
"""

from abc import ABC, abstractmethod


class MessageSender(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        ...


class EmailSender(MessageSender):
    def send(self, message: str) -> str:
        return f"Email sent: {message}"


class SMSSender(MessageSender):
    def send(self, message: str) -> str:
        return f"SMS sent: {message}"


class NotificationService:
    """High-level module. Depends on the MessageSender abstraction,
    never on a concrete class -- that dependency is inverted/injected
    from outside."""

    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, message: str) -> str:
        return self.sender.send(message)


if __name__ == "__main__":
    email_service = NotificationService(EmailSender())
    sms_service = NotificationService(SMSSender())

    print(email_service.notify("Your order has shipped."))
    print(sms_service.notify("Your OTP is 123456."))

    assert email_service.notify("hi").startswith("Email sent")
    assert sms_service.notify("hi").startswith("SMS sent")
    print("All DIP checks passed.")

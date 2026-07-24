"""
Behavioral Pattern: Strategy
-------------------------------
Defines a family of interchangeable algorithms, encapsulates each one,
and lets the algorithm vary independently of the clients that use it.

Example: a PaymentContext that can pay using different strategies
(Credit Card, UPI, Wallet) chosen at runtime.
"""

from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        ...


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid Rs.{amount} using Credit Card."


class UPIPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid Rs.{amount} using UPI."


class WalletPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid Rs.{amount} using Wallet."


class PaymentContext:
    """Holds a reference to a strategy and delegates the pay() call to
    it -- the algorithm can be swapped at runtime without changing this
    class."""

    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def checkout(self, amount: float) -> str:
        return self._strategy.pay(amount)


if __name__ == "__main__":
    cart = PaymentContext(CreditCardPayment())
    print(cart.checkout(500))

    cart.set_strategy(UPIPayment())
    print(cart.checkout(250))

    cart.set_strategy(WalletPayment())
    print(cart.checkout(100))

    assert cart.checkout(100) == "Paid Rs.100 using Wallet."
    print("Strategy checks passed.")

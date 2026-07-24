"""
Open/Closed Principle (OCP)
----------------------------
Software entities should be OPEN for extension but CLOSED for
modification. Adding new behaviour should not require editing existing,
already-tested code.

Example: computing discounts for different customer types. Instead of a
giant if/elif chain in a single function (which we'd have to edit every
time a new customer type appears), we use an abstract base class and
let each discount strategy extend it.
"""

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: float) -> float:
        ...


class NoDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price


class RegularCustomerDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.95  # 5% off


class PremiumCustomerDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.80  # 20% off


class StudentDiscount(DiscountStrategy):
    """New requirement added WITHOUT touching any existing class."""

    def apply_discount(self, price: float) -> float:
        return price * 0.90  # 10% off


class PriceCalculator:
    """Closed for modification: never needs to change when a new
    discount type is introduced, because it only depends on the
    DiscountStrategy abstraction."""

    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def final_price(self, price: float) -> float:
        return round(self.strategy.apply_discount(price), 2)


if __name__ == "__main__":
    price = 1000.0

    calculators = {
        "No discount": PriceCalculator(NoDiscount()),
        "Regular": PriceCalculator(RegularCustomerDiscount()),
        "Premium": PriceCalculator(PremiumCustomerDiscount()),
        "Student": PriceCalculator(StudentDiscount()),
    }

    for label, calc in calculators.items():
        print(f"{label}: {calc.final_price(price)}")

    assert PriceCalculator(NoDiscount()).final_price(1000) == 1000.0
    assert PriceCalculator(RegularCustomerDiscount()).final_price(1000) == 950.0
    assert PriceCalculator(PremiumCustomerDiscount()).final_price(1000) == 800.0
    assert PriceCalculator(StudentDiscount()).final_price(1000) == 900.0
    print("All OCP checks passed.")

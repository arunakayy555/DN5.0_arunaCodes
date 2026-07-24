"""
Structural Pattern: Adapter
------------------------------
Converts the interface of a class into another interface clients
expect. Lets otherwise-incompatible classes work together.

Example: our app expects a `.get_data()` method, but a third-party
library only exposes `.fetch_legacy_data()`. We wrap it in an adapter.
"""

from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def get_data(self) -> str:
        ...


# --- Third-party / legacy class we cannot modify ---
class LegacyXMLLibrary:
    def fetch_legacy_data(self) -> str:
        return "<data>legacy xml payload</data>"


class LegacyXMLAdapter(DataSource):
    """Adapts LegacyXMLLibrary's interface to the DataSource interface
    our application code expects."""

    def __init__(self, legacy_lib: LegacyXMLLibrary):
        self._legacy_lib = legacy_lib

    def get_data(self) -> str:
        raw_xml = self._legacy_lib.fetch_legacy_data()
        return f"[adapted] {raw_xml}"


class ModernJSONSource(DataSource):
    def get_data(self) -> str:
        return '{"data": "modern json payload"}'


def print_data(source: DataSource) -> None:
    print(source.get_data())


if __name__ == "__main__":
    legacy_adapter = LegacyXMLAdapter(LegacyXMLLibrary())
    modern_source = ModernJSONSource()

    print_data(legacy_adapter)
    print_data(modern_source)

    assert legacy_adapter.get_data().startswith("[adapted]")
    print("Adapter checks passed.")

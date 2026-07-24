"""
Single Responsibility Principle (SRP)
--------------------------------------
A class should have only ONE reason to change, i.e. it should have only
one job/responsibility.

BAD DESIGN: Report class both builds the report content AND knows how
to save it to disk. Two responsibilities mixed into one class.

GOOD DESIGN: Split into Report (owns content) and ReportSaver (owns
persistence). Each class now has a single reason to change.
"""


# ---------------------------------------------------------------------------
# BAD EXAMPLE (violates SRP) - kept here only for comparison/reference
# ---------------------------------------------------------------------------
class BadReport:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def format_report(self):
        return f"{self.title}\n{'=' * len(self.title)}\n{self.body}"

    def save_to_file(self, filename):
        # Persistence logic does NOT belong in a "Report" class.
        with open(filename, "w") as f:
            f.write(self.format_report())


# ---------------------------------------------------------------------------
# GOOD EXAMPLE (follows SRP)
# ---------------------------------------------------------------------------
class Report:
    """Responsible ONLY for holding and formatting report content."""

    def __init__(self, title: str, body: str):
        self.title = title
        self.body = body

    def format_report(self) -> str:
        return f"{self.title}\n{'=' * len(self.title)}\n{self.body}"


class ReportSaver:
    """Responsible ONLY for persisting a report somewhere."""

    @staticmethod
    def save_to_file(report: Report, filename: str) -> None:
        with open(filename, "w") as f:
            f.write(report.format_report())


if __name__ == "__main__":
    report = Report("Weekly Status", "Everything is on track.")
    print(report.format_report())

    ReportSaver.save_to_file(report, "/tmp/weekly_status.txt")
    print("\nSaved report to /tmp/weekly_status.txt")

    # simple sanity checks
    assert report.format_report().startswith("Weekly Status")
    with open("/tmp/weekly_status.txt") as f:
        assert f.read() == report.format_report()
    print("All SRP checks passed.")

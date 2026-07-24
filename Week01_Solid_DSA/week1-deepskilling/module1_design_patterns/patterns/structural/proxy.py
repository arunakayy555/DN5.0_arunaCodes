"""
Structural Pattern: Proxy
----------------------------
Provides a surrogate/placeholder for another object to control access
to it -- e.g. lazy loading, access control, caching, or logging.

Example: a ProtectedDatabase proxy that checks a user's role before
allowing access to the real Database object.
"""

from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def query(self, sql: str) -> str:
        ...


class RealDatabase(Database):
    def query(self, sql: str) -> str:
        return f"Executed: {sql}"


class ProtectedDatabaseProxy(Database):
    """Controls access to RealDatabase based on the caller's role,
    without the caller needing to know a proxy is involved."""

    def __init__(self, real_db: RealDatabase, user_role: str):
        self._real_db = real_db
        self._user_role = user_role

    def query(self, sql: str) -> str:
        if self._user_role != "admin" and sql.strip().lower().startswith(
            ("delete", "drop", "update")
        ):
            return "Access denied: insufficient privileges."
        return self._real_db.query(sql)


if __name__ == "__main__":
    admin_db = ProtectedDatabaseProxy(RealDatabase(), user_role="admin")
    guest_db = ProtectedDatabaseProxy(RealDatabase(), user_role="guest")

    print(admin_db.query("DELETE FROM users"))
    print(guest_db.query("DELETE FROM users"))
    print(guest_db.query("SELECT * FROM users"))

    assert admin_db.query("DELETE FROM users").startswith("Executed")
    assert guest_db.query("DELETE FROM users").startswith("Access denied")
    assert guest_db.query("SELECT * FROM users").startswith("Executed")
    print("Proxy checks passed.")

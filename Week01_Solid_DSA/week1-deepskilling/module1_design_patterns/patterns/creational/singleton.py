"""
Creational Pattern: Singleton
-------------------------------
Ensures a class has only ONE instance and provides a global point of
access to it. Common use case: a single shared configuration/logger/
connection-pool object across an app.
"""


class AppConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {}
        return cls._instance

    def set(self, key: str, value):
        self.settings[key] = value

    def get(self, key: str):
        return self.settings.get(key)


if __name__ == "__main__":
    config1 = AppConfig()
    config1.set("env", "production")

    config2 = AppConfig()  # same instance as config1
    print(config2.get("env"))

    assert config1 is config2
    assert config2.get("env") == "production"
    print("Singleton checks passed.")

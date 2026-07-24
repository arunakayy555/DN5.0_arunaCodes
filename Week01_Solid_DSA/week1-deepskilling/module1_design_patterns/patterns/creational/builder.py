"""
Creational Pattern: Builder
------------------------------
Separates the construction of a complex object from its representation,
so the same construction process can create different representations.
Useful when an object has many optional parts/parameters.
"""


class Computer:
    def __init__(self):
        self.cpu = None
        self.ram_gb = None
        self.storage_gb = None
        self.gpu = None

    def __str__(self):
        return (
            f"Computer(cpu={self.cpu}, ram={self.ram_gb}GB, "
            f"storage={self.storage_gb}GB, gpu={self.gpu})"
        )


class ComputerBuilder:
    """Builds up a Computer step by step; each method returns self so
    calls can be chained (fluent interface)."""

    def __init__(self):
        self._computer = Computer()

    def set_cpu(self, cpu: str) -> "ComputerBuilder":
        self._computer.cpu = cpu
        return self

    def set_ram(self, ram_gb: int) -> "ComputerBuilder":
        self._computer.ram_gb = ram_gb
        return self

    def set_storage(self, storage_gb: int) -> "ComputerBuilder":
        self._computer.storage_gb = storage_gb
        return self

    def set_gpu(self, gpu: str) -> "ComputerBuilder":
        self._computer.gpu = gpu
        return self

    def build(self) -> Computer:
        return self._computer


if __name__ == "__main__":
    gaming_pc = (
        ComputerBuilder()
        .set_cpu("Intel i9")
        .set_ram(32)
        .set_storage(2000)
        .set_gpu("RTX 4090")
        .build()
    )
    print(gaming_pc)

    budget_pc = ComputerBuilder().set_cpu("Intel i3").set_ram(8).set_storage(256).build()
    print(budget_pc)

    assert gaming_pc.gpu == "RTX 4090"
    assert budget_pc.gpu is None
    print("Builder checks passed.")

from abc import ABC, abstractmethod

# The Product class
class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"Computer(cpu={self.cpu}, gpu={self.gpu}, ram={self.ram}, storage={self.storage})"

# Abstract Builder class using the ABC module
class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self, cpu):
        pass

    @abstractmethod
    def set_gpu(self, gpu):
        pass

    @abstractmethod
    def set_ram(self, ram):
        pass

    @abstractmethod
    def set_storage(self, storage):
        pass

    @abstractmethod
    def build(self):
        pass

# Concrete Builder implementing the abstract methods
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()  # Initialize an empty Computer object

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def build(self):
        return self.computer  # Return the fully constructed Computer object

# Client code demonstrating the use of the builder
if __name__ == "__main__":
    # Build a gaming computer with custom configurations
    gaming_pc = (GamingComputerBuilder()
                 .set_cpu("Intel Core i9")
                 .set_gpu("NVIDIA RTX 3080")
                 .set_ram("32GB")
                 .set_storage("1TB SSD")
                 .build())
    print(gaming_pc)

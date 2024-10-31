from copy import deepcopy

class Prototype:
    def clone(self):
        raise NotImplementedError("You should implement this method!")

class ConcretePrototypeA(Prototype):
    def __init__(self, name):
        self.name = name

    def clone(self):
        return deepcopy(self)

class ConcretePrototypeB(Prototype):
    def __init__(self, value):
        self.value = value

    def clone(self):
        return deepcopy(self)

class Client:
    def __init__(self):
        self.prototypes = {
            "A": ConcretePrototypeA("Prototype A"),
            "B": ConcretePrototypeB(100)
        }

    def create_prototype(self, prototype_type):
        prototype = self.prototypes.get(prototype_type)
        return prototype.clone() if prototype else None

# Usage
client = Client()
prototype_a = client.create_prototype("A")
prototype_b = client.create_prototype("B")

print(prototype_a.name)  # Output: Prototype A
print(prototype_b.value)  # Output: 100

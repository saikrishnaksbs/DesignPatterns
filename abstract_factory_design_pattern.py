from abc import ABC, abstractmethod

# Abstract Product
class Letters(ABC):
    @abstractmethod
    def show(self, letter):
        pass

# Concrete Products
class SmallLetter(Letters):
    def show(self, letter):
        print(letter.lower())

class CapitalLetter(Letters):
    def show(self, letter):
        print(letter.upper())

# Abstract Factory
class LetterFactory(ABC):
    @abstractmethod
    def create_letter(self) -> Letters:
        pass

# Concrete Factories
class SmallLetterFactory(LetterFactory):
    def create_letter(self) -> Letters:
        return SmallLetter()

class CapitalLetterFactory(LetterFactory):
    def create_letter(self) -> Letters:
        return CapitalLetter()

# Client code
def main():
    # Use the SmallLetterFactory
    factory = SmallLetterFactory()
    letter_instance = factory.create_letter()
    letter_instance.show('ASDFGHJGFD')

    # Use the CapitalLetterFactory
    factory = CapitalLetterFactory()
    letter_instance = factory.create_letter()
    letter_instance.show('asdfghjgfd')

if __name__ == '__main__':
    main()

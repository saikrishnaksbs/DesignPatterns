from abc import ABC, abstractmethod

class Letters(ABC):
    
    @abstractmethod
    def show(self, letter):
        pass

class small_letter(Letters):
    def show(self, letter):
        print(letter.lower())
    
class capital_letter(Letters):
    def show(self, letter):
        print(letter.upper())
        
class Choose_small_or_capital():
    
    @staticmethod
    def choose(function):
        if function == 'small':
            return small_letter()
        if function == 'capital':
            return capital_letter()
        else:
            return None
    
def main():
    function = Choose_small_or_capital.choose('capital')
    function.show('asdfghjgfdsgdsfgfdsdgfds')
    function = Choose_small_or_capital.choose('small')
    function.show('FGSHDJFDSGDHFJGFDSGDHFDS')
    
if __name__ == '__main__':
    main()
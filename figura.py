
from abc import ABC, abstractmethod

#clase abtracta, porque tiene al menos un método abstracto
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
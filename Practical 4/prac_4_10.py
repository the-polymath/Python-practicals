''' 4.10 Write a python program in which Maruti and Santro sub classes implement the abstract methods
of the super class Car. '''

from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def color(self):
        pass

class Maruti(Car):
    def __init__(self):
        print("This is Maruti Class")

    def color(self):
        print("Maruti is Suzuki")

class Santro(Car):
    def __init__(self):
        print("This is Santro")

    def color(self):
        print("Santro is Hyundai!!")

m = Maruti()
m.color()
s = Santro()
s.color()

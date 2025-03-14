from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("Car is Starting by Gear.")

class bike(vehicle):
    def start(self):
        print("Bike is Satrting with Button.") 

car1 =car()
bike1=bike()
car1.start()
bike1.start()      
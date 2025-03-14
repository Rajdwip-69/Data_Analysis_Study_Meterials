class Animal:
    def speak(self):
        print("Animal Makes Sound")
class Dog(Animal):
    def bark(self):
        print("The dog is Barking")


dog1 = Dog()
print(dog1.speak())
print(dog1.bark())
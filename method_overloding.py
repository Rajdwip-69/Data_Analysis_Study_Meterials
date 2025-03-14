class Bird:
    def sound(self):
        print("Birds Makes Sound")
class crow(Bird):
    def sound(self):
        print("Crow Sound is Caw Caw")
class parrot(Bird):
    def sound(self):
        print("Parrot Makes Sound Squak")


bird1 = Bird()
crow1 = crow()
parrot1 = parrot()
bird1.sound()
crow1.sound()
parrot1.sound()         
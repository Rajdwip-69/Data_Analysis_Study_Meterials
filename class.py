class car:
    def set_details(self,model,color):
        self.model = model
        self.color = color
    def show_details(self):
        print(f'The car is {self.model} and color is {self.color}')


car1 = car()
car1.set_details("Tesla","Red")

car2=car()
car2.set_details("BMW","Black")

car3=car()
car3.set_details("Toyota","White")

car1.show_details()
car2.show_details()
car3.show_details()
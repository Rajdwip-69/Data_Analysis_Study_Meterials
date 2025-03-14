# class car:
#     def __init__(self,model,color):
#         self.model = model
#         self.color = color

#     def show_details(self):
#         print(f'The car is {self.model} and color is {self.color}')

# car1= car("Tesla","Black")
# car1.show_details()


class Car:
    def __init__(self, model, color):  # Corrected 'sef' to 'self'
        self.model = model
        self.color = color

    def show_details(self):  # Added 'self' as a parameter
        print(f'The car is {self.model} and color is {self.color}')

car1 = Car("Tesla", "Black")  # Corrected object creation
car2= Car("BMW","Blue")
car1.show_details()  # Calling method on the object
car2.show_details()


           
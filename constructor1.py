class student:
    def __init__(self,name,rollno,age,marks_cs):
        self.name= name
        self.rollno = rollno
        self.age = age
        self.marks_cs = marks_cs
    def display(self):
        print(f'Details of student is \n Name: {self.name},\nAge:{self.age},\nRollNO :{self.rollno},\nMarks_CS:{self.marks_cs}')  


student1 = student("RAJDWIP",193,22,100)
student2=student("AMIT",7,21,77)
student1.display() 
student2.display()         
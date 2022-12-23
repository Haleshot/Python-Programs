# Srihari Thyagarajan
# I066
# B Tech, Artificial Intelligence
# Experiment 8

class Cars:
    
    def __init__(self, colour, price):
        self.color = colour
        self.price = price

    def display(self):
        print(self.color, self.price)


class Student:
    
    def __init__(self):
        self.Name = input("Enter the Name of the Student : ")
        self.Marks = float(input("Enter the Marks of the Student : "))
        self.Subject = input("Enter the Sunject of the Student : ")


    def display(self):
        print(self.Name, "has scored", self.Marks, "marks in", self.Subject, "!")



def main():
    car1 = Cars("Red", 40)
    car1.display()

    student = Student()
    student.display()

main()
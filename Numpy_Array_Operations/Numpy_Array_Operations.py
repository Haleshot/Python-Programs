# Srihari Thyagarajan
# I066
# B Tech, Artificial Intelligence
# Experiment 9

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Main Function
def main():
    run = True
    while(run):
        print("\nMenu\n\
1. Addition and Subtraction of two arrays.(3x3) .\n\
2. Addition of Array elements(Row wise/Column wise/complete) .\n\
3. Square and Square root of Array1 elements. \n\
4. Generate a sine wave and cosine wave using numpy and plot the same using matplotlib. \n\
5. Use transpose, fliplr, flipud, rot90 on a 2D array. \n\
6. Perform matrix multiplication using numpy.dot(). \n\
7. Exit. \n\
Enter Your Choice : ")

        ch = int(input())


        if ch == 1:
            
            array_1 = np.array([1, 2, 3])
            array_2 = np.array([4, 5, 6])

            print(array_1)
            print(array_2)
            print()

            print("The Addition of the two Arrays are is : ", np.add(array_1, array_2))
            print("The Subtraction of the two Arrays are is : ", np.subtract(array_1, array_2))

            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


        elif ch == 2:
            array_1 = np.array([[1, 2, 3], [4, 5, 6]])
            array_2 = np.array([[4, 5, 6], [7, 8, 9]])

            print(array_1)
            print(array_2)
            print()
            
            
            print("The Sum of the Elements in the List 1 Row - Wise", np.sum(array_1, axis = 0))
            print("The Sum of the Elements in the List 2 Row - Wise", np.sum(array_2, axis = 0))
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 3:
            array_1 = np.array([[1, 2, 3], [4, 5, 6]])
            array_2 = np.array([[4, 5, 6], [7, 8, 9]])

            print()
            print(array_1)
            print(array_2)
            print()
            
            
            print("The Square of the Elements in the List 1 \n", np.square(array_1))
            print("The Square of the Elements in the List 2 \n", np.square(array_2))

            print("The Square Root of the Elements in the List 1 \n", np.sqrt(array_1))
            print("The Square Root of the Elements in the List 2 \n", np.sqrt(array_2))

            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 4:
            x = np.linspace(np.pi, 100)
            t = np.sin(x)
            plt.plot(t)
            plt.title("Sine Wave")
            plt.show()


            x = np.linspace(np.pi, 100)
            t = np.cos(x)
            plt.plot(t)
            plt.title("Cosine Wave")
            plt.show()

            
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 5:
            array_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

            print(array_1)

            print("The Transpose of the Elements in the List \n", np.transpose(array_1))
            print("Flipping the Elements in the List horizonatally \n", np.fliplr(array_1))
            print("Flipping the Elements in the List vertically \n", np.flipud(array_1))
            print("Rotating the Elements in the List by 90 degrees \n", np.rot90(array_1))

            
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 6:
            array_1 = np.array([[23,44,67],[6,2,9],[6,7,45]])
            array_2 = np.array([[3,2,28],[10,23,42],[75,4,66]])

            print()
            print(array_1)
            print(array_2)
            print()

            result = np.dot(array_1, array_2)


            print("The Dot product of the two Arrays are is : ", result)

            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))



        elif ch == 7:
            print("Thank You!")
            exit(0)

        else:
            print("Invalid Choice!")
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


main()
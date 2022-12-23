# PP Experiment 6
# Srihari Thyagarajan, I066, Batch - B3

# import modules
import random
import math

# Main Function
def main():
    run = True
    while(run):
        print("Menu\n\
1. Check if Integer entered is Positive/ Negative/ Multiple of 3 or not/ Even or Odd.\n\
2. Evaluating Grades for a Student.\n\
3. Game Calculating Number of Points. \n\
4. Exit \n\
Enter Your Choice : ")

        ch = int(input())


        if ch == 1:
            
            integer = int(input("Enter the Value of the Integer to be checked : "))
        
            
            if (integer > 0):
                if (integer % 2 == 0):
                    print("The Integer is Positive and is Even.")
                elif (integer % 2 == 1  ):
                    print("The Integer is Positive and is Odd.")

            elif (integer < 0):
                print("The Integer is Negative.")


            if (integer % 3 == 0):
                print("The Integer is a multiple of 3.")


            elif (integer % 3 != 0):
                print("The Integer is not a multiple of 3.")

            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


        elif ch == 2:
            
            marks = int(input("Enter the Marks of the Student : "))

            if (marks > 75 and marks <= 100):
                print("The Student has achieved a High Grade!")

            elif (marks > 50 and marks <= 75):
                print("The Student has achieved a Medium Grade.")

            elif (marks < 50):
                print("The Student has achieved a Low Grade")

            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 3:
            
            geeta_turn = 0
            seeta_turn = 0
            
            geeta_points = 0
            seeta_points = 0

            limit = int(input("Enter the Number of Iterations : "))

            for i in range(limit):
                geeta_turn = random.randint(1, 50)
                seeta_turn = random.randint(1, 50)


                root_points_geeta = math.sqrt(geeta_turn)
                root_points_seeta = math.sqrt(seeta_turn)

                if(geeta_turn % 2 == 0):
                    geeta_points += 2
                
                if(seeta_turn % 2 == 0):
                    seeta_points += 2

                if(geeta_turn % 2 == 1):
                    geeta_points += 3
                
                if(seeta_turn % 2 == 1):
                    seeta_points += 3
                
                if(int(root_points_geeta + 0.5) ** 2 == geeta_turn):
                    geeta_points += 4
                
                if(int(root_points_seeta + 0.5) ** 2 == seeta_turn):
                    seeta_points += 4
            
            print("The Total Points accumulated by Geeta is : ", geeta_points)
            print("The Total Points accumulated by Seeta is : ", seeta_points)

            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 4:
            print("Thank You!")
            exit(0)

        else:
            print("Invalid Choice!")
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


main()
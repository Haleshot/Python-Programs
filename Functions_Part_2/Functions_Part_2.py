# Srihari Thyagarajan
# I066
# B Tech, Artificial Intelligence
# Experiment 7

# Function to find the difference of two numbers.
from math import factorial


def difference(n1, n2):
    return n1 - n2


# Function to add Numbers to a list.
def add_nos(l1):
    sum = 0
    for i in l1:
        sum += i
    return sum


# Function to find the Factorial of a number.
def Fact(n1):
    if n1 == 0 or n1 == 1:
        return 1    
    else:
        return n1 * Fact(n1 - 1)


# Function to search for a specific string in a phrase
def Specific(a, b):
    if b in a:
        return 1
    return 0


# Function to find the LCM of two numbers
def LCM(n1, n2):
    maximum = max(n1, n2)
    
    while 1:
        if((maximum % n1 == 0) and (maximum % n2 == 0)):
            lcm = maximum
            break
        maximum += 1

    return lcm

# Function to find the Prime Numbers in a given range.
def Prime(n1, n2):
    prime_nos = [] # For storing the prime numbers to return as a list.
    for i in range(n1, n2 + 1):
        if (i > 1):
            for j in range(2, int(i/2) + 1):
                if (i % j == 0):
                    break
            else:
                prime_nos.append(i)
                
    return prime_nos




# Main Function
def main():
    run = True
    while(run):
        print("\nMenu\nFunctions\n\
1. To Find the difference between two Numbers.\n\
2. To add numbers to a list.\n\
3. To find the factorial of a number. \n\
4. To search for a specific string in a phrase. \n\
5. To find the LCM of two numbers. \n\
6. To find Prime numbers in a given range. \n\
7. Exit. \n\
Enter Your Choice : ")

        ch = int(input())


        if ch == 1:
            
            integer_1 = int(input("Enter Number 1 : "))
            integer_2 = int(input("Enter Number 2 : "))

            print("The Difference between the two numbers is : ", difference(integer_1, integer_2))

            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


        elif ch == 2:
            l = [2, 4, 6, 7]
            
            result = add_nos(l)
            print("The Sum of the Elements in the List ",  l, " is : ", result)
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 3:
            value = int(input("Enter the Number whose factorial is to be found : "))
            print("The Factorial of the Number is : ", Fact(value))

            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 4:
            sentence = input("Enter the Sentence : ")
            phrase = input("Enter the Phrase to be checked in the above sentence : ")
            result = Specific(sentence, phrase)
            if result == 1:
                print("The Phrase exists in the Sentence!")
            else:
                print("The Phrase does not exist in the Sentence!")
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 5:
            integer_1 = int(input("Enter Number 1 : "))
            integer_2 = int(input("Enter Number 2 : "))

            result = LCM(integer_1, integer_2)
            print("The LCM of the 2 Numbers is : ", result)
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 6:
            lower_limit = int(input("Enter the Lower Limit : "))
            upper_limit = int(input("Enter the Higher Limit : "))
            result = Prime(lower_limit, upper_limit)
            print("The Range is given as : \n", result)
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))



        elif ch == 7:
            print("Thank You!")
            exit(0)

        else:
            print("Invalid Choice!")
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


main()
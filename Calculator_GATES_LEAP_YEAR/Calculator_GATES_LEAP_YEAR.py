# Simple Calculator
# PP Experiment 1
# Srihari Thyagarajan, I066, Batch - B3

run = True
while(run):

    n1 = int(input("Enter the value of Number 1 : "))
    n2 = int(input("Enter the value of Number 2 : "))
    print("\nMenu\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Calculating the Remainder\nEnter your Choice : ")
    ch = int(input())

    if(ch == 1):
        print("Addition of the two numbers : ", (n1 + n2))
        run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))
            

    elif(ch == 2):
        print("Subtraction of the two numbers : ", (n1 - n2))
        run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

    elif(ch == 3):
        print("Product of the two numbers : ", (n1 * n2))
        run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

    elif(ch == 4):
        print("Quotient of the two numbers : ", (n1//n2))
        run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

    elif(ch == 5):
        print("Remainder after division : ", (n1%n2))
        run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

    else:
        print("Invalid Choice!")
        run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


# Definitions of OR, AND, NOT, NOR, NAND, XOR, XNOR
def OR(A, B):
    return A | B

def AND(A, B):
    return A & B

def NOT(A):
    return ~A + 2

def NOR(A, B):
    return NOT(OR(A, B))

def NAND(A, B):
    return NOT(AND(A, B))

def XOR(A, B):
    return A ^ B

def XNOR(A, B):
    return NOT(XOR(A, B))

run = True
while(run):
    print("\nMenu\n1.OR Gate\n2.AND Gate\n3.NOT Gate\n4.NOR Gate\n5.NAND Gate\n6.XOR Gate\n7.XNOR Gate\nEnter your Choice : ")
    ch = int(input())

    if ch == 1:
        print("The Output of 0 OR 0 is : ", OR(0, 0))
        print("The Output of 0 OR 1 is : ", OR(0, 1))
        print("The Output of 1 OR 0 is : ", OR(1, 0))
        print("The Output of 1 OR 1 is : ", OR(1, 1))
    
    elif ch == 2:
        print("The Output of 0 AND 0 is : ", AND(0, 0))
        print("The Output of 0 AND 1 is : ", AND(0, 1))
        print("The Output of 1 AND 0 is : ", AND(1, 0))
        print("The Output of 1 AND 1 is : ", AND(1, 1))

    elif ch == 3:
        print("The Output of 0 NOT 0 is : ", NOT(0, 0))
        print("The Output of 0 NOT 1 is : ", NOT(0, 1))
        print("The Output of 1 NOT 0 is : ", NOT(1, 0))
        print("The Output of 1 NOT 1 is : ", NOT(1, 1))

    elif ch == 4:
        print("The Output of 0 NOR 0 is : ", NOR(0, 0))
        print("The Output of 0 NOR 1 is : ", NOR(0, 1))
        print("The Output of 1 NOR 0 is : ", NOR(1, 0))
        print("The Output of 1 NOR 1 is : ", NOR(1, 1))

    elif ch == 5:
        print("The Output of 0 NAND 0 is : ", NAND(0, 0))
        print("The Output of 0 NAND 1 is : ", NAND(0, 1))
        print("The Output of 1 NAND 0 is : ", NAND(1, 0))
        print("The Output of 1 NAND 1 is : ", NAND(1, 1))

    elif ch == 6:
        print("The Output of 0 XOR 0 is : ", XOR(0, 0))
        print("The Output of 0 XOR 1 is : ", XOR(0, 1))
        print("The Output of 1 XOR 0 is : ", XOR(1, 0))
        print("The Output of 1 XOR 1 is : ", XOR(1, 1))

    elif ch == 7:
        print("The Output of 0 XNOR 0 is : ", XNOR(0, 0))
        print("The Output of 0 XNOR 1 is : ", XNOR(0, 1))
        print("The Output of 1 XNOR 0 is : ", XNOR(1, 0))
        print("The Output of 1 XNOR 1 is : ", XNOR(1, 1))

    else:
        print("Invalid Choice!\n")
    run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))



# Leap Year Program using Basic Logic Gates (And (&) and OR (|))
run = True
while(run):
    year = int(input("Enter the Year : "))
    if(year >= 1 and year <= 3000):
        if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            print("The year", year, "is a Leap Year!")
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))
        else:
            print("The year", year, "is not a Leap Year!")
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))
    else:
        print("Invalid Year!")
        run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

# Checking whether number is even, odd, prime

# Defining Function to check for Prime Number
def prime(n):
    for i in range(2, n):
        if (n%i) == 0:
            return False
    return True

run = True
while(run):

    number = int(input("Enter Number to check for prime, even or odd : "))
    if prime(number):
        print("The Number {} is Prime".format(number))
    else:
        print("The Number {} is not Prime".format(number))

    if number % 2 == 1:
        print("The Number {} is Odd".format(number))
    else:
        print("The Number {} is Even".format(number))


    # Check whether the string is greater than 2 characters and if the first and last character is the same.
    str = input("Enter the string : ")
    if len(str) > 2:
        print("The length of the string is greater than 2")
    else:
        print("The length of the string entered is : ", len(str))
    
    if str[0] == str[-1]:
        print("The First and Last character of the strings are the same")
    else:
        print("The characters aren't same")
        
    run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


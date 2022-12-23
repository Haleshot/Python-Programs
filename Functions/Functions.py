# PP Experiment 3
# Srihari Thyagarajan, I066, Batch - B3

# Main Function
def __main__():
    run = True
    while(run):
        print("Menu\n\
1. Computing the 2nd Highest and Lowest Number in the List using bulit in sort function.\n\
2. Computing the 2nd Highest and Lowest Number in the List without function.\n\
3. Sorting Words in a list using built in sort function. \n\
4. Sorting Words in a list without function. \n\
5. Checking whether element entered by user is divisible by 5 or not and printing the\
element if it isn't divisible by 5. \n\
6. Checking whether a number entered can be made into a series of same\
digits by just changing one digit from the entered number \n\
7. Exit \n\
Enter Your Choice : ")

        ch = int(input())

        # Declaration of variables used in the program
        l_1 = []
        l_2 = []
        l_3 = []
        l_4 = []
        l_5 = []
        zc , oc = 0, 0

        if ch == 1:
            limit = int(input("Enter the Limit for the List : "))

            # Computing the 2nd Highest and Lowest Number in the List using bulit in sort function.
            for i in range(limit):
                ele = int(input("Enter the Element {} for the List : ".format(i)))
                l_1.append(ele)

            l_1.sort()
            print("The 2nd Highest Number in the list is = ", l_1[limit - 2])
            print("The 2nd Lowest Number in the list is = ", l_1[1])
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


        elif ch == 2:
            limit = int(input("Enter the Limit for the List : "))

            # Computing the 2nd Highest and Lowest Number in the List without using function.
            for i in range(limit):
                ele = int(input("Enter the Element {} for the List : ".format(i)))
                l_2.append(ele)
            
            for i in range(limit):

                for j in range(i + 1, limit):

                    if l_2[i] > l_2[j]:
                        t = l_2[i]
                        l_2[i] = l_2[j]
                        l_2[j] = t


            print("The 2nd Highest Number in the list is = ", l_2[limit - 2])
            print("The 2nd Lowest Number in the list is = ", l_2[1])
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


        elif ch == 3:
            limit = int(input("Enter the Limit for the List : "))

            # Sorting Words in a list using built in sort function.
            for i in range(limit):
                ele = input("Enter the Element {} for the List : ".format(i))
                l_3.append(ele)

            l_4 = l_3.copy() # Creating a duplicate of the l_3 list and storing it in l_4

            l_3.sort()
            print("The List Sorted in Alphabetical Order is :\n", l_3)
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 4:
            limit = int(input("Enter the Limit for the List : "))

            for i in range(limit):
                ele = input("Enter the Element {} for the List : ".format(i))
                l_4.append(ele)

            # Sorting Words in a list without using functions.
            for i in range(limit):
                for j in range(i + 1, limit):
                    if l_4[i] > l_4[j]:
                        t = l_4[i]
                        l_4[i] = l_4[j]
                        l_4[j] = t

            print("The List Sorted in Alphabetical Order is :\n", l_4)
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 5:  
            limit = int(input("Enter the Limit for the List : ")) 
                   
            # Checking whether element entered by user is divisible by 5 or not and printing the element if it isn't divisible by 5.
            for i in range(limit):
                ele = int(input("Enter the Element {} for the List : ".format(i)))

                if ele % 5 != 0: # Checking whether the element entered by the user is divisible by 5 or not
                    l_5.append(ele) # Appending the element to the list after checking for the above condition.
            print(l_5)
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 6:
            # Checking whether a number entered can be made into a series of same digits by just changing one digit from the entered number
            print("Enter the Number to be checked : ")
            l_6 = input()

            for i in (l_6):
                if i == "0":
                    zc += 1
                elif i == "1":
                    oc += 1

            if zc == 1:
                print("YES")
            if oc == 1:
                print("YES")
            else:
                print("NO")
            
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 7:
            print("Thank You!")
            exit(0)

# Calling the Main Function
__main__()
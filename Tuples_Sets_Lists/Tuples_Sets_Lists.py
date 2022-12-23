# PP Experiment 3
# Srihari Thyagarajan, I066, Batch - B3

# Main Function
def __main__():
    run = True
    while(run):
        print("Menu\n\
1. Finding the length of each word in the Tuple entered.\n\
2. Replacing a Tuple's last element in a list.\n\
3. Unpacking the Tuple. \n\
4. Creating a Set and printing it. \n\
5. Add and Remove Item from a set \n\
6. Union and Intersecion of Sets \n\
7. Exit \n\
Enter Your Choice : ")

        ch = int(input())

        # Declaration of variables used in the program
        t_1 = ()
        t_1_array = []

        if ch == 1:
            limit = int(input("Enter the Limit for the Tuple : "))

            for i in range(limit):
                ele = input("Enter the Element {} for the Tuple : ".format(i))
                t_1_array.append(ele)
            t_1 = tuple(t_1_array)

            a = 1
            print("The Original Tuple is = ", t_1)
            for i in t_1:
                print("The Length of the {} word is".format(a), " = ", len(i))
                a += 1
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


        elif ch == 2:
            limit = int(input("Enter the Limit for the Tuple : "))

            for i in range(limit):
                ele = input("Enter the Element {} for the Tuple : ".format(i))
                t_1_array.append(ele)
            t_1 = tuple(t_1_array)

            print("The Original Tuple is = ", t_1)
            choice = input("Enter the Value to replace the Tuple's last Element : ")
            print("The Tuple after replacing the last value = ", t_1)
            
            t_1_array[limit - 1] = choice
            t_1 = tuple(t_1_array)

            print("The Tuple after replacing the last value = ", t_1)
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


        elif ch == 3:
            t_1 = ("Array", "List", "Tuple", "Linked List", "Dictionary")
            a, b, c, d, e = t_1

            print("The Tuple after unpacking is : ")
            print(a, b, c, d, e)
            print()

            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


            
            

        elif ch == 4:
            limit = int(input("Enter the Limit for the Set : "))
            set_1 = set()
            for i in range(limit):
                ele = input("Enter the Element {} for the Set : ".format(i))
                set_1.add(ele)

            for i in set_1:
                print(i)

            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 5:  
            limit = int(input("Enter the Limit for the Set : "))
            set_1 = set()
            for i in range(limit):
                ele = input("Enter the Element {} for the Set : ".format(i))
                set_1.add(ele)


            print("The Original Set is = ", set_1)
            choice_1 = input("Enter the Value to be added to the Set : ")
            set_1.add(choice_1)
            print("The Set after adding value is = ", set_1)

            choice_2 = input("Enter the Value to be Removed from the Set : ")
            set_1.remove(choice_2)
            print("The Set after removing the value is = ", set_1)

            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 6:
            limit_1 = int(input("Enter the Limit for the Set 1 : "))
            limit_2 = int(input("Enter the Limit for the Set 2 : "))
            set_1 = set()
            set_2 = set()

            for i in range(limit_1):
                ele = input("Enter the Element {} for the Set 1 : ".format(i))
                set_1.add(ele)

            for i in range(limit_1):
                ele = input("Enter the Element {} for the Set 2 : ".format(i))
                set_2.add(ele)

            print("The Union of the Sets is = ", set_1 | set_2)
            print("The Intersection of the Sets is = ", set_1 & set_2)


            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 7:
            print("Thank You!")
            exit(0)

# Calling the Main Function
__main__()

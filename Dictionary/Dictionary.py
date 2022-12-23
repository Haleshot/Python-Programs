# PP Experiment 5
# Srihari Thyagarajan, I066, Batch - B3

# Main Function


def main():
    run = True
    while(run):
        print("Menu\n\
1. Create a dictionary.\n\
2. Print keys and values of the dictionary created.\n\
3. Printing the Frequency of Elements in a list and displaying them in a dictionary. \n\
4. Mapping two lists into a dictionary. \n\
5. Exit \n\
Enter Your Choice : ")

        ch = int(input())

        # Declaration of variables used in the program
        dict_1 = dict()

        if ch == 1:
            dict_1 = {"Car_Company": "Toyota", "Type": "Camry", "Origin": 2013}
            print("Dictionary Created...")

            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


        elif ch == 2:
            
            dict_1 = {"Car_Company": "Toyota", "Type": "Camry", "Origin": 2013}
            print("The Values of Keys of the Dictionary are :\n", dict_1.keys())
            print("The Values of the Dictionary are :\n", dict_1.values())


            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 3:
            l_1 = ["Toyota", "Type", "Camry", "Origin", "Camry", "Origin"]
            print("The Original list is : ", l_1)
            dict_2 = dict()


            for word in l_1:
                if word in dict_2:
                    dict_2[word] += 1
                else:
                    dict_2[word] = 1

            print(dict_2)
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 4:
            dict_3 = dict()
            l_2 = ["Company", "Model", "Name"]
            l_3 = ["Mahindra", "SUV", "Alturas G4"]

            print("The Lists are : ", l_2, l_3)
            dict_3 = dict(zip(l_2, l_3))

            print("The Dictionary is : ", dict_3)
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 5:
            print("Thank You!")
            exit(0)

        else:
            print("Invalid Choice!")
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


main()
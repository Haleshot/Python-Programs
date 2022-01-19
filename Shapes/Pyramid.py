def Pyramid(n):
    l = n - 1
    for i in range(0, n):
        for j in range(0, l):
            print(end = " ")

        l -= 1
        for q in range(0, i+1):
            print("* ", end = "")
        print("\n")
            

n = int(input("Enter the Limit \n"))
Pyramid(n)

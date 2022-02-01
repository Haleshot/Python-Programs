#Program that prints Number Shape as per input limit.
def Numbers(n):
    n1 = 1
    for i in range(0, n):
        for j in range(0, i + 1):
            print(n1, end = ' ')
            n1 += 1
        print("\n")
            

n = int(input("Enter the Limit \n"))
Numbers(n)

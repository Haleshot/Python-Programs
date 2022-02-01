#Program that prints Alphabetical Shape as per input limit.
def Numbers(n):
    for i in range(0, n):
        n1 = 65
        for j in range(0, i + 1):
            print(chr(n1), end = ' ')
            n1 += 1
        print("\n")
            

n = int(input("Enter the Limit \n"))
Numbers(n)

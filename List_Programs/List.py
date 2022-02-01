#Program that prints list elements using function.
def List(n):
    l = []
    for i in range(0, n):
        a = int(input("Enter the Element : "))
        l.append(a)
    print(l)

n = int(input("Enter the Limit \n"))
List(n)

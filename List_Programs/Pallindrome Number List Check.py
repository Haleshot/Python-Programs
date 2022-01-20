# Program to check for Pallindrome Number
def Pallindrome(n):
    l = []
    for i in range(0, n):
        a = int(input("Enter the Element : "))
        l.append(a)
    print("The Original List is :" ,l)

    for i in range(len(l)):
        temp = l[i]
        temp1 = l[i]
        temp2 = l[i]
        c = 0
        rev = 0
        
        while(temp1 > 0):
            last = temp1 % 10
            rev = rev*10 + last
            temp1//=10

        if (rev == temp2):
            print(rev, "Pallindrome")
        else:
            print(rev, "Not Pallindrome")
            

n = int(input("Enter the Limit \n"))
Pallindrome(n)

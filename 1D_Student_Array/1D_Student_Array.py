# Program that compares students marks with average marks of class using 1D Array
# Creates separate 2 lists for Students (less and greater than average marks of class)
l1 = l2 = l3 = []
sum = avg = c1 = c2 = 0

n = int(input("Enter the limit for Number of Students in class : "))
for i in range(n):
    a = int(input("Enter the Marks for Student {} ".format(i)))
    sum += a
    l1.append(a)

# Calculating the average of the class
avg = sum/n

for i in range(n):
    if l1[i] < avg:
        c1 += 1
        l2.append(l1[i])

    elif l1[i] > avg:
        c2 += 1
        l3.append(l1[i])

print("\nThe Marks of Students less than average marks of the class is given below: \n")
for i in range(c1):
    print(l2[i])

print("\nThe Marks of Students greater than average marks respectively is given below: \n")
for i in range(c2):
    print(l3[i])




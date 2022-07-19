# Program that adds two 2D matrices.
# 2D Matrices Addition

sum = 0
row = int(input("Enter the Row limit for the Matrices : "))
column = int(input("Enter the Column limit for the Matrices : "))
array_1 = []
array_2 = []
array_3 = []

# Matrix 1 Formation
for i in range(row):
    col = []
    for j in range(column):
        ele = int(input("Enter the Element {}{} for the Matrix 1 : ".format(i, j)))
        col.append(ele)
    array_1.append(col)

# Matrix 2 Formation
for i in range(row):
    col = []
    for j in range(column):
        ele = int(input("Enter the Element {}{} for the Matrix 2 : ".format(i, j)))
        col.append(ele)
    array_2.append(col)

# Sum of Matrices formation Formation
for i in range(row):
    col = []
    for j in range(column):
        sum = array_1[i][j] + array_2[i][j]
        col.append(sum)
    array_3.append(col)

print("\n")

print("The Matrix A is : \n")
for i in array_1:
    print(i)

print("\n")

print("The Matrix B is : \n")
for i in array_2:
    print(i)

# Sum of Matrices
print("\n")
print("The Sum of Matrices is : \n")
for i in array_3:
    print(i)

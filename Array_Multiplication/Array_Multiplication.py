# Program that multiplies Matrices (NxN order/ Square matrices).
# Multiplicaiton of Matrices

from math import prod


row = int(input("Enter the Row limit for the Matrices : "))
column = int(input("Enter the Column limit for the Matrices : "))
array_1 = []
array_2 = []
result = []

# Matrix 1 Formation
for i in range(row):
    col = []
    for j in range(column):
        ele = int(input("Enter the Element for the Matrix 1 : "))
        col.append(ele)
    array_1.append(col)

# Matrix 2 Formation
for i in range(row):
    col = []
    for j in range(column):
        ele = int(input("Enter the Element {}{} for the Matrix 2 : ".format(i, j)))
        col.append(ele)
    array_2.append(col)

# Result Matrix Formation
for i in range(row):
    col = []
    for j in range(column):
        ele = 0
        col.append(ele)
    result.append(col)


# Multiplication of Matrices formation Formation
while(row == column):
    for i in range(row):
        for j in range(column):
            for k in range(row):
                result[i][j] += array_1[i][k] * array_2[k][j]

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
print("The Product of Matrices is : \n")
for i in result:
    print(i)

# Program that creates Array Transpose of 2D array as entered by user.
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


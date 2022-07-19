# Program that adds two 2D matrices.
# 2D Matrices Addition

sum = 0
row = int(input("Enter the Row limit for the Matrices : "))
column = int(input("Enter the Column limit for the Matrices : "))
array_1 = []
array_2 = []
array_3 = []

for i in range(row):
    col = []
    for j in range(column):
        ele = int(input("Enter the Element {} for the Matrix 1 : ".format(i)))
        col.append(ele)
    array_1.append(col)

for i in range(row):
    col = []
    for j in range(column):
        ele = int(input("Enter the Element {} for the Matrix 2 : ".format(i)))
        col.append(ele)
    array_2.append(col)

for i in range(row):
    for j in range(column):
        sum += array_1[i][j] + array_2[i][j]
        array_3.append(sum)

for i in array_3:
    print(i)
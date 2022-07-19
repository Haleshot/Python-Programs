# Program that adds two 2D matrices.
# 2D Matrices Addition

row = int(input("Enter the Row limit for the Matrix : "))
column = int(input("Enter the Column limit for the Matrix : "))
array = []

for i in range(row):
    col = []
    for j in range(column):
        ele = int(input("Enter the Element {} for the Matrix : ".format(i)))
        col.append(ele)
    array.append(col)

for i in array:
    print(i)
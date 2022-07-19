# Program that multiplies Matrices.
# Multiplicaiton of Matrices

row = int(input("Enter the Row limit for the Matrices : "))
column = int(input("Enter the Column limit for the Matrices : "))
array = []

for i in range(row):
    col = []
    for j in range(column):
        ele = int(input("Enter the Element for the Matrix 1 : "))
        col.append(ele)
    array.append(col)


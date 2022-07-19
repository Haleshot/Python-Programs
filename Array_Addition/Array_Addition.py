# Program that adds two 2D matrices.
# 2D Matrices Addition

from calendar import c
from numpy import array


row = int(input("Enter the Row limit for the 2D Matrix : "))
column = int(input("Enter the Column limit for the 2D Matrix : "))
array_2d = []

for i in range(row):
    col = []
    for j in range(column):
        ele = int(input("Enter the Element {} for the 2D Matrix : ".format(i)))
        col.append(ele)
    array_2d.append(col)

for i in range(row):
    for j in range(column):
        print(array_2d[i][j], ", ")
    print("\n")
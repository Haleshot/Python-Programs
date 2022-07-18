# Program to check whether a room is clean or not
# User will enter 1 if the room is clean, 0 if the room is dirty

import random
import numpy as np
a, b = input("Enter the rows and columns for Rooms A and B : ").split()
a = int(a)
b = int(b)
c = 0
mat = []

for i in range(a):
    row = []
    for j in range(b):
        row.append(input())
    mat.append(row)

mat = np.array(mat)
print(mat)

for i in range(a):
    for j in range(b):
        if mat[i][j] == '1':
            print("The Room {}{} is clean, no cleaning required. Moving to the next room.".format(i, j))
        else:
            mat[i][j] = '0'
            print("The Room {}{} is dirty, the cleaning process starts now...".format(i, j))

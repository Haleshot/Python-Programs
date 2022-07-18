# Program to check whether a room is clean or not

# User will enter 1 if the room is clean, 0 if the room is dirty

import random
import numpy as np
a, b = input("Enter the rows and columns for Rooms A and B: ").split(' ')
a = int(a)
b = int(b)
c = 0
mat = [a][b]


for i in range(a):
    for j in range(b):
        ele = input("Enter the Cleanliness Status for the room\n")
        mat[i][j].append(ele)
for i in range(a):
    for j in range(b):
        if mat[i][j] == "0":
            print("The Room is dirty, the cleaning process starts now...")
            print("Price will be updated at the end")
            c += 1
        
        else:
            print("The Room is clean, no cleaning required. Moving to the next room.")

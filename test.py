# Program to check whether a room is clean or not

# User will enter 1 if the room is clean, 0 if the room is dirty

import random
import numpy as np
a, b = input("Enter the rows and columns for Rooms A and B").split()
a = int(a)
b = int(b)

mat = np.array


for i in a:
    for j in b:
        mat[i][j] = input("Enter the cleanliness status for the room")
        
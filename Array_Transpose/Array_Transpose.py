# Program that creates Array Transpose of arrays as entered by user.
row = int(input("Enter the Row limit for the Matrices : "))
column = int(input("Enter the Column limit for the Matrices : "))
array_1 = []
result = []

# Matrix 1 Formation
for i in range(row):
    col = []
    for j in range(column):
        ele = int(input("Enter the Element for the Matrix 1 : "))
        col.append(ele)
    array_1.append(col)

# Showing the Matrix entered by the user
print("\n")
print("The Matrix is : \n")
for i in array_1:
    print(i)


# Result Matrix Formation
for i in range(row):
    col = []
    for j in range(column):
        ele = 0
        col.append(ele)
    result.append(col)
    

# Checking whether the Matrix is a Square Matrix or not.
while row == column:
    for i in range(row):
        for j in range(column):
            result[column][row] = array_1[row][column]

# Transpose of a Matrix
print("\n")
print("The Transpose of te Matrix is : \n")
for i in result:
    print(i)

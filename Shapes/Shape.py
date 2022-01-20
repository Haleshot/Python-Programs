#Program that prints Shape
k = 6
temp = 2*k - 2
for i in range(k):
    
    for j in range(0, temp):
        print(end = ' ')
        
    temp -= 2

    for l in range(0, i + 1):
         print("* ", end = '')

    
    print("\n")


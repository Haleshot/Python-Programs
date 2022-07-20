# Program which helps in finding an element in a sorted array, Binary Search Technique, Complexity = O(log(n))


from binascii import a2b_hex


def Binary_Search(array_fun, value):
        array_fun = sorted(array_fun)
        low = 0
        high = len(array_fun) - 1

        while low <= high:
            mid = (low + high)//2
            if array_fun[mid] < value:
                low = mid + 1
            
            elif array_fun[mid] > value:
                high = mid - 1
            
            elif array_fun[mid] == value:
                return mid
        return -1
    

def main():
    a = []
    while True:
        print("\nThe Menu is : ")
        print("1. Insert a value in the array\n2. Display the array\n3. Search for an Element in the array\n4.Exit\n")
        ch = int(input("Enter the choice : "))

        if ch == 1:
            value = int(input("Enter the value to be entered into the array : "))
            a.append(value)
        
        elif ch == 2:
            a = sorted(a)
            for i in a:
                print(i)
        
        elif ch == 3:
            value = int(input("Enter the value to be searched from the array : "))
            result = Binary_Search(a, value)

            if result != -1:
                a = sorted(a)
                print("Element present at index :", str(result), "in the array")
            
            else:
                print("Element not found in array")

        elif ch == 4:
            exit(0)
        
        else:
            print("Invalid Choice!")

main()
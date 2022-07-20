# Program which helps in finding an element in a sorted array, Binary Search Technique, Complexity = O(log(n))
array = []
limit = int(input("Enter the limit for the array : "))
print("Please enter Array elements in ascending order")
for i in range(limit):
    ele = int(input("Enter Element {} for the array : ".format(i)))
    array.append(ele)


def Binary_Search(array_fun, value):
    is_sorted = True
    if array_fun == sorted(array_fun):
        low = 0
        high = len(array_fun) - 1
        mid = (low + high)//2

        while low <= high:
            if array_fun[mid] < value:
                low = mid + 1
            
            elif array_fun[mid] > value:
                high = mid - 1
            
            elif array_fun[mid] == value:
                return mid
        return -1
    
    else:
        array_fun = sorted(array_fun)
        Binary_Search(array_fun, value)

def main():
    while True:
        print("\nThe Menu is : ")
        print("1. Insert a value in the BST\n2. Display the BST\n3. Exit\n")
        ch = int(input("Enter the choice : "))
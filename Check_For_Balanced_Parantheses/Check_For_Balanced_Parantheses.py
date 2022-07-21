# Function to check for Balanced Parantheses

# Declaring the Stack
stack = []


# Check Matching Characters Function
def check_match(x, y):

    if x == '(' and y == ')':
        return 1
    elif x == '{' and y == '}':
        return 1
    elif x == '[' and y == ']':
        return 1
    return 0

# Function to check for Balanced Parantheses
def Check_Parantheses(exp):
    for i in exp:
        if i == '(' or i == '{' or i == '[' :
            stack.append(i)
        elif i == ')' or i == '}' or i == ']' :
            top = stack[-1]
            if len(stack) == 0 or check_match(top, i) == 0:
                return 0
            else:
                stack.pop()

    if len(stack) == 0:
        return 1



# Main Function
def main():
    is_true = True
    while is_true:
        expression = input("Enter the Expression : ")

        # Assigning each operator to the Stack
        for i in expression:
            stack.append(i)

        print(expression)
        
        if Check_Parantheses(expression) == 1:
            print("The Brackets are Balanced!")

        elif Check_Parantheses(expression) == 0:
            print("The Brackets are not Balanced!")

        is_true = int(input("\nWant to continue? (Yes = Input 1/ False = Input 0) : "))

main()
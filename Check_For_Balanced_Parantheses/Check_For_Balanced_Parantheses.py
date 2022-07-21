# Program to check for Balanced Parantheses

# Function to check for Balanced Parantheses
def Check_Parantheses(exp):
    # Declaring the Stack
    stack = []

    for i in exp:

        # Assigning/ Appending/ Adding the Opening braces to the Stack
        if i == '(' or i == '{' or i == '[' :
            stack.append(i)
        elif i == ')' or i == '}' or i == ']' :
            if not stack :
                return False
            top = stack.pop()
            if top == '(' :
                 if i != ')':
                    return False

            if top == '{':
                if i != '}':
                    return False

            if top == '[':
                if i != ']':
                    return False

    if not stack:
        return True



# Main Function
def main():
    is_true = True
    while is_true:
        expression = input("Enter the Expression : ")

        print(expression)
        
        if Check_Parantheses(expression):
            print("The Brackets are Balanced!")

        else:
            print("The Brackets are not Balanced!")

        is_true = int(input("\nWant to continue? (Yes = Input 1/ False = Input 0) : "))

main()
# Dabbling with Strings
# PP Experiment 2
# Srihari Thyagarajan, I066, Batch - B3


# Variable to store Hello World
st = "Hello World"
print(st)
# Printing each character of Hello World! seperately
for i in st:
    print(i)

first_char = st[0]  # Storing the first character of the string
last_char = st[-1]  # Storing the last character of the string
new_str = last_char + st[1 : -1] + first_char # Adding the string accordingly
print(new_str)

print("The Reversed String is : ", st[::-1])

number = int(input("Enter the Number : "))
number_1 = number
print("Number before conversion : ", number)

# Converting number to string and storing it in a variable
str_number = str(number)
first_digit = str_number[0]
last_digit = str_number[-1]
str_number = last_digit + str_number[1 : -1] + first_digit
number = int(str_number)
print("Number after Conversion : ", number)

rev = 0
while number_1 != 0:
    last = number_1 % 10
    rev = rev * 10 + last
    number_1//=10

print("The Reversed Number is : ", str(rev))
# Simple calculator in Python

choice = 0

# Loop until the user enters a valid choice
while choice not in range(1, 5):
    # Display the menu of options
    print("Select operation.\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")

    # Take input from the user
    choice = int(input("Enter choice(1/2/3/4): "))

    # Check if the user's choice is valid
    if choice not in range(1, 5):
        print("Invalid input. Please try again.\n")

# Take input for the numbers to perform the operation on
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

# Perform calculation based on user input
if choice == 1:
    print(x, "+", y, "=", x + y)

elif choice == 2:
    print(x, "-", y, "=", x - y)

elif choice == 3:
    print(x, "*", y, "=", x * y)

elif choice == 4:
    print(x, "/", y, "=", x / y)
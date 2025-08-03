# Welcome message
print("Welcome to Calculation Made Simple")

while True:
    try:
        # Ask the user for the first number
        num1 = float(input("Enter the first number: "))

        # Ask the user for the second number
        num2 = float(input("Enter the second number: "))

        # Ask the user for the operation
        operation = input("Choose an operation (+, -, *, /): ")

        # Check the operation and do the math
        if operation == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result:.2f}")

        elif operation == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result:.2f}")

        elif operation == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result:.2f}")

        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result:.2f}")
            else:
                print("Cannot divide by zero!")
                continue  # Restart the loop

        else:
            print("Invalid operation! Please choose +, -, * or /")
            continue  # Restart the loop

        print()  # Add a blank line for readability

        # Ask if the user wants to continue
        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print("Thank you for using our calculator.")
            break

    except ValueError:
        print("Invalid number entered! Please enter numbers only.\n")

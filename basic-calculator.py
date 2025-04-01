def calculator():
    """Performs basic arithmetic operations based on user input."""

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        result = None

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
        else:
            print("Invalid operation. Please use +, -, *, or /.")

        if (result != None):
            print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    calculator()
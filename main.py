from calculator import add, subtract, multiply, divide

def main():
    print("Welcome to the Python Calculator!")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("Enter calculation: ")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        try:
            num1, op, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)

            if op == "+":
                result = add(num1, num2)
            elif op == "-":
                result = subtract(num1, num2)
            elif op == "*":
                result = multiply(num1, num2)
            elif op == "/":
                result = divide(num1, num2)
            else:
                print("Unsupported operator")
                continue

            print("Result:", result)

        except Exception:
            print("Invalid input")

if __name__ == "__main__":
    main()

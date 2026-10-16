def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot perform modulus by zero.")
    return a % b
def exponent(a, b):
    return a ** b
def floor_division(a, b):
    if b == 0:
        raise ValueError("Cannot perform floor division by zero.")
    return a // b


def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, %, **, //")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /, %, **, //): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                result = add(num1, num2)
            elif op == "-":
                result = subtract(num1, num2)
            elif op == "*":
                result = multiply(num1, num2)
            elif op == "/":
                result = divide(num1, num2)
            elif op == "%":
                result = modulus(num1, num2)
            elif op == "**":
                result = exponent(num1, num2)
            elif op == "//":
                result = floor_division(num1, num2)
            else:
                print("Invalid operator.")
                continue

            print(f"Result: {result}")

        except ValueError as e:
            print(f"Invalid input: {e}")

        again = input("Do you want to calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    calculator()
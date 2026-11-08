"""A beginner-friendly calculator for local Python practice."""


def calculate(a, b, operation):
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    if operation == "%":
          return (a * b) / 100
    raise ValueError("Unknown operation")


def main():
    print("Python Calculator Practice")
    try:
        first = float(input("First number: "))
        operation = input("Operation (+, -, *, /, %): ").strip()
        second = float(input("Second number: "))
        print("Result:", calculate(first, second, operation))
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()

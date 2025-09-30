def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b  # Division by zero will be handled elsewhere


def main():
    print("Welcome to the calculator... I guess.")
    print("Let's just get this over with.")

    try:
        num1 = float(input("First number. Whatever: "))
        num2 = float(input("Second number. Can't wait: "))
    except ValueError:
        print("Brilliant. You had one job: type a number.")
        return

    print("Pick your operation, not that it matters:")
    print(" +  for addition")
    print(" -  for subtraction")
    print(" *  for multiplication")
    print(" /  for division")

    operation = input("So, what's it gonna be? (+, -, *, /): ").strip()

    if operation == "+":
        result = add(num1, num2)
        print(f"Yay. The result is {result}. Happy now?")
    elif operation == "-":
        result = subtract(num1, num2)
        print(f"There. Subtracted. It's {result}. Try to contain your excitement.")
    elif operation == "*":
        result = multiply(num1, num2)
        print(f"Multiplied. Shocking. It's {result}.")
    elif operation == "/":
        if num2 == 0:
            print("Wow. Divide by zero? What a genius move.")
        else:
            result = divide(num1, num2)
            print(f"Yep. It's {result}. Whatever.")
    else:
        print("I can't even. That wasn't an option.")

    print("Can I go now?")

if __name__ == "__main__":
    main()

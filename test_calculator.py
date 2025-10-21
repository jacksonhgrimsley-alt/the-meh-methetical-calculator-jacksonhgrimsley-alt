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
        if num2 == 0 == 0.0:
            print("Wow. Divide by zero? What a genius move.")
        else:
            result = divide(num1, num2)
            print(f"Yep. It's {result}. Whatever.")
    else:
        print("I can't even. That wasn't an option.")

    print("Can I go now?")

if __name__ == "__main__":
    main()
  
import pytest
from calculator import add, subtract, multiply, divide

def test_add_posative_numbers():
    """Test that adding two positive numbers works correctly."""
    assert add(5, 3) == 8

def test_add_negative_numbers():
    """Test that adding two negative numbers works correctly."""
    assert add(-5+-8) == -8

def test_subtract_posative_numbers():
    """Test that subracting two posative numbers works correctly."""
    assert subtract(8-4) == 4

def test_subtract_big_small_numbers():
    """Test that subtracting one small number and a bigger number works correctly."""
    assert subtract(4-8) == -4

def test_multiply_posative_numbers():
    """test multipling two numbers"""
    assert multiply(9*9) == 81

def test_multiply_zero():
    """"test multpling a number with zero"""
    assert multiply(9*0) == 0

def test_divide_posative_numbers():
    """test dividing two positive numbers"""
    assert divide(12/3) == 4

def test_divide_two_numbers_with_one():
    """test dividing a number with one"""
    assert divide(12/1) == 12

def test_divide_zero():
    """test dividing a number with zero"""
    assert divide(12/0) == "?"

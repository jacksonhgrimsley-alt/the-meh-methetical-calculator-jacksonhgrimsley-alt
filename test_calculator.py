
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

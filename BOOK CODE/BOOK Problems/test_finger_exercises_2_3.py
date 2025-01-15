import pytest

from finger_exercises_2_3 import largest_odd_num


def test_largest_odd_num_case1():
    # Test case 1: Normal case with odd numbers
    assert largest_odd_num(5, 7, 9) == 9, "Failed: Largest odd number in (5, 7, 9) should be 9."

def test_largest_odd_num_case1_reversed():
    # Test case 1: Normal case with odd numbers in descending order
    assert largest_odd_num(9, 7, 5) == 9, "Failed: Largest odd number in (5, 7, 9) should be 9."

def test_largest_odd_num_case2():
    # Test case 2: Mixed odd and even numbers
    assert largest_odd_num(10, 11, 24) == 11, "Failed: Largest odd number in (10, 11, 24) should be 11."

def test_largest_odd_num_case2_reversed():
    # Test case 2: Mixed odd and even numbers in descending order
    assert largest_odd_num(51, 11, 4) == 51, "Failed: Largest odd number in (10, 11, 24) should be 11."

def test_largest_odd_num_case3():
    # Test case 3: No odd numbers in descending order
    assert largest_odd_num(6, 8, 10) == 6, "Failed: Largest odd number in (6, 8, 10) should be 6."

def test_largest_odd_num_case3_reversed():
    # Test case 3: No odd numbers in descending order
    assert largest_odd_num(10, 8, 6) == 6, "Failed: Largest odd number in (6, 8, 10) should be 6."

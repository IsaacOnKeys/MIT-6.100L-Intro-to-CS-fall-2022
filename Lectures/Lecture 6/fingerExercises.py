"""Finger Exercise Lecture 6
Assume you are given an integer 0 <= N <= 1000. Write a piece of Python code that uses bisection search to guess N. The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N. Hints: If the halfway value is exactly in between two integers, choose the smaller one."""

from math import floor


def bisection(num):
    if num < 0 or num > 1000:
        return f"{num} is out of bounds."

    low = 0
    high = 1000
    guess = (low + high) / 2
    count = 0
    while guess != num:
        count += 1
        if num > guess:
            low = guess
            guess = floor((low + high) / 2)
        else:
            high = guess
            guess = floor((low + high) / 2)

    return f"it took {count} guess(es) to find the number {num}"


result = bisection(50)
print(result)

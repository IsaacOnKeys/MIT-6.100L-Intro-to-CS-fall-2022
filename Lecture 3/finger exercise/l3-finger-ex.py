"""Finger Exercise Lecture 3
Assume you are given a positive integer variable named N. Write a piece of Python code that prints hello world on separate lines, N times. You can use either a while loop or a for loop.
"""

N = int(input(f"please input a positice integer:\n"))
counter = 0
for i in range(N):
    counter += 1
    print("Hello World", counter)

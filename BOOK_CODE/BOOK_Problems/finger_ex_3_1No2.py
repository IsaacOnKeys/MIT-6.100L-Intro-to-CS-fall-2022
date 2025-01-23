"""
Finger exercise: Write a program that asks the user to enter an
integer and prints two integers, root and pwr, such that 1 < pwr < 6
and root**pwr is equal to the integer entered by the user. If no such
pair of integers exists, it should print a message to that effect.
"""

num = int(input(f"Please enter an integer: \n"))
root = 0
pwr = 0
guess = num/2
for y in range(int(num/2), 0, -1):
    for x in range(2,6):
        if  y**x == num:
            root = y
            pwr = x
            print(f"Root = {y}, and pwr = {x}")
            break
if root == 0 or pwr == 0:
    print("No integers, between 1 and 6 are a power that can be combined with any base to equal your number.")

"""Finger exercise: Write a program that asks the user to input 10
integers, and then prints the largest odd number that was entered. If
no odd number was entered, it should print a message to that effect."""
counter = 0
largest = 0
while counter <  10:
    num = int(input(f'Please enter 1 integer below: \n'))
    if num %2 != 0 and num > largest:
        largest = num
    counter += 1
if largest == 0:
    print("There are no odd numbers here.")
else: 
    print(f"The largest odd number you entered was: {largest}")

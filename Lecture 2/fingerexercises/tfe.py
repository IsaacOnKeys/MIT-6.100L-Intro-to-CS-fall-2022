"""Finger exercise: Write a program that asks the user to input 10
integers, and then prints the largest odd number that was entered. If
no odd number was entered, it should print a message to that effect."""
count = 0
is_odd = False
curr = float('-inf')

while True:
	i = input("input an integer: ")
	i = int(i)
	if (i % 2 != 0):
		is_odd = True
		if i > curr:
			curr = i
	
	count += 1
	if count == 10:
		if is_odd:
			print(f"{curr}")
			break
		else:
			print("no odd number was entered")
			break




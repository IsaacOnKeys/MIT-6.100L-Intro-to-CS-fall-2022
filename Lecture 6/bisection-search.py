"""
Use a Bisection Search to find the Sqare Root of x. 
This is an example of logarithmic time: Logarithmic growth is when search area is cut in half with each iteration

Process:
- The answer is between 0 & x
- pick a number in the middle of this range
"""
import timeit


def square_root(x):	
	epsilon = 0.01  # this is the range of precision, in case the number has a veeeeerry long or infinite decimal
	num_guesses = 0  # tally of the num of guesses
	low = 0
	high = x
	guess = (high + low) / 2.0  # 9 5

	while abs(guess**2 - x) > epsilon:  # The guess is not yet closer than epsilon
		# print(
		# 	f"guess number:{num_guesses}\n current guess:{guess}\n {abs(guess**2 - x)} is greater than epsilon: {abs(guess**2 - x) > epsilon}"
		# )
		if guess**2 < x:
			low = guess
		else:
			high = guess
		guess = (high + low) / 2.0
		num_guesses += 1

	# print("num_guesses =", num_guesses)
	if guess**2 == x:
		print(f"The Square root of {x} is {guess}")
	else:
		print(guess, "is approximately the square root of", x)
		print(f"Guess^2 == {guess**2}")

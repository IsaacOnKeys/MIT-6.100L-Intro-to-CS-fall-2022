"""
Use the Newton-Raphson algorithm to find the approximation of the Sqare Root of x. 
	- only works to find roots for a polynomial

Newton-Raphson Algorithm:
If you have a polynomial of this form:
p(x) = a_n-1x^n-1 + ... + a_1x+a_0
You can use g as an approximation to the root then:
	g-p(g)/p'(g)
is a better approximation; where p' is a derivative of p.
Process:
start with a guess (g)
"""

epsilon = 0.01  # egree of accuracy
k = 24.0  # number we are fining the sqare root of.
guess = k / 2.0  # Initial resonable guess, although it can be anything.
num_guesses = 0  # purely for science

while abs(guess * guess - k) >= epsilon: #same while-loop condition as in bisection search
	num_guesses += 1
	print(f"{guess}")
	guess = guess - (((guess * guess) - k) / (2 * guess)) 
print(f"num_guesses = {num_guesses}")
print(f"Square root of {k} is about {guess}")

#if guess = 12, and k = 24
# guess = 12 - ((12 * 12) - 24) / (2 * 12)

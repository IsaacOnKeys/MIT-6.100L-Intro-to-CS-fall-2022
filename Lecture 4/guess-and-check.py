""" process is called exhaustive enumeration
Applies to a problem where...
	- You are able to guess a value for solution
	- You are able to check if the solution is correct
You can keep guessing until
	- You find a solution, or
	- have guessed all values

Square RootProblem
------------------
	Basic idea:
		- Given an int x, we want to see if it has another int which is it's square root.
		- Start with a guess and check if it is the right answer4
	If the x is not a perfect square:
		-we need to implement an exhaustive set of solutions to avoid an infinite loop.
		- Use algebra: if guess^2 is bigger than x, the you have exhausted all values and can stop.
"""


def squareRoot() -> int:
    x = int(input("Enter an Integer"))
    guess = 0
    prev = 0

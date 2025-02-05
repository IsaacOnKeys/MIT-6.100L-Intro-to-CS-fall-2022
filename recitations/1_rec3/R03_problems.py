# Problem 1 - Bisection Search Practise
# Write a program using bisection search to find the forth root of a number inputted by the
# user. Print the forth root calculated with max error of 0.01.

"""x = float(input("Using bisection search calculate the forth root of: "))
epsilon = 0.01
low = 0.0
high = max(x, 1)
ans = (high + low) / 2.0
epsilon = 0.01
count = 0

while abs(ans**4 - x) >= epsilon:
    count += 1
    print(f"{count}: guess = {ans}")

    if ans**4 > x:
        print(ans, "is too high")
        high = ans
        ans = (high + low) / 2
        
    elif ans**4 < x:
        print(ans, "is too low")
        low = ans
        ans = (high + low) / 2
        
    if count >= 20:
        break
print(f"The cubed root of {x} is approximately {ans}\nnumber of iterations = {count}")"""


# Problem 2 - Functions
# Write a Python function to check whether a number falls in a given range.
"""def range_check(n, high, low):
    if low > high:
        return "the last number should be lower than the second"
    return high > n > low

check_positive = range_check(20,90,5)
check_negative = range_check(15, 50, 16)
print(check_positive, check_negative)"""

# Problem 3 - Functions
# Write a Python function to check whether a number is perfect or not.
# (In number theory, a perfect number is a positive integer that is equal
# to the sum of its proper positive divisors, excluding the number itself).

"""def perfect_num(n):
    sum = 0
    for i in range(1,int(n/2 + 1)):
        if n % i == 0:
            sum += i
    return sum == n

check1 = perfect_num(6) #true
check2 = perfect_num(28) #true
check3 = perfect_num(55) #false
print(check1,check2, check3)
"""



# Problem 4 - Approximation Algorithm (see Lecture 5 slides for similar problem)
# Write an approximation algorithm to calculate the forth root of some
# number inputted by the user.
# Print the result and the number of iterations required to reach that result.
# The program should not accept negative numbers. Initial parameters epsilon
# (i.e. accuracy), initial guess, increment and num_guesses are defined below.

# example initial parameters
"""def approx(num):
    epsilon = 0.01
    ans = 0.0
    increment = 0.001
    num_guesses = 0
    while abs(ans**4 - num) >= epsilon:
        num_guesses += 1
        ans += increment
        print(f"guess {num_guesses}: {ans}")
        
    return(ans)

# check1 = approx(16) # returns 2
# print(f"\n The answer is approximately: {check1}")
# check2 = approx(81) # returns 3
# print(f"\n The answer is approximately: {check2}")
# check3 = approx(410.0625) # returns 4.5
# print(f"\n The answer is approximately: {check3}")"""

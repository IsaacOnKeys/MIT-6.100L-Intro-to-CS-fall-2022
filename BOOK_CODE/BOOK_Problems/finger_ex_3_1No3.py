"""
Finger exercise: Write a program that prints the sum of the prime
numbers greater than 2 and less than 1000. Hint: you probably want
to have a loop that is a primality test nested inside a loop that
iterates over the odd integers between 3 and 999.

"""

sum = 0
for n in range(3,999,2):
    for y in range(2,int(n/2)):
        if n % y != 0:
            print(n)
            sum = sum + n
            break
print(f"The sum of all prime numbers between 2 and 1000 equals: {sum}")
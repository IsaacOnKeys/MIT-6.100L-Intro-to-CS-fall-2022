"""Finger exercise: Write a program that prints the sum of the prime
numbers greater than 2 and less than 1000. Hint: you probably want
to use a for loop that is a primality test nested inside a for loop that
iterates over the odd integers between 3 and 999."""
total = 0
for num in range(3,999,2):
    for div in range(2, int(num**0.5) + 1):
        if num % div == 0:
            break
        else:
            print(f'{num} is prime')
            total = total + num
            print(f"The total is now {total}")
            break
print(total)

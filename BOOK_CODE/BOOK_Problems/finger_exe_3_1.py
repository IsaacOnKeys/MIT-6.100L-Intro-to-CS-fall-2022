"""
Finger exercise: Change the code in Figure 3-2 so that it returns
the largest rather than the smallest divisor. Hint: if y*z = x and y is
the smallest divisor of x, z is the largest divisor of x.

# Test if an in > 2 is pri e. I f no, print smallest divisor
x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None
for guess in range(2, x):
    print(guess)
    if x % guess == 0 :
        smallest_divisor= guess
        break   
if smallest_divisor != None:
    print('Smallest divisor of ', x, 'is', smallest_divisor)
else:
    print (x, 'is a prime number')
"""

x = int(input('Enter an integer greater than 2: '))
largest_divisor = None
if x % 2 == 0:
    print('Largest divisor of ', x, 'is', int(x/2))
else:
    for guess in range(int(x/2 - 1), 2, -2):
        print(guess)
        if x % guess == 0 :
            largest_divisor= guess
            break   
    if largest_divisor != None:
        print('Largest divisor of ', x, 'is', largest_divisor)
    else:
        print (x, 'is a prime number')

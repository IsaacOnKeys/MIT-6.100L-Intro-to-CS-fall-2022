"""
Finger exercise: What would have to be changed to make the code
in Figure 3-5 work for finding an approximation to the cube root of
both negative and positive numbers? Hint: think about changing low
to ensure that the answer lies within the region being searched.
"""

import math

# Find lower bound on ans
x=16
epsilon = 0.1
lower_bound = 0
while 2**lower_bound < x:
    lower_bound += 1
low = lower_bound - 1
high= lower_bound + 1
# Perform bisection search
ans = (high + low)/2
while abs(2**ans < x) >= epsilon:
    if 2**ans < x:
        low= ans
    else:
        high = ans
    ans = ( high + low) /2
print(ans,'is close to the log base 2 of', x)

print(math.log2(16))

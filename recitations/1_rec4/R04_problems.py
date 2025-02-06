import timeit

# Problem 1: Lamba Functions Practice
# a) Write a lambda function that calculates the cube root of a given number 
# passed in as an argument
# INSERT CODE BELOW HERE

"""myroot = lambda x: x**(1/3)
print(myroot(12))"""
# b) Write a lambda function that takes in two arguments and outputs the product
# of those two numbers. 
# INSERT CODE BELOW HERE
"""product = lambda x, y: x*y
print(product(8,9))"""

# uncomment to test function
# print(f1(8))
# print(f1(4))
# print(f2(1,2))
# print(f2(4,5))



#############################################################################
# Problem 2: Practice working with Tuples:
# Write a function that counts the number of times the number 1 appears 
# in an inputted tuple.
# INSERT CODE BELOW HERE
"""def count_number_one(t:tuple) -> int:
    count = 0
    for i in t:
        if i == 1:
            count += 1
    return count"""




# uncomment to test function
# print(count_number_one((1,2,3,4,5,1,1)))  


#############################################################################
# Problem 3: Practice working with Python Tuples
# Write a Function that takes in two tuples and outputs a single tuple containing 
# only common elements of both tuples. 
# INSERT CODE BELOW HERE

"""def common_elements(tupleA:tuple, tupleB:tuple):
    myArr = []

    for n in tupleA:
        if n in tupleB:
            myArr.append(n)
    return tuple(myArr)

# Better Yet:

def common_elements2(tupleA:tuple, tupleB:tuple):
    newSet = (set(tupleA) & set(tupleB))
    return tuple(newSet)

# MIT's solution:
def common_elements3(tup1, tup2):
    output_tuple = ()
    for x in tup1:
        for y in tup2:
            if x == y:
                output_tuple += (x,)
    return output_tuple"""


# uncomment to test function
#

#############################################################################
# Problem 4: Practice working with Python Lists
# Write a Python program to remove sublists from a given list of lists, which 
# contain an element outside a given range.
# e.g 
# Original list:
# [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# After removing sublists from a given list of lists, which contain an 
# element outside the given range of 12 - 20 (inclusive):
# [[13, 14, 15, 17]]
# INSERT CODE BELOW HERE

def remove_list_range(l: list, num1, num2) -> list:
    if num1 < num2:
        minNum, maxNum = num1, num2
    else:
        maxNum, minNum = num1, num2
    lPrime = []
    for sublist in l:
        for index in sublist:
            if index > minNum or index > maxNum:
                print("Before: ", lPrime)
                lPrime.append(sublist)
                print("After: ", lPrime)
    return lPrime

# uncomment to test function
print(remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]], 13, 17))


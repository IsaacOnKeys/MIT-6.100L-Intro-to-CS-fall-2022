# Finger Exercise Lecture 10
# Implement the function that meets the specifications below:
def is_even(n):
    return n % 2 == 0

def is_positive(n):
    return n > 0

def less_than_ten(n):
    return n < 10

Lf = [is_even, is_positive, less_than_ten]

def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    # Your code here

    for i in Lf:
        if i(n) != True:
            return False
        return True


  

# MIT solution:

"""def all_true(n, Lf):
    flag = True
    for f in Lf:
        if not f(n):
            flag = False
        break
    return flag"""

# Examples:  
print(all_true(4,Lf)) #returns True
print(all_true(11,Lf)) # Returns False
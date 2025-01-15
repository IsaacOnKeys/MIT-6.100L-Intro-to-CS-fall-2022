"""
Finger exercise: Write a program that examines three variables—
x, y, and z—and prints the largest odd number among them. If none
of them are odd, it should print the smallest value of the three.
"""

def largest_odd_num(x,y,z):
    
    largest = None
    smallest = None
    for name, value in {'x':x, 'y':y, 'z':z}.items():
        if name[value] % 2 != 0:
            if largest ==  None:
                largest = name[value]
            elif name[value] > largest:
                largest = name[value]
        elif smallest ==  None:
            smallest = name[value]
        elif name[value] < smallest:
            smallest = name[value]
        if largest != None:
            return largest
        else: return smallest

        
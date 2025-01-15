"""
Finger exercise: Write a program that examines three variables—
x, y, and z—and prints the largest odd number among them. If none
of them are odd, it should print the smallest value of the three.
"""

def largest_odd_num(x,y,z):
    
    num_arr = [x,y,z]
    largest = float('-inf')
    smallest = float('inf')

    for num in range(len(num_arr)):
        if num_arr[num] != int(num_arr[num]):
            pass
        if num_arr[num] % 2 != 0:
            if num_arr[num] > largest:
                largest = num_arr[num]
        elif num_arr[num] <  smallest:
             smallest = num_arr[num]
    if largest != float('-inf'):
            return largest
    else: return smallest

"""
Finger Exercise Lecture 5
Assume you are given a string variable named my_str. Write a piece of Python code that prints out a new string containing the even indexed characters of my_str. For example, if my_str = "abcdefg" then your code should print out aceg."""

my_string = input(f"Please enter a word or sentence")
new_string = ""
for c in range(0, len(my_string),2):
 new_string += my_string[c]
    

print (new_string)

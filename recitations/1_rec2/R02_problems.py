####################################################################################
# Practice Problem 1
# Write a program that takes your name as an Input and Outputs the length of your name minus 5.

# Insert code below
# name = input("What is your name?")
# print(len(name) - 5)

####################################################################################
# Practice Problem 2
# Write a program to remove the nth character from a non empty string.
# Print the old string and the new string.



# Insert code below
# test_string = "We want to remove the nth character from this string"
# n = 8
# string1 = test_string[0:n -1]
# string2 = test_string[n:]
# print(string1+string2) 


####################################################################################
# Practice Problem 3
# Write a program which answers the following:
# Does a given string have length greater than 10 or less than 5? If True, output True. If False, output False.


# Insert code below

# my_string = "This is my string"  # example string - modify to test
# strLen = len(my_string) > 10 or len(my_string) < 5
# print(strLen)


####################################################################################
# Practice Problem 4
# Write a program which answers the following using a for loop:
# Count the number of e's in the following string

my_string = "How many times is the letter e in this string?"
count = 0
for c in my_string:
    if c == "e" or c == "E":
        count += 1
print(count)

# Insert code below

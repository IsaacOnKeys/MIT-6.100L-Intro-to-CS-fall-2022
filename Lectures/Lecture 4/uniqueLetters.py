## Assume you are given a string lf lowercase letters in variable s. Count how many unique letters there are in the string. For example, if s = "abca", then your code prints 3.
def check(s):
    charMap = {}
    counter = 0
    # s = "abracadabra"
    for i, char in enumerate(s):
        if char not in charMap:
            counter += 1
            charMap[char] = i
        else:
            pass
    return counter


answer = check("abracadabra")
print(answer)


##simplified version:
def check(s):
    charMap = {}
    counter = 0
    for i, char in enumerate(s):
        if char not in charMap:
            counter += 1
            charMap[i] = char
        else:
            pass
    return counter


check("abracadabra")

def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    Total = 0
    for s in L:
            if type(s) == list:
                for i in s:
                    if type(i) == str:
                        Total += len(i)
                    else:
                        raise ValueError("Index is not a string.")
            elif type(s) == str: 
                Total += len(s)
            else:
                raise ValueError("Index is not a string.")
    return Total    


# Examples:
# print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
# print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
# print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError

"""
22. Write a Python program to compute the sum of the ASCII values of the upper-case characters in a given string.
Input:
PytHon ExerciSEs
Output:
373
Input:
JavaScript
Output:
157
"""


def get_ascii_for_upper(target_string):
    sum = 0
    for i in target_string:
        if i.isalpha() == True and i.isupper() == True:
            sum += ord(i)
    return sum

print(get_ascii_for_upper('JavaScript'))
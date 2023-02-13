"""
12. Write a Python program to check whether the given strings are palindromes or not. Return True otherwise False.
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']
Output:
[False, True, True, False, False]
"""

condition_list = []

def check_palindrome(target_list):
    for i in target_list:
        if i == i[::-1]:
            condition_list.append(True)
        else:
            condition_list.append(False)
    return condition_list

print(check_palindrome(['palindrome', 'madamimadam', '', 'foo', 'eyes']))
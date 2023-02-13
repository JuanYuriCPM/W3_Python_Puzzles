"""
21. Write a Python program to check, for each string in a given list, whether the last character is an isolated letter or not.
 Return True otherwise False.
Input:
['cat', 'car', 'fear', 'center']
Output:
[False, False, False, False]
Input:
['ca t', 'car', 'fea r', 'cente r']
Output:
[True, False, True, True]
"""

def check_isolated_last_letter(target_list):
    checklist = []
    for i in target_list:
            if i[-2] == ' ' and i[-1] != ' ':
                checklist.append(True)
            else:
                checklist.append(False)
    return checklist

print(check_isolated_last_letter(['ca t', 'car', 'fea r', 'cente r']))
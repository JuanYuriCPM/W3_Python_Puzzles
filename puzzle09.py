"""
9. Write a Python program to find a list of integers containing exactly four distinct values,
such that no integer repeats twice consecutively among the first twenty entries.
Input:
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
Output:
True
Input:
[1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
Output:
False
Input:
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
Output:
False
"""

def check_conditions(int_list):
    previous = None
    for i in int_list[1:21:1]:
        if i == previous:
            return False
        previous = i
    if len(set(int_list)) == 4:
        return True
    else:
        return False

print(check_conditions([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]))
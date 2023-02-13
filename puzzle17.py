"""
17. Write a Python program to create a string consisting of non-negative integers up to n inclusive.
Input:
4
Output:
0 1 2 3 4
Input:
15
Output:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
"""

def int_list_creation(target_number):
    return [i for i in range(0,target_number+1)]

print(int_list_creation(15))
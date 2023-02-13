"""
7. Write a Python program to check a given list of integers where the sum of the first i integers is i. Go to the editor
Input:
[0, 1, 2, 3, 4, 5]
Output:
False
Input:
[1, 1, 1, 1, 1, 1]
Output:
True
Input:
[2, 2, 2, 2, 2]
Output:
False
"""
def sum_in_range_i(range_i):
    sum = 0
    for i in range(1,range_i+1):
        sum += i
    return sum

def check_condition(int_list):
    for i in int_list:
        if i != sum_in_range_i(i):
            return False
    return True

print(check_condition([2, 2, 2, 2, 2]))
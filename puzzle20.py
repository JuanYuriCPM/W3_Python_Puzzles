"""
20. Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.
Input:
[1, 2, 3, 4, 5, 6]
Output:
Increasing.
Input:
[6, 5, 4, 3, 2, 1]
Output:
Decreasing.
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
Not a monotonic sequence!
"""

def check_decreasing(target_list):
    previous = target_list[0]
    for i in target_list[1::]:
        if i >= previous:
            return False
        return True

def check_increasing(target_list):
    previous = target_list[0]
    for i in target_list[1::]:
        if i <= previous:
            return False
        return True

def check_direction(target_list):
    if check_decreasing(target_list) == True:
        return 'Decreasing.'
    elif check_increasing(target_list) == True:
        return 'Increasing.'
    else:
        return 'Not a monotonic sequence!'

print(check_direction([1, 2, 3, 4, 5, 6]))


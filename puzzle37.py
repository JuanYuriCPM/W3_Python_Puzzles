"""
37. Write a Python program to find the largest integer divisor of a number n that is less than n.
Input: 18
Output:
9
Input: 100
Output:
50
Input: 102
Output:
51
Input: 500
Output:
250
Input: 1000
Output:
500
Input: 6500
Output:
3250
"""

def find_highest_divisor(number_n):
    divisor_tracker = 2
    if number_n < 1:
        return 'Positive integers only'
    elif number_n == 1:
        return 1
    while divisor_tracker < number_n/2:
        if number_n % divisor_tracker == 0:
            return number_n / divisor_tracker
        divisor_tracker += 1
    return 1

print(find_highest_divisor(19))
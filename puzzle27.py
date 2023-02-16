"""
27. Write a Python program to find x that minimizes the mean squared deviation from a given list of numbers.
Input:
[4, -5, 17, -9, 14, 108, -9]
Output:
17.142857142857142
Input:
[12, -2, 14, 3, -15, 10, -45, 3, 30]
Output:
1.1111111111111112
"""

def mean_square_deviation_minimizer(target_list):
    return sum(target_list) / len(target_list)

print(mean_square_deviation_minimizer([4, -5, 17, -9, 14, 108, -9]))
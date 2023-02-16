"""
34. Write a Python program to find the sum of the numbers in a given list among the first k with more than 2 digits. Go to the editor
Input: [4, 5, 17, 9, 14, 108, -9, 12, 76]
Value of K: 4
Output:
0
Input: [4, 5, 17, 9, 14, 108, -9, 12, 76]
Value of K: 6
Output:
108
Input: [114, 215, -117, 119, 14, 108, -9, 12, 76]
Value of K: 5
Output:
331
Input: [114, 215, -117, 119, 14, 108, -9, 12, 76]
Value of K: 1
Output:
114
"""

def sum_of_more_than_2_digits(target_list, target_range):
    index_tracker = 0
    total_sum = 0
    for i in target_list:
        if index_tracker < target_range and len(str(abs(i))) > 2:
            total_sum += i
        index_tracker += 1
    return total_sum

print(sum_of_more_than_2_digits([114, 215, -117, 119, 14, 108, -9, 12, 76], 5))
    
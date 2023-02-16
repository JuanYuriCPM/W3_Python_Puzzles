"""
36. Write a Python program to find the largest k numbers from a given list of numbers.
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6]
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6, 5]
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6, 5, 5]
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6, 5, 5, 4]
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6, 5, 5, 4, 3]
"""

def find_k_largest_numbers(target_list, k):
    sorted_list = sorted(target_list)
    k_highest_numbers = []
    for i in sorted_list[::-1]:
        if len(k_highest_numbers) < k:  
            k_highest_numbers.append(i) 
    return k_highest_numbers

print(find_k_largest_numbers([1, 2, 3, 4, 5, 5, 3, 6, 2], 2))

    

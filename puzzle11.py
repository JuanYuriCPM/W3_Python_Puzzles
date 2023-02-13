"""
11. Write a Python program to find the indexes of numbers in a given list below a given threshold.
Original list:
[0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
Threshold: 100
Check the indexes of numbers of the said list below the given threshold:
[0, 1, 2, 3, 7, 8, 9, 10]
Original list:
[0, 12, 4, 3, 49, 9, 1, 5, 3]
Threshold: 10
Check the indexes of numbers of the said list below the given threshold:
[0, 2, 3, 5, 6, 7, 8]
"""

filtered_list = []

def index_checker(target_list, threshold):
    for index, i in enumerate(target_list):
        if i < threshold:
            filtered_list.append(index)
    return filtered_list

print(index_checker([0, 12, 4, 3, 49, 9, 1, 5, 3], 10))

"""
14. Write a Python program to find the length of a given list of non-empty strings. Go to the editor
Input:
['cat', 'car', 'fear', 'center']
Output:
[3, 3, 4, 6]
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
[3, 3, 7, 5, 2, 4, 0]
"""

len_list = []

def check_string_lenght(target_list):
    for i in target_list:
        len_list.append(len(i))
    return len_list

print(check_string_lenght(['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']))
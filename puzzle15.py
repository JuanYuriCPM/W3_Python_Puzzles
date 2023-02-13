"""
15. Write a Python program to find the longest string in a given list of strings.
Input:
['cat', 'car', 'fear', 'center']
Output:
center
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
shatter
"""

def find_longest_string(target_list):
    longest_string = ''
    for i in target_list:
        if len(i) > len(longest_string):
            longest_string = i
    return longest_string

print(find_longest_string(['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']))
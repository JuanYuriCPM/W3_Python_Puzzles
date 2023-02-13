"""
16. Write a Python program to find strings in a given list containing a given substring.
Input:
[(ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
['dog', 'donut', 'todo']
Input:
[(oe,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
[]
"""

def find_string(target_list):
    filtered_list = []
    for i in target_list:
        for j in i[1]:
            if i[0] in j:
                filtered_list.append(j)
    return filtered_list

print(find_string([('o',('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]))
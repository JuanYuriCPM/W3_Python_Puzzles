"""
13. Write a Python program to find strings in a given list starting with a given prefix. Go to the editor
Input:
[( ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
Output:
['dog', 'donut']
"""

filtered_list = []

def prefix_checker(target_list):
    for i in target_list:
        prefix = i[0]
        for j in i[1]:
            if j[0:2] == prefix:
                filtered_list.append(j)
    return filtered_list

print(prefix_checker([('do',('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]))
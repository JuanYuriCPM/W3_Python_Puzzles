"""
28. Write a Python program to select a string from a given list of strings with the most unique characters.
Input:
['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
Output:
abcdefhijklmnop
Input:
['Green', 'Red', 'Orange', 'Yellow', '', 'White']
Output:
Orange
"""

def most_unique_characters(target_list):
    most_UC = ''
    for i in target_list:
        if len(set(i)) > len(set(most_UC)):
            most_UC = i
    return most_UC

print(most_unique_characters(['Green', 'Red', 'Orange', 'Yellow', '', 'White']))
    

"""
33. Write a Python program to find the positions of all uppercase vowels (not counting Y) in even indices of a given string.
Input: w3rEsOUrcE
Output:
[6]
Input: AEIOUYW
Output:
[0, 2, 4]
"""

def check_uppercase_index(target_string):
    uppercase_vowels = 'AEIOU'
    index_tracker = 0
    list_of_indices = []
    for i in target_string:
        if i in uppercase_vowels and index_tracker % 2 == 0:
            list_of_indices.append(index_tracker)
        index_tracker += 1
    return list_of_indices

print(check_uppercase_index('AEIOUYW'))
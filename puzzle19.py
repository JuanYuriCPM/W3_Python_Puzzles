"""
19. Write a Python program to split a given string (s) into strings if there is a space in s,
otherwise split on commas if there is a comma,
otherwise return the list of lowercase letters in odd order (order of a = 0, b = 1, etc.).
Input:
a b c d
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['a', 'b', 'c', 'd']
Input:
a,b,c,d
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['a', 'b', 'c', 'd']
Input:
abcd
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['b', 'd']
"""

def split_strings(target_string):
    if ' ' in target_string:
        return target_string.split(' ')
    elif ',' in target_string:
        return target_string.split(',')
    else:
        lower_case_odd_order = []
        for i in enumerate(target_string):
            if i[0] % 2 != 0 and i[1] == i[1].lower():
                lower_case_odd_order.append(i[1])
        return lower_case_odd_order

print(split_strings('abcd'))
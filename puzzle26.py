"""
26. Write a Python program to find the largest number where commas or periods are decimal points.
Input:
['100', '102,1', '101.1']
Output:
102.1
"""

def check_for_decimals(target_list):
    largest_decimal = 0
    for i in target_list:
        if ',' in i:
            i = i.replace(',', '.')
        if i.count('.') == 1 and float(i) > largest_decimal:
            largest_decimal = float(i)
    if largest_decimal == 0:
        return 'No decimals detected'
    return largest_decimal

print(check_for_decimals(['100', '102,1', '101.1']))


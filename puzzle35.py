"""
35. Write a Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.
Input: 123456789
Output:
945
Input: 2468
Output:
0
Input: 13579
Output:
945
"""

def product_of_odd_digits(target_number):
    total_product = None
    for i in str(target_number):
        if int(i) % 2 != 0:
            if total_product == None:
                total_product = int(i)
            else:
                total_product *= int(i)
    if total_product == None:
        return 0
    return total_product

print(product_of_odd_digits(123456789))
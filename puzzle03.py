"""
3. Write a Python program that accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34.
Input:
922
Output:
True
Input:
914
Output:
False
Input:
854
Output:
True
Input:
854
Output:
True
"""

def check_conditions(number):
    if number > (4**4) and number % 34 == 4:
        return True
    else:
        return False

print(check_conditions(854))
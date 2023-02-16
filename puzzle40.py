"""
40. Write a Python program to find strings that, when case is flipped, give a target where vowels are replaced by characters two later.
Input: Python
Output:
pYTHQN
Input: aeiou
Output:
CGKQW
Input: Hello, world!
Output:
hGLLQ, WQRLD!
Input: AEIOU
Output:
cgkqw
"""

def vowel_swapper(target_string):
    swapped_string = target_string.swapcase()
    vowels = 'aeiouAEIOU'
    for i in vowels:
        swapped_string = swapped_string.translate({ord(i): ord(i)+2})
    return swapped_string

print(vowel_swapper('AEIOU'))
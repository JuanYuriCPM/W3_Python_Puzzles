"""
4. We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones.
Each pile must have more stones than the previous pile but as few as possible.
Write a Python program to find the number of stones in each pile.
Input: 2
Output:
[2, 4]
Input: 10
Output:
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
Input: 3
Output:
[3, 5, 7]
Input: 17
Output:
[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
"""

def stone_pile_making(n):
    stone_piles = [n]
    sum = n
    for i in range(1,n):
        sum += 2
        stone_piles.append(sum)
    return stone_piles

print(stone_pile_making(10))


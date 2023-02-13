"""
1. Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True
"""

def find_nineteen_twice_and_five_thrice(int_list):
    verification_list_19 = []
    verification_list_5 = []
    for i in int_list:
        if i == 19:
            verification_list_19.append(i)
        if i == 5:
            verification_list_5.append(i)
    if len(verification_list_19) == 2 and len(verification_list_5) >= 3:    
        return True
    else:
        return False

print(find_nineteen_twice_and_five_thrice([19,15,15,5,3,3,5,2]))

"""
Sample solution:

def test(nums):
    return nums.count(19) == 2 and nums.count(5) >= 3
nums = [19,19,15,5,3,5,5,2]
print("Original list:")
print(nums)
print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
print(test(nums))
nums = [19,15,15,5,3,3,5,2]
print("\nOriginal list:")
print(nums)
print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
print(test(nums))
nums = [19,19,5,5,5,5,5]
print("\nOriginal list:")
print(nums)
print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
print(test(nums))
"""
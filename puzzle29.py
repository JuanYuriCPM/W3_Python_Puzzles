"""
29. Write a Python program to find the indices of two numbers that sum to 0 in a given list of numbers.
Input:
[1, -4, 6, 7, 4]
Output:
[4, 1]
Input:
[1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
Output:
[1, 7]
"""

"""def sum_loop(target_list, target_int):
    tracker = 0
    while tracker != len(target_list):
        if target_int + target_list[tracker] == 0:"""
"""
def get_index(target_list):
    indexed_list = enumerate(target_list)
    for i in indexed_list[1]:
        if i in analyzed_list:
            current_zero_sum.append(indexed_list[0])
"""

def zero_sum(target_list):
    for i in target_list:
        if -i in target_list:
            return [target_list.index(i), target_list.index(-i)]
            
    
print(zero_sum([1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]))
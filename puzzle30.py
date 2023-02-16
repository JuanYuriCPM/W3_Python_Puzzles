"""
30. Write a Python program to find a list of strings that have fewer total characters (including repetitions).
Input:
[['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
Output:
['this', 'list', 'is', 'narrow']
Input:
[['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
Output:
['Red', 'Black', 'Pink']
"""
def get_highest_char_count(target_list):
    tracker = -1
    total_char_count  = 0
    current_low_index = None
    for i in target_list:
        tracker += 1
        for j in i:
            total_char_count += len(j)
        if current_low_index == None:
            current_low_index = tracker
        elif total_char_count < current_low_index:
            current_low_index = tracker
        total_char_count = 0
    return target_list[current_low_index]

print(get_highest_char_count([['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]))
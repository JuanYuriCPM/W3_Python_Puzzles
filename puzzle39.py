"""
39. Write a Python program to determine which triples sum to zero from a given list of lists. Go to the editor
Input: [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]
Output:
[False, True, True, False, True]
Input: [[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]
Output:
[True, True, False, False, False]
"""

def triple_sums(target_list):
    total_sum = 0
    list_of_results = []
    for i in target_list:
        for j in i:
            total_sum += j
        if total_sum == 0:
            list_of_results.append(True)
        else:
            list_of_results.append(False)
        total_sum = 0
    return list_of_results

print(triple_sums([[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]))
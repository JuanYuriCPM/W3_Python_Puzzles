"""
38. Write a Python program to sort the numbers in a given list by the sum of their digits.
Input: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Output:
[10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19]
Input: [23, 2, 9, 34, 8, 9, 10, 74]
Output:
[10, 2, 23, 34, 8, 9, 9, 74]
"""
def sort_by_sum_of_digits(target_list):
    number_sorted_list = []
    sum_and_number_sorted_list = []
    sum_total = 0
    for i in target_list:
        for j in str(i):
            sum_total += int(j)
        sum_and_number_sorted_list.append([sum_total, i])
        sum_total = 0
    for i in sorted(sum_and_number_sorted_list):
        number_sorted_list.append(i[1])
    return number_sorted_list
        

print(sort_by_sum_of_digits([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
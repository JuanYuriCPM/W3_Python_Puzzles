"""
25. Write a Python program to find the XOR of two given strings interpreted as binary numbers.
Input:
['0001', '1011']
Output:
0b1010
Input:
['100011101100001', '100101100101110']
Output:
0b110001001111
"""

def xor_strings(target_list):
    counter = 0
    string_answer = ''
    for i in target_list[0]:
        if i == target_list[1][counter]:
            string_answer += '0'
        else:
            string_answer += '1'
        counter += 1
    final_string = '0b' + string_answer
    return final_string

print(xor_strings(['100011101100001', '100101100101110']))

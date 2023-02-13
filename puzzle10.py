"""
10. Given a string consisting of whitespace and groups of matched parentheses, 
write a Python program to split it into groups of perfectly matched parentheses without any whitespace.
Input:
( ()) ((()()())) (()) ()
Output:
['(())', '((()()()))', '(())', '()']
Input:
() (( ( )() ( )) ) ( ())
Output:
['()', '((()()()))', '(())']
"""

parentheses_list = []
combined_list = []

def matched_parentheses(target_string):
    for i in target_string:
        if i != ' ':
            parentheses_list.append(i)
    return parentheses_list

def combine_parentheses(target_string):
    separated_list = []
    concatenated_string = ''
    for i in target_string:
        separated_list.append(i)
        if separated_list.count('(') == separated_list.count(')'):
            for i in separated_list:
                concatenated_string += i
            combined_list.append(concatenated_string)
            separated_list = []
            concatenated_string = ''
    return combined_list

print(combine_parentheses(matched_parentheses('() (( ( )() ( )) ) ( ())')))
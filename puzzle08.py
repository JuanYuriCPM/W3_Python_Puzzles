"""
8. Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.
Input: W3resource Python, Exercises.
Output:
[['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
Input: The dance, held in the school gym, ended at midnight.
Output:
[['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
Input: The colors in my studyroom are blue, green, and yellow.
Output:
[['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]
"""
import re

list_of_separators = []
list_of_words = []

def separate_lists(string):
    list_of_words = re.split(r'[ ,]+', string)
    split_list = re.split(r"([ ,]+)", string)
    for i in split_list:
        if i not in list_of_words:
            list_of_separators.append(i)
    return list_of_separators, list_of_words

print(separate_lists('The dance, held in the school gym, ended at midnight.'))
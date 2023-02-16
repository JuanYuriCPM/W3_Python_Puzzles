"""
31. Write a Python program to find the coordinates of a triangle with given side lengths.
Input:
[3, 4, 5]
Output:
[[0.0, 0.0], [3, 0.0], [3.0, 4.0]]
Input:
[5, 6, 7]
Output:
[[0.0, 0.0], [5, 0.0], [3.8, 5.878775382679628]]
"""
import math

def get_coordinates_of_triangle(target_list):
    sorted_list = sorted(target_list)
    side_a = sorted_list[0]
    side_b = sorted_list[1]
    side_c = sorted_list[2]
    squares_formula = (side_c**2) + (side_a**2) - (side_b**2)
    coordinate_1 = [0,0]
    coordinate_2 = [0, sorted_list[0]]
    coordinate_3 = [squares_formula/(2*side_a) , math.sqrt((side_c**2) - ((squares_formula**2)/(4*(side_a**2))))]
    return coordinate_1, coordinate_2, coordinate_3
    
    
    

print(get_coordinates_of_triangle([5, 6, 7]))
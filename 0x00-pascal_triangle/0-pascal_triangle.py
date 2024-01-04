#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""

def pascal_triangle(n):
    """Generates Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list of lists: A list of lists representing Pascal's Triangle.
    """
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize an empty list to store Pascal's Triangle
    pascal_triangle_list = []

    # Iterate through each row
    for i in range(n):
        # Initialize a new row
        pascal_triangle_list.append([])
        # The first element in each row is always 1
        pascal_triangle_list[i].append(1)

        # Iterate through each element in the row (excluding the first and last)
        for j in range(1, i):
            # Calculate the value using the values from the previous row
            x = pascal_triangle_list[i-1][j-1]
            y = pascal_triangle_list[i-1][j]
            # Append the calculated value to the current row
            pascal_triangle_list[i].append(x + y)

        # If it's not the first row, append 1 to complete the row
        if n != 0 and i != 0:
            pascal_triangle_list[i].append(1)

    return pascal_triangle_list

# Example usage:
# result = pascal_triangle(5)
# print(result)
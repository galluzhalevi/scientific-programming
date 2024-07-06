from typing import List


# Function to create Pascal's triangle up to nth row
def create_pascal_triangle(n):
    # Initialize Pascal's triangle with first two rows
    pascal_triangle = [[1], [1, 1]]

    # Iterate to generate subsequent rows
    for i in range(1, n - 1):
        pascal_triangle.append(pascal_row(pascal_triangle[i]))

    return pascal_triangle


# Function to generate a row of Pascal's triangle based on the previous row
def pascal_row(last_row: List[int]):
    # Calculate values for the new row based on the previous row
    return [1] + [last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)] + [1]


# Function to print Pascal's triangle
def pascal_print(triangle: List[list]):
    # Iterate over each row and print it
    for row in triangle:
        print(row, end=' | ')
        print(f'row sum = {sum(row)}')


# Create Pascal's triangle with 10 rows and print it
pascal_print(create_pascal_triangle(10))


# Output from execution:
# [1] | row sum = 1
# [1, 1] | row sum = 2
# [1, 2, 1] | row sum = 4
# [1, 3, 3, 1] | row sum = 8
# [1, 4, 6, 4, 1] | row sum = 16
# [1, 5, 10, 10, 5, 1] | row sum = 32
# [1, 6, 15, 20, 15, 6, 1] | row sum = 64
# [1, 7, 21, 35, 35, 21, 7, 1] | row sum = 128
# [1, 8, 28, 56, 70, 56, 28, 8, 1] | row sum = 256
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1] | row sum = 512
# 
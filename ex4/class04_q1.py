# Define a list of numbers
numbers = [306,  83, 156, 129, 115, 100, 331, 96, 116, 363, 478, 309, 358, 459, 216, 491, 272, 245, 401, 345, 348, 345,
           22, 243, 265, 460, 247,  44, 184, 469, 171, 138, 261, 262, 423, 20, 113, 470, 361, 14, 163, 254, 159, 498,
           214, 39, 173, 147, 358,  27]

# Print numbers from the list that are divisible by 5
print(f'numbers divisible by 5: {[n for n in numbers if (n % 5) == 0]}')


# Output from execution:
# numbers divisible by 5: [115, 100, 245, 345, 345, 265, 460, 20, 470]
# 
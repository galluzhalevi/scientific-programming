# Create a list of numbers from 2 to 100
numbers = list(range(2, 101))

# Iterate through numbers from 2 to 100
for n in range(2, 101):
    # Remove multiples of 2, except 2 itself
    if (n % 2 == 0) and (n > 2):
        numbers.remove(n)
    # Remove multiples of 3, except 3 itself
    elif (n % 3 == 0) and (n > 3):
        numbers.remove(n)
    # Remove multiples of 5, except 5 itself
    elif (n % 5 == 0) and (n > 5):
        numbers.remove(n)
    # Remove multiples of 7, except 7 itself
    elif (n % 7 == 0) and (n > 7):
        numbers.remove(n)

# Print the remaining prime numbers
print(f'\nPrime numbers: {numbers}')

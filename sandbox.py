import random
import pandas as pd
import os
from fractions import Fraction

# Define a constant
TWO_ROOTS = 1000
ONE_ROOT = 500
NO_ROOTS = 500


def sum_denominator(rational1, rational2):
    # Create Fraction objects from the rational numbers
    frac1 = Fraction(rational1[0], rational1[1])
    frac2 = Fraction(rational2[0], rational2[1])

    # Calculate the sum
    sum_frac = frac1 + frac2

    # Return the denominator of the sum
    return sum_frac.denominator


def create_two_roots_quadratic():
    # Define the probabilities
    both_integers_probability = 0.5
    one_integer_one_rational_probability = 0.25
    both_rationals_probability = 0.25

    # Generate a random number between 0 and 1
    rand_num = random.random()

    # Generate roots based on the random number
    if rand_num <= both_integers_probability:
        # Both roots are integers
        roots = [random.randint(-10, 10) for _ in range(2)]
    elif rand_num <= both_integers_probability + one_integer_one_rational_probability:
        # One root is an integer, the other is a rational number
        roots = [random.randint(-10, 10), random.randint(-10, 10) / random.randint(2, 10)]
    else:
        # Both roots are rational numbers
        roots = [random.randint(-10, 10) / random.randint(2, 10) for _ in range(2)]

    # Convert roots to Fraction instances
    roots = [Fraction(root).limit_denominator(10) if isinstance(root, float) else root for root in roots]

    # Calculate the coefficients a, b, and c from the roots
    a = 1  # We can choose a to be 1 without loss of generality
    b = -sum(roots)
    c = roots[0] * roots[1]

    # If at least one root is a fraction, multiply the coefficients a, b, and c by the common denominator
    if any(isinstance(root, Fraction) for root in roots):
        common_denom = sum_denominator((roots[0], 1), (roots[1], 1))
        a, b, c = [int(coeff * common_denom) for coeff in (a, b, c)]

    return a, b, c


def create_one_root_quadratic():
    # Define a constant
    integer_root_probability = 0.65

    # Generate a random number between 0 and 1
    rand_num = random.random()

    # Generate root based on the random number
    if rand_num <= integer_root_probability:
        # The root is an integer
        root = random.randint(-10, 10)
    else:
        # The root is a rational number
        root = random.randint(-10, 10) / random.randint(2, 10)

    # Convert root to Fraction instance if it is a float
    root = Fraction(root).limit_denominator(10) if isinstance(root, float) else root

    # Calculate the coefficients a, b, and c from the root
    a = 1  # We can choose a to be 1 without loss of generality
    b = -2 * root
    c = root * root

    # If the root is a fraction, multiply the coefficients a, b, and c by the denominator of the root
    if isinstance(root, Fraction):
        a, b, c = [int(coeff * root.denominator) for coeff in (a, b, c)]

    return a, b, c


def create_no_roots_quadratic():
    # Generate two random integers a and b
    a = random.randint(1, 10)  # a should not be 0 to avoid a linear equation
    b = random.randint(-10, 10)

    # Calculate c as b^2 + 1 to ensure the discriminant is negative
    c = b**2 + 1

    # Generate a random number between 0 and 1
    rand_num = random.random()

    # If the random number is less than 0.5, multiply a, b, and c by -1
    if rand_num < 0.5:
        a, b, c = -a, -b, -c

    return a, b, c


def write_quadratic(a, b, c):
    # Check if a is 1 or -1
    if a == 1:
        a_str = ''
    elif a == -1:
        a_str = '-'
    else:
        a_str = str(a)

    # Check if b is 1, -1 or 0
    if b == 1:
        b_str = '+x'
    elif b == -1:
        b_str = '-x'
    elif b < 0:
        b_str = str(b) + 'x'
    elif b == 0:
        b_str = ''
    else:
        b_str = '+' + str(b) + 'x'

    # Check if c is positive, negative or 0
    if c < 0:
        c_str = str(c)
    elif c == 0:
        c_str = ''
    else:
        c_str = '+' + str(c)

    # Return the string representation of the quadratic equation
    return f"{a_str}x^2{b_str}{c_str}"


# Check if the file exists and is not empty
if os.path.exists('quadratics.csv') and os.path.getsize('quadratics.csv') > 0:
    # Open the file in write mode to clear it
    open('quadratics.csv', 'w').close()


# Create a list to store the coefficients and string representations
quadratics = []

# Loop TWO_ROOTS times
for _ in range(TWO_ROOTS):
    # Generate a quadratic equation
    a, b, c = create_two_roots_quadratic()
    # Get the string representation of the quadratic equation
    quad_str = write_quadratic(a, b, c)
    # Append the coefficients and string representation to the list
    quadratics.append([a, b, c, quad_str])

# Loop ONE_ROOT times
for _ in range(ONE_ROOT):
    # Generate a quadratic equation with one root
    a, b, c = create_one_root_quadratic()
    # Get the string representation of the quadratic equation
    quad_str = write_quadratic(a, b, c)
    # Append the coefficients and string representation to the list
    quadratics.append([a, b, c, quad_str])

# Loop NO_ROOTS times
for _ in range(NO_ROOTS):
    # Generate a quadratic equation with no roots
    a, b, c = create_no_roots_quadratic()
    # Get the string representation of the quadratic equation
    quad_str = write_quadratic(a, b, c)
    # Append the coefficients and string representation to the list
    quadratics.append([a, b, c, quad_str])

random.shuffle(quadratics)

# Convert the list to a DataFrame
df = pd.DataFrame(quadratics, columns=['a', 'b', 'c', 'equation'])

print(quadratics[:9])

# Save the DataFrame to a CSV file
df.to_csv('quadratics.csv', index=False)
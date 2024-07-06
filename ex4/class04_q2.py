# Import the math module for mathematical operations
import math

# Prompt the user to enter a number and convert it to an integer
N = int(input("Enter a number: "))


# Define a function to find prime numbers up to a given number n
def prime_upto(n):
    # If the input number is less than or equal to 2, return a set containing 2 (the smallest prime number)
    if n <= 2: return {2}

    # Create a set containing numbers from 2 to n
    numbers_upto_n = set(range(2, n + 1))

    # Iterate through prime numbers up to the square root of n
    for p in iter(prime_upto(math.isqrt(n))):
        # Remove multiples of each prime number from the set
        numbers_upto_n -= set(range(2 * p, n + 1, p))

    # Return the set of prime numbers up to n
    return numbers_upto_n


# Print the prime numbers up to the user-input number N using the prime_upto function
print(f'Prime up to {N}: {prime_upto(N)}')

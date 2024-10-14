import random
import sys

# Number of integers to generate
num_integers = 1000

# Define the range of integers
min_value = 0
max_value = sys.maxsize  # This is the maximum integer value supported by Python

# Generate random integers
random_integers = [random.randint(min_value, max_value) for _ in range(num_integers)]

# Write the integers to a text file
with open('random_integers.txt', 'w') as file:
    for integer in random_integers:
        file.write(f"{integer}\n")

print(f"Generated {num_integers} random integers and saved to 'random_integers.txt'")


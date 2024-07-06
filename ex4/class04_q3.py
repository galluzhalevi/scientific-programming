import numpy as np
import matplotlib.pyplot as plt

SIZE = 1000000

# Generate two sets of random numbers representing two dice rolls and sum them up
dice_sums = np.random.randint(1, 7, size=SIZE) + np.random.randint(1, 7, size=SIZE)

# Count the occurrences of each sum from 2 to 12
results = {i: list(dice_sums).count(i) for i in range(2, 13)}

# Calculate the expected frequency for each sum (assuming a fair dice)
expected_frequency = SIZE // 36

# Create a bar plot for the results
plt.bar(results.keys(), results.values())

# Calculate the linear function representing the expected frequency
m = expected_frequency
x_line = np.linspace(2, 12, 200)
y_line = - np.abs(m * (x_line - 7)) + m * 6

# Plot the linear function over the bar plot
plt.plot(x_line, y_line, color='#ff4d85', linewidth=12, alpha=0.5)

# Show the plot
plt.show()

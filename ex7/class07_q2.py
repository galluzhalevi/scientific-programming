import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='motor_eff.csv', delimiter=',')

# Create a figure and axis
fig, ax = plt.subplots()

# Generate the grid for the contour plot
speed = data[0, 1:]
torque = data[1:, 0]
efficiency = data[1:, 1:]

# Plot the filled contour
contourf = ax.contourf(speed, torque, efficiency, levels=np.linspace(0.77, 1, 512), cmap='jet')

# Add a colorbar to the plot
cbar = fig.colorbar(contourf, ax=ax)
cbar.set_label('Efficiency')

# Add titles and labels
ax.set_title('Motor Efficiency Filled Contour Plot')
ax.set_xlabel('Speed')
ax.set_ylabel('torque')

# Show the plot
plt.show()

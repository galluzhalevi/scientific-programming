import numpy as np

# Create a 3D numpy array
arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

print("Original 3D array:")
print(arr)

# Use np.where to find indices of elements greater than 15
indices = np.where(arr > 15)

print("\nIndices where condition is met:")
print(indices)
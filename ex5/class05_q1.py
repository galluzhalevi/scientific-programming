import numpy as np


# Convert radians to degrees
def rad2deg(angle_in_radians):
    normalized_angle = angle_in_radians % (2 * np.pi)
    return (normalized_angle / np.pi) * 180


# Convert degrees to radians
def deg2rad(angle_in_degrees):
    normalized_angle = angle_in_degrees % 360
    return (normalized_angle / 180) * np.pi


# Calculate area of a sector
def calc_area(angle, radius):
    return np.pi * (radius ** 2) * (angle / (2 * np.pi))


# Main function to calculate and print area
def main(angle_in_degrees=45.0, radius=20):
    radius_in_meters = radius / 100
    angle = deg2rad(angle_in_degrees)
    area = np.round(calc_area(angle, radius_in_meters), 4)

    print(f'Area of {angle_in_degrees} degrees, {radius} cm is {area} m^2')


# Test cases
main(60, 10)  # Test with custom values
main()  # Test with default values


# Output from execution:
# Area of 60 degrees, 10 cm is 0.0052 m^2
# Area of 45.0 degrees, 20 cm is 0.0157 m^2
# 
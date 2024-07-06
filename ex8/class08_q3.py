from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Define color constants
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
BAR = 345
LINE_LENGTH = 8.5

def find_pixel_cm_ratio(canvas, x_min, x_max, y_min, y_max):
    """
    Function to find the ratio of pixels to centimeters in the image.

    Parameters:
    canvas (numpy.ndarray): The image as a numpy array.
    x_min, x_max, y_min, y_max (int): The coordinates defining the area to search for the line.

    Returns:
    float: The ratio of pixels to centimeters.
    """
    # assume that the line is horizontal
    search_area = canvas[y_min:y_max, x_min:x_max]
    blacks = np.where(search_area == BLACK)

    return (np.max(blacks[1]) - np.min(blacks[1])) / LINE_LENGTH


def find_center_of_object(canvas, x_min, x_max, y_min, y_max):
    """
    Function to find the center of an object in the image.

    Parameters:
    canvas (numpy.ndarray): The image as a numpy array.
    x_min, x_max, y_min, y_max (int): The coordinates defining the area to search for the object.

    Returns:
    tuple: The coordinates of the center of the object.
    """
    search_area = canvas[y_min:y_max, x_min:x_max]
    blacks = np.where(search_area == BLACK)
    x_center = (np.min(blacks[1]) + np.max(blacks[1])) // 2
    y_center = (np.min(blacks[0]) + np.max(blacks[0])) // 2

    return x_center + x_min, y_center + y_min


def center_annotation(center):
    """
    Function to create an annotation for the center of an object.

    Parameters:
    center (tuple): The coordinates of the center of the object.

    Returns:
    str: The annotation text.
    """
    pixels_per_cm = find_pixel_cm_ratio(trimmed_image, 200, 770, 150, 300)
    x, y = center

    x_cm  = np.round(x / pixels_per_cm, 2)
    y_cm = np.round(y / pixels_per_cm, 2)

    return f'({x_cm}cm, {y_cm}cm)'

# Load and process the image
original_image = Image.open("q3_original.jpg")
original_image.thumbnail(size=(1028, 1028))

image_as_array = np.array(original_image).astype(int)
trimmed_image = np.zeros_like(image_as_array)

# Convert the image to binary
for i in range(image_as_array.shape[0]):
    for j in range(image_as_array.shape[1]):
        if np.sum(image_as_array[i, j]) > BAR:
            trimmed_image[i, j] = WHITE

# Display the image
plt.imshow(trimmed_image, cmap="gray")

# Find the centers of the objects and annotate them
coin_center = find_center_of_object(trimmed_image, 30, 250, 300, 500)
medallion_center = find_center_of_object(trimmed_image, 220, 600, 550, 900)

plt.plot(coin_center[0], coin_center[1], 'rx')
plt.annotate(center_annotation(coin_center), (coin_center[0], coin_center[1]), textcoords="offset points", xytext=(40,20), ha='center', color='r')
plt.plot(medallion_center[0], medallion_center[1], 'rx')
plt.annotate(center_annotation(medallion_center), (medallion_center[0], medallion_center[1]), textcoords="offset points", xytext=(45,-60), ha='center', color='r')

# Show the plot
plt.show()
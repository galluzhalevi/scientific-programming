from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def darker(color_channel, factor=2):
    return int(color_channel // factor)


def lighter(color_channel, factor=2):
    lighter_channel = int(color_channel * factor)
    return lighter_channel if lighter_channel <= 255 else 255


def no_ticks(ax):
    ax.set_xticks([])
    ax.set_yticks([])


def as_greyscale(image):
    rows, cols, _ = image.shape
    greyscale_image = np.zeros_like(image)
    for i in range(rows):
        for j in range(cols):
            mean_pixel = np.mean(image[i, j])
            greyscale_image[i, j] = [mean_pixel] * 3

    return greyscale_image


original_image = Image.open("q2_original.jpg")
original_image.thumbnail(size=(1028, 1028))

image_as_array = np.array(original_image).astype(int)
darker_image = np.vectorize(darker)(image_as_array)
lighter_image = np.vectorize(lighter)(image_as_array)

fig, axs = plt.subplots(2, 2, dpi=300)

axs[0][0].imshow(original_image)
axs[0][0].set_title("Original Image")
no_ticks(axs[0][0])

axs[0][1].imshow(as_greyscale(image_as_array))
axs[0][1].set_title("Greyscale Image")
no_ticks(axs[0][1])

axs[1][0].imshow(darker_image)
axs[1][0].set_title("Darker Image")
no_ticks(axs[1][0])

axs[1][1].imshow(lighter_image)
axs[1][1].set_title("Lighter Image")
no_ticks(axs[1][1])

plt.show()

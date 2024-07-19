import numpy as np
from matplotlib import pyplot as plt

# Create an image which have red and green pixels.
width, height = 500, 500
image_1 = np.zeros((height, width, 3))

for y in range(height):
    for x in range(width):
        if (x + y) % 2 == 0:
            image_1[y, x] = [1, 0, 0]  # Red
        else:
            image_1[y, x] = [0, 1, 0]  # Green

# Create another image which looks has the similar colour as the first image
red = 184
green = 174
blue = 40

image_2 = np.zeros((height, width, 3))
image_2[:, :] = [red/255, green/255, blue/255]


# Show the images
fig, ax = plt.subplots(1, 2)
fig.set_size_inches(15, 7.5)
ax[0].imshow(image_1, interpolation='none')
ax[0].set_title('Image 1')
ax[1].imshow(image_2, interpolation='none')
ax[1].set_title('Image 2')
plt.show()










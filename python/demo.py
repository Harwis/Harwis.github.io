import numpy as np
from matplotlib import pyplot as plt

# Create an empty array of size 1000 x 1000 pixels
width, height = 1000, 1000
image_array = np.zeros((height, width, 3))

# Fill the array with a pattern of red and green pixels
for y in range(height):
    for x in range(width):
        if (x + y) % 2 == 0:
            image_array[y, x] = [1, 0, 0]  # Red
        else:
            image_array[y, x] = [0, 1, 0]  # Green

# Show the image
plt.figure()
plt.imshow(image_array, interpolation='none')









# # RGB
# from PIL import Image
#
# # Define the size of the image
# width, height = 1000, 1000
#
# # Create a new image with RGB mode
# image = Image.new('RGB', (width, height))
#
# # Get the pixel map of the image
# pixels = image.load()
#
# # Define colors
# green = (0, 255, 0)
# red = (255, 0, 0)
# blue = (0, 0, 255)
#
# # Fill the image with the pattern
# for y in range(height):
#     for x in range(width):
#         if (x % 2 == 1 and y % 2 == 1):
#             pixels[x, y] = red  # Red pixel
#         elif (x % 2 == 0 and y % 2 == 0):
#             pixels[x, y] = blue  # Blue pixel
#         else:
#             pixels[x, y] = green  # Green pixel
#
#
#
#
# # Save the image
# image.save('ccd_pattern_1000x1000.png')
#
# # Display the image
# image.show()


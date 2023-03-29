import numpy as np
from PIL import Image

def create_image(red, green, blue, size=(512, 512)):
    # Normalize input values
    red_norm = 255.0 * (red - np.min(red)) / (np.max(red) - np.min(red))
    green_norm = 255.0 * (green - np.min(green)) / (np.max(green) - np.min(green))
    blue_norm = 255.0 * (blue - np.min(blue)) / (np.max(blue) - np.min(blue))

    # Create image array
    img_array = np.zeros((len(red), 3))
    img_array[:, 0] = red_norm
    img_array[:, 1] = green_norm
    img_array[:, 2] = blue_norm

    # Resize image array
    img_array = np.resize(img_array, (size[0], size[1], 3))

    # Convert numpy array to image and return
    img = Image.fromarray(np.uint8(img_array))
    return img

# Get user input for red, green, and blue values
red = np.array(input("Enter red values separated by commas: ").split(',')).astype(float)
green = np.array(input("Enter green values separated by commas: ").split(',')).astype(float)
blue = np.array(input("Enter blue values separated by commas: ").split(',')).astype(float)

# Get the output
img = create_image(red, green, blue)
img.show() 
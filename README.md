# caMicroscope - Multi-channel Imaging Support - Challenge

![Screenshot (214)](https://user-images.githubusercontent.com/102804548/228495488-5b7763d0-6fe6-4b45-b8d2-166f5eb1ba81.png)

## create_image function

```
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
```


The `create_image` function takes three numpy arrays `red`, `green`, and `blue` which represent the intensity values for the corresponding color channels of an RGB image. It also takes an optional size parameter that specifies the desired `size` of the output image.

The function first normalizes the input values of each color channel to be between 0 and 255 using min-max normalization. This is done to ensure that the intensity values of each channel are within the valid range of an 8-bit RGB image.

Then, it creates an image array by concatenating the normalized red, green, and blue channel arrays horizontally using `np.zeros` and array indexing. The resulting array has shape `(N, 3)`, where `N` is the number of pixels in the image.

Next, it resizes the image array to the desired size using np.resize.

Finally, it converts the numpy array to a PIL image using `Image.fromarray` and returns it.

Overall, the `create_image` function takes the intensity values of each color channel as input and produces a corresponding RGB image as output.

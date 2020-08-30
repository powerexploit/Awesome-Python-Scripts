
## Canny Edge-detection ##

- This script implements the sobel filter for edge detection without the use of the openCV in-built functions.
- The basic principle used here is convolution.
- A kernel, a matrix of size(3X3 or 5X5) is often chosen and is convoluted over the image.(which is a matrix of pixels)
- In RGB images there are 3 channels, while in grayscale there is only 1 channel.

## Implementation ##

- To run the scripts the user needs to run -
    pip install opencv

- The path to the image needs to be mentioned
- The image is converted to grayscale and then blurred
- The sobel kernel in the X-direction is [-1,-2,-1,0,0,0,1,2,1]
- The sobel kernel in the Y-direction is [-1,0,1,-2,0,2,-1,0,1]

## Working ##

This is the example image to begin with :

![Image](./images/start.png)

This is the final image after running the filter :

![Image](./images/end.png)

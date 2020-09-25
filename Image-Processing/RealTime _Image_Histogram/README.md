# Image Processing

Image Processing is most commonly termed as 'Digital Image Processing' and the domain in which it is frequently used is 'Computer Vision'. 
Don't be confused - we are going to talk about both of these terms and how they connect. 
Both Image Processing algorithms and Computer Vision (CV) algorithms take an image as input; however, in image processing,
the output is also an image, whereas in computer vision the output can be some features/information about the image.

## OpenCV

![](https://logodix.com/logo/1989939.png)

## Installation

### Windows
 $ pip install opencv-python
### MacOS
   $ brew install opencv3 --with-contrib --with-python3
### Linux
   $ sudo apt-get install libopencv-dev python-opencv
   
## Other Modules

  $ pip install numpy <br>
  $ pip install matplotlib
  
# About RealTime Image Histrogram
This script is used to make real-time image histogram with respect to RGB (Red, Green, Blue) colors. It starts with open the camera to capture the image using **opencv** module, and store it to your script directory. After that by using **numpy** and **matplotlib** it creates the histogram of image by mapping it through 256 gray scales.

# Output

![](https://github.com/gulshanbaraik01/Awesome-Python-Scripts/blob/Image-Process/Image-Processing/RealTime%20_Image_Histogram/Histogram_output.png)

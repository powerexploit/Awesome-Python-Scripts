HOUGH TRANSFORM

Hough transform can be used to detect lines, circles or other parametric curves. The goal is to find the location of lines in images. Hough transform can detect lines, circles and other structures if their parametric equation is known. It can give robust detection under noise and partial occlusion It can give robust detection under noise and partial occlusion.

Algorithm

1.	Perform Edge detection on the original image by suitable edge detection technique.
2.	Decide on the range of ρ and θ. Often, the range of θ is [ 0, 180 ] degrees and ρ is [ -d,d ] where d is the length of the edge image’s diagonal.
3.	Create a 2D array called the accumulator representing the Hough Space with dimension (num_rhos, num_thetas) and initialize all its values to zero.
4.	For every pixel on the edge image, check whether the pixel is an edge pixel. If it is an edge pixel, loop through all possible values of θ, calculate the corresponding ρ, find the θ and ρ index in the accumulator, and increment the accumulator base on those index pairs.
5.	Loop through all the values in the accumulator. If the value is larger than a certain threshold, get the ρ and θ index, get the value of ρ and θ from the index pair which can then be converted back to the form of y=ax+b.


INPUT IMAGE:

![image](https://user-images.githubusercontent.com/46890827/94119467-9486b280-fe6c-11ea-9a52-e0bc50e14df2.png)

OUTPUT IMAGE:

![image](https://user-images.githubusercontent.com/46890827/94119579-bc761600-fe6c-11ea-8309-f606768b1c87.png)


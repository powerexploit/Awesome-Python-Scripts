## PYTHON HANDWRITING RECOGNIZER

**1.**The first hidden layer is a convolutional layer called a Convolution2D. The layer has 32 feature maps, which with the size of 5×5 and a rectifier activation function. 
**2**This is the input layer, expecting images with the structure outline above [pixels][width][height].
**3.**Next we define a pooling layer that takes the max called MaxPooling2D. It is configured with a pool size of 2×2.
**4.**The next layer is a regularization layer using dropout called Dropout. It is configured to randomly exclude 20% of neurons in the layer in order to reduce overfitting.
**5.**Next is a layer that converts the 2D matrix data to a vector called Flatten. It allows the output to be processed by standard fully connected layers.
**6.**Next a fully connected layer with 128 neurons and rectifier activation function.
**7.**Finally, the output layer has 10 neurons for the 10 classes and a softmax activation function to output probability-like predictions for each class.

#RUNNING THE CODE
run the code with the following command 

```
python hand.py
```
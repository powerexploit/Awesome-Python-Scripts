# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 11:31:58 2020

@author: Gulshan
"""


#Importing necessary libraries for capture image and plot histrogram
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Script to capture realtime image
webcam = cv2.VideoCapture(0)  #Inititalize object for camera
i = 0
while i < 10:
    input('Press Enter to capture')
    return_value, image = webcam.read()
    cv2.imwrite('realtime'+str(i)+'.png', image)
    if i == i: #Break when value becomes greater than 1
        break
del(webcam) #Delete camera object after capture

#Script to load realtime captured image
img = cv2.imread('realtime0.png')
color = ('b','g','r')  #Create RGB Histogram
plt.figure(figsize = (10, 8))
for i, col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show() #Show Histogram
    

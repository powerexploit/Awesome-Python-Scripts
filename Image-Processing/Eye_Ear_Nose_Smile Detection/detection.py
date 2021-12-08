# Created by Anirudh Gudi
import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier('XML Files/haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('XML Files/eye.xml')
nose_cascade = cv2.CascadeClassifier('XML Files/nose.xml')
smile_cascade = cv2.CascadeClassifier('XML Files/smile.xml')
cap = cv2.VideoCapture(0)
while 1: 
    ret, img = cap.read() 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    for (x,y,w,h) in faces: 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
        eyes = eye_cascade.detectMultiScale(roi_gray) 
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
        nose = nose_cascade.detectMultiScale(roi_gray,1.2, 4) 
        for (nx,ny,nw,nh) in nose: 
            cv2.rectangle(roi_color,(nx,ny),(nx+nw,ny+nh),(255,255,0), 2) 
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        for (sx, sy, sw, sh) in smiles: 
            cv2.rectangle(roi_color,(sx, sy),(sx + sw,sy + sh), (0, 0, 255), 2) 
    cv2.imshow('img',img)
    k = cv2.waitKey(5) & 0xff
    if k == 4: 
        break
        
cap.release() 
cv2.destroyAllWindows()

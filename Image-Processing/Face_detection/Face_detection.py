import cv2    ##Import OpenCv

face = cv2.CascadeClassifier('C:/Users/91976/Desktop/haarcascade_frontalface_default.xml') ##'haarcascade_frontalface_default.xml' an opencv classifier for face detection 
cap = cv2.VideoCapture(0) ##capturevideo by webcam or your laptop default cam for webcame  => 1 and for defalut laptop camera => 2

while True:
    sucess , img = cap.read()
    gray = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY ) ##before detecting  face you should convert img or video into gray image
    faces = face.detectMultiScale( gray ,1.1 ,5 )

    for ( x , y , w , h) in faces:
        cv2.rectangle(img,( x , y ),( x*w , y*h ),(255,0,0),2)  ##will create the rectangle where face is detected

    cv2.imshow('img',img) 
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
        
cap.release()

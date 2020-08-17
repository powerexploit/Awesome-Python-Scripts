import cv2
img_file = "human.jpg" ##image file contain human on road
classifier_Human = 'human_detect.xml'  #trained car data  Link:"https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_fullbody.xml"
img=cv2.imread(img_file) #create image reader
black_and_white = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert image black and white i.e. grayscale 
Human_detect = cv2.CascadeClassifier(classifier_Human) #create classifier
Humans = Human_detect.detectMultiScale(black_and_white) #detect human in image

for (x,y,w,h) in Humans:  ## the above variable will return 4 cordinates i.e height,width,postionx,positiony
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) ##this loop will create grren rectangle when car is detected
    
cv2.imshow('Human image',img) #display image
cv2.waitKey()

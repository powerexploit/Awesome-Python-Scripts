import cv2

img_file="car2.jpg"

#trained car data  Link:"https://gist.github.com/199995/37e1e0af2bf8965e8058a9dfa3285bc6"
classifier_car='car_dect.xml'

#create image reader
img=cv2.imread(img_file)

#convert image black and white i.e. grayscale 
black_and_white=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#create classifier
car_tracker=cv2.CascadeClassifier(classifier_car)

#detect cars
cars=car_tracker.detectMultiScale(black_and_white)


## the above variable will return 4 cordinates i.e height,width,postionx,positiony


for (x,y,w,h) in cars: 
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) ##this loop will create grren rectangle when car is detected





#display image
cv2.imshow('car image',img)

cv2.waitKey()


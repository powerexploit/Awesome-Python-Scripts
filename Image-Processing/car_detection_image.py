import cv2
img_file="car2.jpg"
classifier_car='car_dect.xml'  #trained car data  Link:"https://gist.github.com/199995/37e1e0af2bf8965e8058a9dfa3285bc6"
img=cv2.imread(img_file) #create image reader
black_and_white=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert image black and white i.e. grayscale 
car_tracker=cv2.CascadeClassifier(classifier_car) #create classifier
cars=car_tracker.detectMultiScale(black_and_white) #detect cars
for (x,y,w,h) in cars:  ## the above variable will return 4 cordinates i.e height,width,postionx,positiony
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) ##this loop will create grren rectangle when car is detected
cv2.imshow('car image',img) #display image
cv2.waitKey()


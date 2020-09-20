import cv2
refpt = [] #List of refrence points

def select_roi (event,x,y,flags,param):
    global refpt #Global refrences

    if event == cv2.EVENT_LBUTTONDOWN: # When the left mouse button is cliked
        refpt = [(x , y)]

    elif event == cv2.EVENT_LBUTTONUP: # When the left mouse button is released
        refpt.append((x , y)) # recording the last coordinates
        cv2.rectangle(img_main,refpt[0],refpt[1],(0,255,0),2)
        cv2.imshow("frame",img_main)
        print("Selection Successful")

img = cv2.imread("Data/Man_United.jpeg")
img_main = cv2.resize(img,(400,400)) #Resizing image

clone = img_main.copy() # To reset the image after cropping
clone2 = img_main.copy() # To crop a section out without affecting the original image

cv2.namedWindow("frame")
cv2.setMouseCallback("frame",select_roi)

i = 1 # Numbering for saving images

while True:
    cv2.imshow("frame",img_main)
    var = cv2.waitKey(0)

    # Select a region , then press c to crop that portion

    if var == ord('c'): # Crop selected images
        
        if len(refpt) == 2:
            roi = clone2[ refpt[0][1] : refpt[1][1] , refpt[0][0] : refpt[1][0] ] # [x1:x2 , y1:y2]
            cv2.namedWindow("Crop")
            cv2.imshow("Crop",roi)
            print("Cropped")

            var2 = cv2.waitKey(0)

            if var2 == ord('s'): # Saving cropped image
                cv2.imwrite("Data/cropped image{}.png".format(i),roi)
                i = i+1
                print("image saved\n")
                cv2.destroyWindow("Crop") 
                img_main = clone.copy()
                
            elif var2 == ord('r'): # Reset
                cv2.destroyWindow("Crop")
                print("Reset\n")
                img_main = clone.copy()
                           
    elif var == ord('q'): # Exit the loop
        print("Exiting ...")
        break

cv2.destroyAllWindows()

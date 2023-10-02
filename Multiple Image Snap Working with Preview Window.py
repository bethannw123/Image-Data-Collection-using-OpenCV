import cv2 as cv
import os
import numpy as np
camera = cv.VideoCapture(0)
result, image = camera.read()
rootfolder = "C:/GTMLDataCollection/"

if result:
    cv.namedWindow("Preview Window")
    cv.imshow("Preview Window",image)
    cv.waitKey(0)
    #cv.destroyWindow("Initial Preview")

#argument 0 is given to use the default camera of the laptop
#camera = cv.VideoCapture(0)
background = np.zeros((480, 640), np.uint8)
#Now check if the camera object is created successfully
if not camera.isOpened():
    print("The Camera is not Opened....Exiting")
    exit()

# creating a list of lables "You could add as many you want"
Labels = ["Ms. White", "Donald", "Tannilea", "Khalil", "Calaya", "Amishai", "Adrian", "Jordan", "Jaiden", "William"]
# Now create folders for each label to store images
for label in Labels:
    if not os.path.exists(os.path.join(rootfolder,label)):
        os.mkdir(os.path.join(rootfolder,label))

for folder in Labels:
    #using count variable to name the images in the dataset.
    count = 50
    #Taking input to start the capturing
    print("Select the Preview Window and press any key to start data collection for "+folder)
    #cv.namedWindow("Preview Window")
    #cjv.imshow("Preview Window", image)
    cv.waitKey(0)

    print("Got a key, starting to collect images")

    #cv.destroyWindow("Preview Window")s
    #clicking 200 images per label, you could change as you want.
    while count<150:
        print("Reading from camera")
        #read returns two values one is the exit code and other is the frame
        status, frame = camera.read()
        #check if we get the frame or not
        if not status:
            print("Frame is not been captured..Exiting...")
            break
        #convert the image into gray format for fast caculation
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #display window with gray image

        cv.imshow("Preview Window",gray)
        #resizing the image to store it
        gray = cv.resize(gray, (200,200))
        #Store the image to specific label folder
        filename= os.path.join(rootfolder,folder,'img'+str(count)+'.png')
        cv.imwrite(filename,gray)
        count=count+1
        print(cv.imwrite(filename, gray))
        #to quit the display window press 'q'
        #if cv.waitKey(1) == ord('q'):
        #    break
# When everything done, release the capture
camera.release()
cv.destroyAllWindows()
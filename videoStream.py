import cv2
import numpy as np

print "Courtesy:- OpenCV "+cv2.__version__
print "streaming live from Webcam 0"
print "Note:- press 'q' to stop streaming"

a = 0
cap = cv2.VideoCapture (0) # create a video object

# stream infinitely
while True:
    
    a = a + 1 # keep count of duration of streaming in ms
    check, video = cap.read () # create a frame object
    
    print (check)
    print (video)
    
    cv2.namedWindow ('Live Streaming', cv2.WINDOW_NORMAL) # create a resizable window
    cv2.imshow ('Live Streaming', video) # display the captured image(second argument) in the given window(first argument)
    
    #cv2.waitKey(0) # press any key to stop streaming
    
    key = cv2.waitKey (1) # display the frame for 1 ms
    
    if key == ord("q"): # check for keyboard input to stop streaming
        
        cap.release () # shutdown the camera
        cv2.destroyAllWindows () # close the window
        
        print ('\n\t%sms' % (a)) # print the duration of streaming
        
        break # exit from the infinite while loop

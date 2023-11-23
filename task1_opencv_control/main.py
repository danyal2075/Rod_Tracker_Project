from modules.opencv_controller import OpenCVController
import time
import cv2
import numpy as np
import base64
#
# Do NOT change this script
opencv_controller = OpenCVController()

#Iteration
for i in range(6):
    print("----------- Distance number: ", i)
    frame = opencv_controller.process_frame() #Calling to get the frame

    # Display in window
    jpg_as_np = np.frombuffer(frame, np.uint8) #Convert the frame from a byte buf to a NumPy array
    img = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB)
    #cv2.imshow('image', frame)  # Not in Raspberry Pi
    
    print("Current color from OpenCV: ", opencv_controller.get_current_color())
    print("---------------------------------")
    
    #cv2.waitKey(0) # Not in Raspberry Pi
    #cv2.destroyAllWindows() # Not in Raspberry Pi


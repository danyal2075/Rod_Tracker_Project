import logging
import threading
import cv2
import numpy as np
import imutils

USE_FAKE_PI_CAMERA = True # Chage to FALSE if testing in the Raspberry Pi

if USE_FAKE_PI_CAMERA:
    from .camera import Camera  # For running app
else:
    from .pi_camera import Camera  # For running Raspberry Pi

log = logging.getLogger(
    __name__)  # Creates a logger instance, we use it to log things out


class OpenCVController(object):

    def __init__(self):
        self.current_color = [False, False, False, False]
        self.camera = Camera()
        print('OpenCV controller initiated')

    def process_frame(self):  # generate frame by frame from camera
        while True:
            # Capture frame-by-frame
            frame = self.camera.get_frame()  # read the camera frame
            jpg_as_np = np.frombuffer(frame, np.uint8)
            frame = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, [640, 480])
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
        # Red
            lower_red1 = np.array([0, 50, 50])
            upper_red1 = np.array([10, 255, 255])
            lower_red2 = np.array([160, 50, 50])
            upper_red2 = np.array([180, 255, 255])
            red_mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
            red_mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
            red_mask = cv2.bitwise_or(red_mask1, red_mask2)

        # Light Blue
            lower_light_blue = np.array([90, 50, 70])
            upper_light_blue = np.array([128, 255, 255])
            light_blue_mask = cv2.inRange(hsv, lower_light_blue, upper_light_blue)

        # Purple
            lower_purple = np.array([129, 50, 70])
            upper_purple = np.array([158, 255, 255])
            purple_mask = cv2.inRange(hsv, lower_purple, upper_purple)

        # Yellow
            lower_yellow = np.array([25, 50, 70])
            upper_yellow = np.array([35, 255, 255])
            yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        
        # Green
            lower_green = np.array([36, 50, 70])
            upper_green = np.array([89, 255, 255])
            green_mask = cv2.inRange(hsv, lower_green, upper_green)

            kernal = np.ones((5, 5), "uint8")

        # Red mask
            red_mask = cv2.dilate(red_mask, kernal)

        # Light Blue mask
            light_blue_mask = cv2.dilate(light_blue_mask, kernal)

        # Purple mask
            purple_mask = cv2.dilate(purple_mask, kernal)

        # Yellow mask
            yellow_mask = cv2.dilate(yellow_mask, kernal)
        
        # Green mask
            green_mask = cv2.dilate(green_mask, kernal)
            
        # Initialize the variables before the if conditions
            l11 = (-1, -1)
            l12 = (-1, -1)
            l21 = (-1, -1)
            l22 = (-1, -1)
            l31 = (-1, -1)
            l32 = (-1, -1)
            l41 = (-1, -1)
            l42 = (-1, -1)
            l51 = (-1, -1)
            l52 = (-1, -1)
            
            contours = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)
            
            for contours in contours:
                area = cv2.contourArea(contours)
                if area > 5000:
                    xr, yr, wr, hr = cv2.boundingRect(contours)
                    imageFrame = cv2.rectangle(frame, (xr, yr), (xr + wr, yr + hr), (0, 0, 255), 3)  # colour of border
                    cv2.putText(imageFrame, "Mark", (xr, yr), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
                    l11 = (xr, yr)
                    l12 = (xr + wr, yr + hr)
                    break
                
            #Light Blue Mark Detection
            contours = cv2.findContours(light_blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)
            for contours in contours:
                area = cv2.contourArea(contours)
                if area > 5000:
                    xl, yl, wl, hl = cv2.boundingRect(contours)
                    imageFrame = cv2.rectangle(frame, (xl, yl), (xl + wl, yl + hl), (255, 255, 0), 3)  # colour of border
                    cv2.putText(imageFrame, "Light Blue", (xl, yl), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0))
                    l21 = (xl, yl)
                    l22 = (xl + wl, yl + hl)
                    break

            # Purple Mark Detection
            contours = cv2.findContours(purple_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)
            for contours in contours:
                area = cv2.contourArea(contours)
                if area > 5000:
                    xp, yp, wp, hp = cv2.boundingRect(contours)
                    imageFrame = cv2.rectangle(frame, (xp, yp), (xp + wp, yp + hp), (255, 0, 255), 3)  # colour of border
                    cv2.putText(imageFrame, "Purple", (xp, yp), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 255))
                    l31 = (xp, yp)
                    l32 = (xp + wp, yp + hp)
                    break

            # Yellow Mark Detection
            contours = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)
            for contours in contours:
                area = cv2.contourArea(contours)
                if area > 5000:
                    xy, yy, wy, hy = cv2.boundingRect(contours)
                    imageFrame = cv2.rectangle(frame, (xy, yy), (xy + wy, yy + hy), (0, 255, 255), 3)  # colour of border
                    cv2.putText(imageFrame, "Yellow", (xy, yy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                    l51 = (xy, yy)
                    l52 = (xy + wy, yy + hy)
                    break
                
        # Green Mark Detection
            contours = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)
            for contours in contours:
                area = cv2.contourArea(contours)
                if area > 5000:
                    xg, yg, wg, hg = cv2.boundingRect(contours)
                    imageFrame = cv2.rectangle(frame, (xg, yg), (xg + wg, yg + hg), (0, 255, 0), 3)  # colour of border
                    cv2.putText(imageFrame, "Green", (xg, yg), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
                    l41 = (xg, yg)
                    l42 = (xg + wg, yg + hg)
                    break
                
        # From Left side to Right side
            if ((l21[0] <= l11[0] < l22[0]) and (l21[0] <= l12[0] < l22[0])) or ((l11[0] < l21[0]) and (l12[0] < l22[0])):
                self.current_color = [True, False, False, False]  # Blue
                
            elif (l21[0] <= l11[0] < l22[0]) and (l31[0] <= l12[0] <= l32[0]):
                self.current_color = [True, True, False, False]  # Blue and Purple
                
            elif (l31[0] <= l11[0] < l32[0]) and (l31[0] <= l12[0] < l32[0]):
                self.current_color = [False, True, False, False]  # Purple
                
            elif (l31[0] <= l11[0] < l32[0]) and (l51[0] <= l12[0] <= l52[0]):
                self.current_color = [False, True, True, False]  # Purple and Yellow
                
            elif (l51[0] <= l11[0] < l52[0]) and (l51[0] <= l12[0] < l52[0]):
                self.current_color = [False, False, True, False]  # Yellow
                
            elif (l51[0] <= l11[0] <= l52[0]) and (l41[0] <= l12[0] <= l42[0]):
                self.current_color = [False, False, True, True]  #Yellow and Green
                
            elif (l41[0] <= l11[0] < l42[0]) and (l41[0] <= l12[0] <= l42[0]):
                self.current_color = [False, False, False, True]  # Green
                
        #From Right side to Left side 
                 
            if ((l41[0] >= l11[0] > l42[0]) and (l41[0] >= l12[0] > l42[0])): 
                self.current_color = [False, False, False, True]  # Green
                
            elif (l51[0] <= l11[0] <= l52[0]) and (l41[0] <= l12[0] <= l42[0]):
                self.current_color = [False, False, True, True]  #Yellow and Green
                
            elif (l51[0] <= l11[0] < l52[0]) and (l51[0] <= l12[0] < l52[0]):
                self.current_color = [False, False, True, False]  # Yellow
                
            elif (l31[0] <= l11[0] < l32[0]) and (l51[0] <= l12[0] <= l52[0]):
                self.current_color = [False, True, True, False]  # Purple and Yellow
                
            elif (l31[0] <= l11[0] < l32[0]) and (l31[0] <= l12[0] < l32[0]):
                self.current_color = [False, True, False, False]  # Purple
                
            elif (l21[0] <= l11[0] < l22[0]) and (l31[0] <= l12[0] <= l32[0]):
                self.current_color = [True, True, False, False]  # Blue and Purple
                
            elif (l21[0] <= l11[0] < l22[0]) and (l21[0] <= l12[0] < l22[0]):
                self.current_color = [True, False, False, False]  # Blue
                
                ret, buffer = cv2.imencode(".jpg", frame)
                frame = buffer.tobytes()
                #print("Monitoring")
            
            return frame


    def get_current_color(self):
        return self.current_color

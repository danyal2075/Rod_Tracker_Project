# For Final Submission
USE_FAKE_GPIO = True #Chage to FALSE if testing in the Raspberry Pi

if USE_FAKE_GPIO:
    from .fake_gpio import GPIO  # For running app
else:
    import RPi.GPIO as GPIO  # For testing in Raspberry Pi

import time
import statistics
import random

class SensorController:

    def __init__(self):
        self.PIN_TRIGGER = 18  # do not change
        self.PIN_ECHO = 24  # do not change
        self.distance = None
        self.color_from_distance = [False, False, False, False]
        print('Sensor controller initiated')

    def track_rod(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)   # Setup trigger pin as output to start the sensor
        GPIO.setup(self.PIN_ECHO, GPIO.IN)       # Set echo pin to receive input
        GPIO.output(self.PIN_TRIGGER, False)     # Set trigger pin to low to let the sensor settle
        print ('Monitoring')
        #time.sleep(0.1)

        values = []
        for i in range(10):
            start = time.time()
            end = time.time()

            GPIO.output(self.PIN_TRIGGER, True)      # Set pin trigger to high to allow sensor to trigger
            time.sleep(0.00001)                      # Wait 10 micro second
            GPIO.output(self.PIN_TRIGGER, False)

            while GPIO.input(self.PIN_ECHO) == 0:    # Wait till ECHO is Low (start time)
                start = time.time()
            
            while GPIO.input(self.PIN_ECHO) == 1:    # Wait till ECHO is High (end time)
                end = time.time()

            duration = end - start
            dis = round(duration*17150, 2)  #rough speed of ultrasonic sound is 34300 cm/s.   34300/2 = 17150 cm/s.
            values.append(dis)         # Add distance to list
        print(values)
        self.distance = statistics.median(values)  #taking median
        print(self.distance)
        return self.distance
    
    def get_distance(self):
        return self.distance
    
    def get_color_from_distance(self):
        #self.distance = 13
        if(self.distance >= 4 and self.distance <= 8.4):
            self.color_from_distance = [False, False, False, True]
            #print('Green Color Zone')
            return self.color_from_distance

        elif(self.distance >= 7 and self.distance <= 9.5):
            self.color_from_distance = [False, False, True, True]
            #print('Green Color and Yellow Color Zone')
            return self.color_from_distance

        elif(self.distance >= 8.5 and self.distance <= 13):
            self.color_from_distance = [False, False, True, False]
            #print('Yellow Color Zone')
            return self.color_from_distance

        elif(self.distance >= 12 and self.distance <= 14.5):
            self.color_from_distance = [False, True, True, False]
            #print('Yellow Color and Purple Color Zone')
            return self.color_from_distance
            
        elif(self.distance >= 14 and self.distance <= 16.5):
            self.color_from_distance = [False, True, False, False]
            #print('purple Color Zone')
            return self.color_from_distance

        elif(self.distance >= 17 and self.distance <= 19.5):
            self.color_from_distance = [True, True, False, False]
            #print('purple Color and blue color Zone')
            return self.color_from_distance
            
        elif(self.distance >= 18 and self.distance <= 22):
            self.color_from_distance = [True, False, False, False]
            #print('Blue Color Zone')
            return self.color_from_distance

        elif(self.distance < 4 or self.distance > 22):
            self.color_from_distance = [False,False,False, False]
            print('Outside of Color Zone')
            return self.color_from_distance
            
        else:
            return self.color_from_distance

# END
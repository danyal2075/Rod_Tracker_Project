import time
import random


USE_FAKE_GPIO = True #Chage to False if testing in the Raspberry Pi

if USE_FAKE_GPIO:
    from .fake_gpio import GPIO  # For running app
else:
    import RPi.GPIO as GPIO  # For testing in Raspberry Pi


# import ...

class MotorController(object):

    def __init__(self):
        self.working = False
        self.stopMotor = False
        self.status = 'Stopped'

    def start_motor(self):
        self.PIN_STEP = 25  # do not change
        self.PIN_DIR = 8  # do not change
        self.working = True
        # ...
        print('Motor started')
        CW = 0  # Clockwise Rotation
        CCW = 1  # Counterclockwise Rotation
        z=0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_DIR, GPIO.OUT)
        GPIO.setup(self.PIN_STEP, GPIO.OUT)

        rand = random.randint(0, 1)
        if rand == 0:
            step_count =2000
            print("The motor is rotating 180 degrees clockwise")
            print(step_count)

        else:
            step_count = 4000
            print("The motor is rotating 360 degrees anticlockwise")

        delay = .0625  # 1/1600

        y = random.randint(CW, CCW)
        if y == 0:

            self.status = str(self.working)+' and '+'Clockwise!\n'
            print(step_count)
            #print("Motor Status: " + str(self.working))
            GPIO.output(self.PIN_DIR, CW)
            for z in range(step_count):
                if not self.stopMotor:
                    GPIO.output(self.PIN_STEP, GPIO.HIGH)
                    time.sleep(delay)
                    GPIO.output(self.PIN_STEP, GPIO.LOW)
                    time.sleep(delay)
                    print("Motor Working:Clockwise & 180\n")
                    print(step_count)
                    #print(self.status)
                    # if (z == 7999):
                    #     print(z)
                else:
                    self.working = False
                    self.status = 'Stopped\n'

                    print("Motor Status: " + str(self.working)+ "Clockwise")
                    break

        elif y == 1:
            self.status = str(self.working)+' and '+'Anticlockwise!\n'
            print(step_count)
            #print("Motor Status: " + str(self.working))
            GPIO.output(self.PIN_DIR, CCW)
            for z in range(step_count):
                if not self.stopMotor:
                    GPIO.output(self.PIN_STEP, GPIO.HIGH)
                    time.sleep(delay)
                    GPIO.output(self.PIN_STEP, GPIO.LOW)
                    time.sleep(delay)
                    print("Motor Working:Anticlockwise\n")
                    print(step_count)
                    print(self.status)
                    # if (z == 7999):
                    #     print(z)
                else:

                    self.working = False
                    self.status = 'Stopped\n'
                    print("Motor Status: " + str(self.working))

                    break

        else:
            print("The motor stopped working/n")
            self.status = 'stopped!/n'
            self.working = False
            print("Motor Status: " + str(self.working))


    GPIO.cleanup()

    print("Motor_running")
    #return "Motor Running"

    def stop_motor(self):
     self.working = False
     self.status = 'Motor Stopped'


    def is_working(self):
        return self.working

    def m_status(self):
        return self.status


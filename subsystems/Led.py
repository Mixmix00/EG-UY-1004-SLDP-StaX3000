import RPi.GPIO as GPIO
import time

RED_PIN = 12
GREEN_PIN = 19
BLUE_PIN = 13

def setup():
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(RED_PIN, GPIO.OUT)
    GPIO.setup(GREEN_PIN, GPIO.OUT)
    GPIO.setup(BLUE_PIN, GPIO.OUT)

# Light Blue
# Values are inverted (HIGH becomes LOW etc)
# Think of LOW as 0 and HIGH as 255
def signalStartingRobot():
    GPIO.output(GREEN_PIN, GPIO.HIGH)
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)

def signalRobotUnloading():
    chan_list = (GREEN_PIN,BLUE_PIN)
    GPIO.output(chan_list, GPIO.LOW)
    GPIO.output(RED_PIN,GPIO.HIGH)

def signalRobotOnAndNotEnabled():
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.HIGH)
    GPIO.output(BLUE_PIN, GPIO.HIGH)

def signalDrivingToBox():
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)


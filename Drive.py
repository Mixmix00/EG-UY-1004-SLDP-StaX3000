#!/usr/bin/python
import PiMotor
import time
import RPi.GPIO as GPIO
import math

#Name of Individual MOTORS 
fl = PiMotor.Motor("MOTOR1",1)
fr = PiMotor.Motor("MOTOR2",1)
bl = PiMotor.Motor("MOTOR3",1)
br = PiMotor.Motor("MOTOR4",1)

#To drive all motors together
flBr = PiMotor.LinkedMotors(fl, br)
frBl = PiMotor.linkedMotors(fr, bl)

#Names for Individual Arrows
ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3) 
ar = PiMotor.Arrow(4)

def setDriveMotors(radians, speed):
    frontLeftBackRight = math.sin(radians + (math.pi/4)) * speed
    frontRightBackLeft = math.sin(radians - (math.pi/4)) * speed

    if frontLeftBackRight > 0:
        flBr.forward(frontLeftBackRight)
    elif frontLeftBackRight < 0:
        flBr.reverse(frontLeftBackRight)
    else:
        flBr.stop()
    
    if frontRightBackLeft > 0:
        frBl.forward(frontRightBackLeft)
    elif frontRightBackLeft < 0:
        frBl.reverse(frontRightBackLeft)
    else:
        frBl.stop()
    
def stopAllMotors():
    flBr.stop()
    frBl.stop()

##This segment drives the motors in the direction listed below:
## forward and reverse takes speed in percentage(0-100)

try:
    ab.on()
    al.on()
    af.on()
    ar.on()
    while True:
        setDriveMotors(0)
        time.sleep(5)
        setDriveMotors(math.pi/2)
        time.sleep(5)
        setDriveMotors(math.pi)
        time.sleep(5)
        setDriveMotors(3*math.pi/2)
        time.sleep(5)
        stopAllMotors()
        
except KeyboardInterrupt:
    ab.off()
    al.off()
    af.off()
    ar.off()
    GPIO.cleanup()

    

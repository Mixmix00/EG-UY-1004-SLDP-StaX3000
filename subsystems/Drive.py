#!/usr/bin/python
import MotorShield.PiMotor as PiMotor
import time
import RPi.GPIO as GPIO
import math

#To drive all motors together
flBr = PiMotor.Motor("MOTOR4",1)
frBl = PiMotor.Motor("MOTOR3",1)

#Names for Individual Arrows
#ab = PiMotor.Arrow(1)
#al = PiMotor.Arrow(2)
#af = PiMotor.Arrow(3) 
#ar = PiMotor.Arrow(4)

def CONCURRENT_setDriveMotors(radians, speed):
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

def CONCURRENT_spinClockwise():
    #fl.forward(100)
    #bl.forward(100)
    #fr.reverse(100)
    #br.reverse(100)
    raise Exception("Unimplemented")

def CONCURRENT_spinCounterClockwise():
    #fl.reverse(100)
    #bl.reverse(100)
    #fr.forward(100)
    #br.forward(100)
    raise Exception("Unimplemented")

    
def CONCURRENT_stopAllMotors():
    flBr.stop()
    frBl.stop()


def CONCURRENT_driveStraight():
    CONCURRENT_setDriveMotors(math.pi/2)

def CONCURRENT_driveBackwards():
    CONCURRENT_setDriveMotors(3 * math.pi/2)

def CONCURRENT_driveDiagonalForwardRight():
    CONCURRENT_setDriveMotors(math.pi/4)

def CONCURRENT_driveDiagonalForwardLeft():
    CONCURRENT_setDriveMotors(3 * math.pi/4)

def PROC_driveSquare():
    #ab.on()
    #al.on()
    #af.on()
    #ar.on()
        
    CONCURRENT_setDriveMotors(0)
    time.sleep(5)
    CONCURRENT_setDriveMotors(math.pi/2)
    time.sleep(5)
    CONCURRENT_setDriveMotors(math.pi)
    time.sleep(5)
    CONCURRENT_setDriveMotors(3*math.pi/2)
    time.sleep(5)
    CONCURRENT_stopAllMotors()
            
    
    frBl.off()
    flBr.off()

    

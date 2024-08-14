#!/usr/bin/python
import MotorSheild.PiMotor as PiMotor
import time
import RPi.GPIO as GPIO
import math

#Motors as they are connected to the motor board
flBr = PiMotor.Motor("MOTOR4",1)
frBl = PiMotor.Motor("MOTOR3",1)

''' 
Method to set power to the drive motor
@param radians: The angle in radians to set the motors to
@param speed: The speed to set the motors to (0.00-100.00)
    @return: None
    @throws: None
    @author: Max Spier, 2024
    '''
def CONCURRENT_setDriveMotors(radians, speed):
    # Find the speed of the motors based on the angle by using the formula and multiply it by the speed
    frontLeftBackRight = math.sin(radians + (math.pi/4)) * speed
    frontRightBackLeft = math.sin(radians - (math.pi/4)) * speed

    # Set the motors to the speed using the library
    # If the motors should have no power, stop them
    if frontLeftBackRight > 0:
        flBr.forward(frontLeftBackRight)
    elif frontLeftBackRight < 0:
        flBr.reverse(-frontLeftBackRight)
    else:
        flBr.stop()
    
    if frontRightBackLeft > 0:
        frBl.forward(frontRightBackLeft)
    elif frontRightBackLeft < 0:
        frBl.reverse(-frontRightBackLeft)
    else:
        frBl.stop()


'''
Method to stop all motors
@return: None
@throws: None
@author: Max Spier, 2024
'''
def CONCURRENT_stopAllMotors():
    flBr.stop()
    frBl.stop()

'''
Method to set the drive motors to drive straight
@return: None
@throws: None
@author: Max Spier, 2024
'''
def CONCURRENT_driveStraight():
    CONCURRENT_setDriveMotors(math.pi/2,100)

'''
Method to set the drive motors to drive backwards
@return: None
@throws: None
@author: Max Spier, 2024
'''
def CONCURRENT_driveBackwards():
    CONCURRENT_setDriveMotors(3 * math.pi/2,100)

'''
Method to set the drive motors to drive diagonal up (where the slope of the line would be 1)
@return: None
@throws: None
@author: Max Spier, 2024
'''
def CONCURRENT_driveDiagonalForwardRight():
    CONCURRENT_setDriveMotors(math.pi/4,100)

'''
Method to set the drive motors to drive diagonal up (where the slope of the line would be -1)
@return: None
@throws: None
@author: Max Spier, 2024
'''
def CONCURRENT_driveDiagonalForwardLeft():
    CONCURRENT_setDriveMotors(3 * math.pi/4,100)
'''
Method to set the drive motors to drive diagonal down (where the slope of the line would be -1)
@return: None
@throws: None
@author: Max Spier, 2024
'''
def CONCURRENT_driveDiagonalBackwardsRight():
    CONCURRENT_setDriveMotors(7 * math.pi/4,100)

def CONCURRENT_M3():
    frBl.forward(100)

def CONCURRENT_M4():
    flBr.forward(100)

    

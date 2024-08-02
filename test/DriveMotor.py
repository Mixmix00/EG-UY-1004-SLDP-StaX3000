import MotorSheild.PiMotor as PiMotor
import time
import RPi.GPIO as GPIO
import math

testMotor = PiMotor.Motor("MOTOR1",1)

def forward():
    testMotor.forward(100)

def backward():
    testMotor.reverse(100)

forward()
time.sleep(10)
backward()
time.sleep(10)
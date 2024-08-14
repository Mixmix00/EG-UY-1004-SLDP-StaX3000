import subsystems.Drive as Drive
import time
import math

def run():
    Drive.CONCURRENT_driveStraight()
    time.sleep(5)
    Drive.CONCURRENT_setDriveMotors(0,100)
    time.sleep(5)
    Drive.CONCURRENT_driveBackwards()
    time.sleep(5)
    Drive.CONCURRENT_setDriveMotors(math.pi,100)
    time.sleep(5)
    Drive.CONCURRENT_stopAllMotors()

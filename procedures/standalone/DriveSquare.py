import subsystems.Drive as Drive
import time
import math

def run():
    Drive.CONCURRENT_driveStraight()
    time.sleep(5)
    Drive.CONCURRENT_setDriveMotors(0)
    time.sleep(5)
    Drive.CONCURRENT_driveBackwards()
    time.sleep(5)
    Drive.CONCURRENT_setDriveMotors(math.pi)
    time.sleep(5)
    Drive.CONCURRENT_stopAllMotors()
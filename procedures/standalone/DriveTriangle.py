import subsystems.Drive as Drive
import time
import math

def run():
    Drive.CONCURRENT_driveStraight()
    time.sleep(4)
    Drive.CONCURRENT_driveDiagonalBackwardsRight()
    time.sleep(5)
    Drive.CONCURRENT_setDriveMotors(math.pi)
    time.sleep(3)
    Drive.CONCURRENT_stopAllMotors()

import time
from adafruit_motorkit import MotorKit

kit = MotorKit()

for i in range(100):
    kit.stepper1.onestep()
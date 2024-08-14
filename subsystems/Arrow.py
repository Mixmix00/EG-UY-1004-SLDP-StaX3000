import MotorSheild.PiMotor as PiMotor
import time

a1 = PiMotor.Arrow(1)
a2 = PiMotor.Arrow(2)
a3 = PiMotor.Arrow(3)
a4 = PiMotor.Arrow(4)

def signalRobotStopped():
    a1.on()
    a2.on()
    a3.on()
    a4.on()

def signalRobotEnabled():
    a1.on()
    a2.on()
    a3.off()
    a4.off()

def signalRobotLoggedIn():
    a1.on()
    a2.off()
    a3.off()
    a4.off()

def PROC_signalRobotFailedAttempt():
    for i in range(5):
        a1.on()
        a2.on()
        a3.on()
        a4.on()
        time.sleep(0.1)
        a1.off()
        a2.off()
        a3.off()
        a4.off()
        time.sleep(0.05)
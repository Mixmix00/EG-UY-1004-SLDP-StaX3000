import MotorSheild.PiMotor as PiMotor

ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3) 
ar = PiMotor.Arrow(4)

def turnArrow1On():
    ab.on()

def turnArrow2On():
    al.on()

def turnArrow3On():
    af.on()

def turnArrow4On():
    ar.on()

def turnArrow1Off():
    ab.off()

def turnArrow2Off():
    al.off()

def turnArrow3Off():
    af.off()

def turnArrow4Off():
    ar.off()

def turnAllArrowsOff():
    ab.off()
    al.off()
    af.off()
    ar.off()

def turnAllArrowsOn():
    ab.on()
    al.on()
    af.on()
    ar.on()
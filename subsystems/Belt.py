import RPI.GPIO as GPIO

in1=12
in2=26
en_a=21

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en_a,GPIO.OUT)

power_a= GPIO.PWM(en_a,100)
power_a.start(90)

GPIO.output(in1,GPI0.LOW)
GPIO.output(in2,GPI0.LOW)
def forward():
    GPIO.output(in1,GPI0.HIGH)
    GPIO.output(in2,GPI0.LOW)   
    
def backward():
    GPIO.output(in1,GPI0.LOW)
    GPIO.output(in2,GPI0.HIGH) 

def stop():
    GPIO.cleanup()
        
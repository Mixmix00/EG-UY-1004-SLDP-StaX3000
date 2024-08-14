import RPI.GPIO as GPIO

in1=
in2=
en_a=

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en_a,GPIO.OUT)

power_a= GPIO.PWM(en_a,100)
power_a.start(90)

GPIO.output(in1,GPI0.LOW)
GPIO.output(in2,GPI0.LOW)

while(True):
    user_input=input()
    if user_input == "f":
        GPIO.output(in1,GPI0.HIGH)
        GPIO.output(in2,GPI0.LOW)   
    
    elif user_input == "b":
        GPIO.output(in1,GPI0.LOW)
        GPIO.output(in2,GPI0.HIGH) 

    elif user_input== "s":
        GPIO.cleanup()
        break
        
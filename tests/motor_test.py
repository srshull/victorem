# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
L_dir = 17 # Broadcom pin 18 (P1 pin 12)
R_dir = 27 # Broadcom pin 18 (P1 pin 12)
L_spd = 18 # Broadcom pin 18 (P1 pin 12)
R_spd = 13 # Broadcom pin 18 (P1 pin 12)


# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(L_dir, GPIO.OUT) # LED pin set as output
GPIO.setup(R_dir, GPIO.OUT) # LED pin set as output
GPIO.setup(L_spd, GPIO.OUT) # PWM pin set as output
GPIO.setup(R_spd, GPIO.OUT) # PWM pin set as output
L_pwm = GPIO.PWM(L_spd, 5000)  # Initialize PWM on pwmPin 100Hz frequency
R_pwm = GPIO.PWM(R_spd, 5000)  # Initialize PWM on pwmPin 100Hz frequency


# Initial state for LEDs:
GPIO.output(L_dir, GPIO.LOW)
GPIO.output(R_dir, GPIO.LOW)


L_pwm.start(100)
R_pwm.start(100)


print("Here we go! Press CTRL+C to exit")
try:
    while 1:
            #GPIO.output(L_dir, GPIO.HIGH)
            GPIO.output(L_dir, GPIO.HIGH)
            GPIO.output(R_dir, GPIO.HIGH)
            R_pwm.ChangeDutyCycle(100)
            L_pwm.ChangeDutyCycle(100)
            time.sleep(1.75)
            GPIO.output(L_dir, GPIO.HIGH)
            GPIO.output(R_dir, GPIO.LOW)
            R_pwm.ChangeDutyCycle(30)
            L_pwm.ChangeDutyCycle(30)
            time.sleep(.68)
            GPIO.output(L_dir, GPIO.HIGH)
            GPIO.output(R_dir, GPIO.HIGH)
            R_pwm.ChangeDutyCycle(100)
            L_pwm.ChangeDutyCycle(100)
            time.sleep(2.3)
            GPIO.output(L_dir, GPIO.LOW)
            GPIO.output(R_dir, GPIO.HIGH)
            R_pwm.ChangeDutyCycle(30)
            L_pwm.ChangeDutyCycle(30)
            time.sleep(.5)
            GPIO.output(L_dir, GPIO.LOW)
            GPIO.output(R_dir, GPIO.LOW)
            R_pwm.ChangeDutyCycle(100)
            L_pwm.ChangeDutyCycle(100)
            time.sleep(5)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO

# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
Pin = 18 # Broadcom pin 18 (P1 pin 12)



# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(Pin, GPIO.OUT) # LED pin set as output


# Initial state for LEDs:
GPIO.output(Pin, GPIO.LOW)


print("Here we go! Press CTRL+C to exit")
try:
    while 1:
            GPIO.output(Pin, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(Pin, GPIO.LOW)
            time.sleep(2)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO

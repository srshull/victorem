# External module imports
import RPi.GPIO as GPIO
import time
import pygame


pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

print 'Initialized Joystick : %s' % j.get_name()

# Pin Definitons:
L_dir = 17 # Broadcom pin 18 (P1 pin 12)
R_dir = 27 # Broadcom pin 18 (P1 pin 12)
L_spd = 18 # Broadcom pin 18 (P1 pin 12)
R_spd = 13 # Broadcom pin 18 (P1 pin 12)

rs = 75
rd = True
ls = 75
ld = True




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


L_pwm.start(0)
R_pwm.start(0)

threshold = 0.1
RightTrack = 0
LeftTrack = 0

def setmotors(rs,ls):
        GPIO.output(R_dir, rd)
        GPIO.output(L_dir, ld)
        if rs > 100.0:
            rs = 100
        if ls > 100.0:
            ls=100
        R_pwm.ChangeDutyCycle(rs)
        L_pwm.ChangeDutyCycle(ls)

print("Here we go! Press CTRL+C to exit")
try:
    # Turn on the motors
    #GPIO.output(MotorAE, True)
    #GPIO.output(MotorBE, True)

    # This is the main loop
    while True:

        # Check for any queued events and then process each one
        events = pygame.event.get()
        for event in events:
          UpdateMotors = 0

          # Check if one of the joysticks has moved
          if event.type == pygame.JOYAXISMOTION:
            if event.axis == 1:
              LeftTrack = event.value
              UpdateMotors = 1
            elif event.axis == 3:
              RightTrack = event.value
              UpdateMotors = 1

            # Check if we need to update what the motors are doing
            if UpdateMotors:

              # Check how to configure the left motor

              # Move forwards
              if (RightTrack > threshold):
                  rd = True
                  rs = RightTrack * 100
              # Move backwards
              elif (RightTrack < -threshold):
                  rd = False
                  rs = RightTrack * -100
              # Stopping
              else:
                  rs = 0    

              # And do the same for the right motor
              if (LeftTrack > threshold):
                  ld = True
                  ls = LeftTrack * 100
              # Move backwards
              elif (LeftTrack < -threshold):
                  ld = False
                  ls = LeftTrack * -100
              # Otherwise stop
              else:
                  ls = 0

              # Now we've worked out what is going on we can tell the
              # motors what they need to do
              setmotors(rs,ls)


except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    R_pwm.ChangeDutyCycle(0)
    L_pwm.ChangeDutyCycle(0)
    GPIO.cleanup() # cleanup all GPIO



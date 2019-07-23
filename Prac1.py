#!/usr/bin/python3
"""
Names: Niceta Nduku
Student Number: NDKNIC001
Prac: Prac 1
Date: 23/07/2019
"""

import RPi.GPIO as GPIO
import time
LED_List = (5,6,12) #LED channels
on_button = 18 #on button
off_button = 17 #off button

def main():
	if GPIO.input(on_button)== GPIO.HIGH:
		print ("on button pressed")
		GPIO.output(LED_List,GPIO.HIGH)
		print ("LED on")
	if GPIO.input(off_button)==GPIO.HIGH:
		print("off button pressed")
		GPIO.output(LED_List,GPIO.LOW)
		print("LED off")
def init_GPIO():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup([off_button,on_button],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(LED_List,GPIO.OUT, initial=GPIO.LOW)

init_GPIO()

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)

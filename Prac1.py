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
button_List = (17,18) #button channels

def main():
	GPIO.output(LED_List,GPIO.HIGH)
	print ("LED on")
	time.sleep(1)
	GPIO.output(LED_List,GPIO.LOW)
	print ("LED off")
	time.sleep(1)

def init_GPIO():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	#GPIO.setup(button_list,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(LED_List,GPIO.OUT)

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

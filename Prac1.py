#!/usr/bin/python3
"""
Names: Niceta Nduku
Student Number: NDKNIC001
Prac: Prac 1
Date: 23/07/2019
"""

import RPi.GPIO as GPIO

LED_list = (5,6,12) #LED channels
button_List = (17,18) #button channels

def main():
	init_GPIO()
	GPIO.output(5,GPIO.HIGH)
	GPIO.cleanup()

def init_GPIO():
	GPIO.setmode(GPIO.BCM)
	#GPIO.setup(button_list,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(LED_list,GPIO.OUT,initial=GPIO.LOW)


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

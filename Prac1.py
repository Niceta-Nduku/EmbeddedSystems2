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

def init_GPIO():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup([off_button,on_button],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(LED_List,GPIO.OUT, initial=GPIO.LOW)

	GPIO.add_event_detect(on_button, GPIO.RISING, callback=on_callback,bouncetime=300)
	GPIO.add_event_detect(off_button, GPIO.RISING, callback=off_callback, bouncetime=300)

def on_callback(channel):
	GPIO.output(LED_List,GPIO.HIGH)
	print ("LED on")

def off_callback(channel):
	GPIO.output(LED_List,GPIO.LOW)
	print ("LED off")

def main():
	time.sleep(3)

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    init_GPIO()

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

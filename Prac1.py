#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Niceta Nduku
Student Number: NDKNIC001
Prac: Prac 1
Date: 23/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
LED_list = (5,6,12)
button_List = (17,18)
# Logic that you write
def main():
	init_GPIO()
	GPIO.output(5,GPIO.HIGH)

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

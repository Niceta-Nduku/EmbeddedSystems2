#!/usr/bin/python3
"""
Names: Niceta Nduku
Student Number: NDKNIC001
Prac: Prac 1
Date: 23/07/2019
"""

import RPi.GPIO as GPIO
import time
from itertools import product

lsb=5 #least significant bit
msb =  12 #most significant bit
sec_bit =  6 #middle digit

up_button = 18 #button to count down
down_button = 17 #button to count down
binary_digits = list(product(range(2),repeat=3)) #binary values from 000 to 1
current = 0 #the iterator that will determine what the current nuber is

def init_GPIO():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup([down_button,up_button],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup((msb,sec_bit,lsb),GPIO.OUT, initial= 0)

	GPIO.add_event_detect(up_button, GPIO.RISING, callback=count_up,bouncetime=300)
	GPIO.add_event_detect(down_button, GPIO.RISING, callback=count_down, bouncetime=300)

def count_up(channel):
	global current
	print("Counting up")
	while True:
		if current==8:
			current=0
		time.sleep(1)
		GPIO.output((msb,sec_bit,lsb),binary_digits[current])
		print(binary_digits[current])
		current+=1

def count_down(channel):
	global current
	print("Counting down")
	while True:
		if current==-1:
			current=7
		time.sleep(1)
		GPIO.output((msb,sec_bit,lsb),binary_digits[current])
		print(binary_digits[current])
		current-=1

def main():
	time.sleep(1)

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

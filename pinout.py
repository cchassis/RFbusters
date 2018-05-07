#!/usr/bin/python

import sys
import mraa
import time

# Use pin 7 by default
pin_no = 16
#pin_no = 18

# Export the GPIO pin for use
pin = mraa.Gpio(pin_no)

# Small delay to allow udev rules to execute (necessary only on up)
time.sleep(0.1)

# Configure the pin direction
pin.dir(mraa.DIR_OUT)

# Loop
while True:
    # Turn the LED on and wait for 0.5 seconds
    pin.write(1)
    time.sleep(2)
    # Turn the LED off and wait for 0.5 seconds
    pin.write(0)
    time.sleep(2)

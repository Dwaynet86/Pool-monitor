#!/usr/bin/env python

#Written by Dwayne Truex June 2019
#Written for PiZeroW
#Contact: dwaynetruex@yahoo.com

# This program was designed to control multiple relays
# and read multiple inputs



#import needed modules

import RPi.GPIO as GPIO #  Import GPIO Module
from time import sleep # Import sleep Module for timing

# Setup GPIO Pins 

GPIO.setmode(GPIO.BCM)  # Configures how we are describing our pin numbering
GPIO.setwarnings(False)  # Disable Warnings




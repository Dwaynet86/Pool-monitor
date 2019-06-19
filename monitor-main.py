#!/usr/bin/env python

#Written by Dwayne Truex June 2019
#Written for PiZeroW
#Contact: dwaynetruex@yahoo.com

# This program was designed to control multiple relays
# and read multiple inputs for the purpose of 
# monitoring and controlling swimming pool water parameters



#import needed modules
from config import *
from sensors import *
from relays import *
from database import *
import RPi.GPIO as GPIO #  Import GPIO Module
import pymysql
from time import sleep # Import sleep Module for timing

# Setup GPIO Pins 

GPIO.setmode(GPIO.BCM)  # Configures how we are describing our pin numbering
GPIO.setwarnings(False)  # Disable Warnings



# Main Program

# First run create database and tables
create_database() 
#create_relay_table()
create_settings_table()
#create_sensors_table()


print("main loop")

#Main Loop
while True: # Loop Continuously
    
    #sensors() #pull sensor data then react if needed
    #relays() #de/activate relays based on sensors
    print("loop")
    sleep(10)
    

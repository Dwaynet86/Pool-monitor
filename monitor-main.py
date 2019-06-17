#!/usr/bin/env python

#Written by Dwayne Truex June 2019
#Written for PiZeroW
#Contact: dwaynetruex@yahoo.com

# This program was designed to control multiple relays
# and read multiple inputs



#import needed modules
import configuration as cfg
import RPi.GPIO as GPIO #  Import GPIO Module
from time import sleep # Import sleep Module for timing

# Setup GPIO Pins 

GPIO.setmode(GPIO.BCM)  # Configures how we are describing our pin numbering
GPIO.setwarnings(False)  # Disable Warnings


def create_database():

    conn = mysql.connect(localhost, poolmon, poolmon)
    curs = conn.cursor()
    curs.execute("SET sql_notes = 0; ")  # Hide Warnings

    curs.execute("CREATE DATABASE IF NOT EXISTS {}".format(dbname))

    curs.execute("SET sql_notes = 1; ")  # Show Warnings
    conn.commit()
    conn.close()
    return


# Main Program

# First run create database and tables
create_database()
create_relay_table()
create_settings_table()
create_sensors_table()



#Main Loop
while True: # Loop Continuously
    #relays()
    sleep(1)
    

#!/usr/bin/env python

#Written by Dwayne Truex June 2019
#Written for PiZeroW
#Contact: dwaynetruex@yahoo.com

# This program was designed to control multiple relays
# and read multiple inputs for the purpose of 
# monitoring and controlling swimming pool water parameters



#import needed modules
import config as cfg
import RPi.GPIO as GPIO #  Import GPIO Module
import pymysql
from time import sleep # Import sleep Module for timing

# Setup GPIO Pins 

GPIO.setmode(GPIO.BCM)  # Configures how we are describing our pin numbering
GPIO.setwarnings(False)  # Disable Warnings


def create_database():
    print("connecting to server %s using user %s and password %s") % (cfg.servername, cfg.username, cfg.password)
    conn = pymysql.connect(cfg.servername, cfg.username, cfg.password, cfg.dbname)
    print("connection made")
    curs = conn.cursor()
    print("curs done")
    curs.execute("SET sql_notes = 0; ")  # Hide Warnings
    print("creating db ", cfg.dbname)
    curs.execute("CREATE DATABASE IF NOT EXISTS {}".format(cfg.dbname))
    
    curs.execute("SET sql_notes = 1; ")  # Show Warnings
    conn.commit()
    conn.close()
    return




# Main Program

# First run create database and tables
create_database()
#create_relay_table()
#create_settings_table()
#create_sensors_table()


print("hello.. this is the end")
#Main Loop
#while True: # Loop Continuously
    #relays()
 #   sleep(1)
    

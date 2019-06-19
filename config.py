#configuration settings

#Define what sensors are connected, there names, and there type
# Define MySQL database login settings

servername = "localhost"
username = "poolmonitor"
password = "poolmon!"
dbname = "pool_monitor"

# Define Relay Settings

outputpins = [22, 23, 24, 25]  # Specifiy a RPi GPIO Pin for each relay
numdtpairs = [4, 3, 2, 1]  # Number of Start/Stop pairs for each relay
relaycount = list(range(1, (len(outputpins) + 1)))

# Define other alert settings

misc_setting = {"offset_percent": 2,  # Stop toggling when close to alert value
                "pause_readings": False,
                "email_reset_delay": 172800,  # 60x60x24x2 = 2 Days
                "read_sensor_delay": 290,  # 60x5 = 5 Minutes
                "pause_reset_delay": 1800,  # 60x30 = 30 Minutes
                "to_email": "dwaynetruex@yahoo.com"}

# Define other settings

# number of seconds between sensor readings
time_between_readings = misc_setting["read_sensor_delay"]
main_pump_relay = outputpins[0]  # Stops email alert check if the pump is "off"
alert_check = False
loops = 0  # Set starting loops count for timing relay and sensor readings
email_sent = False
email_sent_reset = 0
pause_loops = 0

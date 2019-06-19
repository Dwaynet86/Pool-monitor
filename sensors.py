# Add sensor information here


sensors = OrderedDict([("temperature", {  # DS18B20 Temperature Sensor
                            "sensor_type": "1_wire_temp",
                            "name": "ds18b20_temp",
                            "is_connected": True,
                            "is_ref": False,
                            "ds18b20_file":
                            "/sys/bus/w1/devices/28-xxxxxxxxxxxx/w1_slave",
                            "accuracy": 1,
                            "test_for_alert": False,
                            "upper_alert_name": "temp_hi",
                            "upper_alert_value": 50,
                            "lower_alert_name": "temp_low",
                            "lower_alert_value": 10}),

                       ("EC", {  # EC Sensor
                            "sensor_type": "atlas_scientific_ec",
                            "name": "ec",
                            "is_connected": True,
                            "is_ref": False,
                            "i2c": 100,
                            "accuracy": 0,
                            "ppm_multiplier": 0.67,  # Convert EC to PPM
                            "test_for_alert": True,
                            "upper_alert_name": "ec_hi",
                            "upper_alert_value": 6000,
                            "lower_alert_name": "ec_low",
                            "lower_alert_value": 4500}),

                       ("ph", {  # pH Sensor
                            "sensor_type": "atlas_scientific",
                            "name": "ph",
                            "is_connected": True,
                            "is_ref": False,
                            "i2c": 99,
                            "accuracy": 2,
                            "test_for_alert": True,
                            "upper_alert_name": "ph_hi",
                            "upper_alert_value": 7.4,
                            "lower_alert_name": "ph_low",
                            "lower_alert_value": 7}),

                       ("orp", {  # ORP Sensor
                            "sensor_type": "atlas_scientific",
                            "name": "orp",
                            "is_connected": True,
                            "is_ref": False,
                            "i2c": 98,
                            "accuracy": 0,
                            "test_for_alert": True,
                            "upper_alert_name": "orp_hi",
                            "upper_alert_value": 700,
                            "lower_alert_name": "orp_low",
                            "lower_alert_value": 550})])

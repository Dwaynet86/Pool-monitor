#! /usr/bin/env python

def create_database():
    print("connecting to server...") 
    conn = pymysql.connect(cfg.servername, cfg.username, cfg.password)
    print("connection made")
    curs = conn.cursor()
    curs.execute("SET sql_notes = 0; ")  # Hide Warnings
    print("creating db ", cfg.dbname)
    curs.execute("CREATE DATABASE IF NOT EXISTS {}".format(cfg.dbname))
    print("creating database if not created")
    curs.execute("SET sql_notes = 1; ")  # Show Warnings
    
    # Setup tables
    
    
    
    conn.commit()
    conn.close()
    return
    
def create_relay_tables():

    conn, curs = open_database_connection()

    relaytimer = []
    dtcount = 0

    for number in relaycount:
        relay = ("relay_" + str(number) + "_timer")
        relaytimer.append(relay)

    for tablename in relaytimer:
        curs.execute("CREATE TABLE IF NOT EXISTS {} "
                    "(pk INT UNSIGNED PRIMARY KEY,"
                    "starttime DATETIME DEFAULT NULL, "
                    "stoptime DATETIME DEFAULT "
                    "NULL);".format(tablename))

    # Add default "NULL" data to each relay_timer table

        for pairs in range(1, (numdtpairs[dtcount] + 1)):
            curs.execute("INSERT IGNORE INTO {} (pk,starttime,stoptime)"
                        " VALUES({},NULL,NULL)".format(tablename, pairs))
        dtcount += 1

    close_database_connection(conn, curs)

    return relaytimer


def create_timer_override_table():

    conn, curs = open_database_connection()

    curs.execute("CREATE TABLE IF NOT EXISTS timer_override "
                "(pk INT UNSIGNED PRIMARY KEY);")
    curs.execute("INSERT IGNORE INTO timer_override (pk) VALUES(1)")
    curs.execute("INSERT IGNORE INTO timer_override (pk) VALUES(2)")

    # Add columns and default "off" data to timer_override table

    for number in relaycount:
        relayname = ("relay_" + str(number))
        try:
            curs.execute("ALTER TABLE timer_override ADD {} VARCHAR(5)"
                         .format(relayname))
            curs.execute("UPDATE IGNORE timer_override SET {} = 'off' "
                        "WHERE pk = 1;".format(relayname))
            curs.execute("UPDATE IGNORE timer_override SET {} = 'False' "
                        "WHERE pk = 2;".format(relayname))
        except:
            pass

    close_database_connection(conn, curs)

    return


def create_sensors_table():

    conn, curs = open_database_connection()

    curs.execute("CREATE TABLE IF NOT EXISTS sensors (timestamp DATETIME);")

    for key, value in list(sensors.items()):
        if value["is_connected"] is True:
            try:
                curs.execute("ALTER TABLE sensors ADD {} DECIMAL(10,2);"
                .format(value["name"]))
            except:
                pass

    close_database_connection(conn, curs)

    return


def create_settings_table():

    conn, curs = open_database_connection()

    curs.execute("CREATE TABLE IF NOT EXISTS settings "
                "(pk TINYINT(1) UNSIGNED PRIMARY"
                " KEY);")
    try:
        curs.execute("INSERT IGNORE INTO settings (pk) VALUES(1)")
    except:
        pass
    for key, value in list(sensors.items()):
        try:
            curs.execute("ALTER TABLE settings ADD ({} DECIMAL(10,2), "
            "{} DECIMAL(10,2));".format(value["upper_alert_name"],
                                        value["lower_alert_name"]))
            curs.execute("UPDATE IGNORE settings SET {} = {}, {} = {} "
                    "WHERE pk=1;".format(value["upper_alert_name"],
                                        value["upper_alert_value"],
                                        value["lower_alert_name"],
                                        value["lower_alert_value"]))
        except:
            pass

    for key, value in list(misc_setting.items()):
        if key == "to_email":
            try:
                curs.execute("ALTER TABLE settings ADD {} VARCHAR(254);"
                .format(key))
                curs.execute("UPDATE IGNORE settings SET {} = '{}' "
                        "WHERE pk=1;".format(key, value))
            except:
                pass

        elif key == "pause_readings":
            try:
                curs.execute("ALTER TABLE settings ADD {} BOOLEAN;"
                .format(key))
                curs.execute("UPDATE IGNORE settings SET {} = {} "
                        "WHERE pk=1;".format(key, value))
            except:
                pass

        elif key == "offset_percent":
            try:
                curs.execute("ALTER TABLE settings ADD {} DECIMAL(10,2);"
                .format(key))
                curs.execute("UPDATE IGNORE settings SET {} = {} "
                        "WHERE pk=1;".format(key, value))
            except:
                pass

        else:
            try:
                curs.execute("ALTER TABLE settings ADD {} INT(10);"
                .format(key))
                curs.execute("UPDATE IGNORE settings SET {} = {} "
                        "WHERE pk=1;".format(key, value))
            except:
                pass

    close_database_connection(conn, curs)

    return

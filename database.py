#! /usr/bin/env python


def open_database_connection():

    conn = pymysql.connect(servername, username, password, dbname)
    curs = conn.cursor()
    curs.execute("SET sql_notes = 0; ")  # Hide Warnings

    return conn, curs

def close_database_connection(conn, curs):

    curs.execute("SET sql_notes = 1; ")
    conn.commit()
    conn.close()

def create_database():
    #print("connecting to server...") 
    conn = pymysql.connect(servername, username, password)
    #print(servername, username, password)
    #print("connection made!")
    curs = conn.cursor()
    curs.execute("SET sql_notes = 0; ")  # Hide Warnings
    
    #print("creating database %s") % (dbname)
    curs.execute("CREATE DATABASE IF NOT EXISTS {}".format(dbname))
    
    #print("creating database if not created")
    curs.execute("SET sql_notes = 1; ")  # Show Warnings
    
    conn.commit()
    conn.close()
    return

def create_settings_table():

    conn, curs = open_database_connection()

    curs.execute("CREATE TABLE IF NOT EXISTS settings "
                "(pk TINYINT(1) UNSIGNED PRIMARY"
                " KEY);")
    try:
        # insert pk value 1
        curs.execute("INSERT IGNORE INTO settings (pk) VALUES(1)")
    except:
        pass
    for key, value in list(sensors.items()):
        try:
            # Add upper and lower limits to table
            curs.execute("ALTER TABLE settings ADD ({} DECIMAL(10,2), "
            "{} DECIMAL(10,2));".format(value["upper_alert_name"],
                                        value["lower_alert_name"]))
            # Add values to upper and lower limits
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

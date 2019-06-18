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
    

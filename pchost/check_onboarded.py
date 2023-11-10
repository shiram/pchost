import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('db.sqlite3') 
        return conn
    except Error as e:
        print(e)

def select_status(conn):
    cur = conn.cursor()
    cur.execute("SELECT onboarded FROM appsetup LIMIT 1")

    status = cur.fetchone()
    return status[0] #since tuple return index 0

def is_onboarded():
    conn = create_connection()
    status = select_status(conn)
    return status
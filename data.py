import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('db.sqlite3') # creates a memory-only database for this example
        return conn
    except Error as e:
        print(e)

def create_table(conn):
    try:
        sql = ''' CREATE TABLE appsetup (
                    onboarded BOOLEAN NOT NULL
                ); '''
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def create_appsetup(conn, onboarded_status):
    sql = ''' INSERT INTO appsetup(onboarded)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (onboarded_status,))
    conn.commit()

def update_appsetup(conn, onboarded_status):
    sql = ''' UPDATE appsetup
              SET onboarded = ? 
              WHERE id = 1'''
    cur = conn.cursor()
    cur.execute(sql, (onboarded_status,))
    conn.commit()

def delete_appsetup(conn):
    sql = 'DELETE FROM appsetup WHERE id=1'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def select_all_appsetup(conn):
    cur = conn.cursor()
    cur.execute("SELECT onboarded FROM appsetup LIMIT 1")

    data = cur.fetchone()
    return data[0]

def setup_data():
    print(">>>>>>> Creating a connection to db >>>>>>>>")
    conn = create_connection()

    print(">>>>>>> Creating the table >>>>>>>>")
    create_table(conn)

    print(">>>>>>> Adding data to the table >>>>>>>>")
    create_appsetup(conn, False)
    print(">>>>>>> Finished... >>>>>>>>")

def test_select():
    conn = create_connection()
    data = select_all_appsetup(conn)
    print(data)

if __name__ == "__main__":
    while True:
        print("Please choose an option:")
        print("1. Create data")
        print("2. Select data")
        print("3. Quit")
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            setup_data()
        elif user_choice == '2':
            test_select()
        elif user_choice == '3':
            print("Quitting the program...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

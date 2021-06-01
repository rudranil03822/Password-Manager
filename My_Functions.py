import psycopg2

def store_passwords(usname,key, web, user, pass1, em_mb):
    try:
        connection = connect(key)
        cursor = connection.cursor()
        sql_query = """ INSERT INTO """ +usname+ """(website,username,pass,email_mobile) VALUES (%s, %s, %s, %s)"""
        our_input = (web, user, pass1, em_mb)
        cursor.execute(sql_query, our_input)
        connection.commit()
        print('Password updated')
    except (Exception, psycopg2.Error) as error:
        print(error)

def connect(key):
    try:
        connection = psycopg2.connect(database='pwd_mngr', user='postgres', password=key)
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)

def display(usname,key):
    try:
        connection = connect(key)
        cursor = connection.cursor()
        sql_query = """SELECT * FROM """+usname
        cursor.execute(sql_query)
        result = cursor.fetchall()
        print("Sl,   website,    userID,     password,   email/number")
        for row in result:
            print(row)
            print("\n")
    except (Exception, psycopg2.Error) as error:
        print(error)

def create_profile(usname,key):
    try:
        connection = connect(key)
        cursor = connection.cursor()
        sql_query = """CREATE TABLE """+usname+ """(idno SERIAL PRIMARY KEY, website varchar(50) NOT NULL, username varchar(50) NOT NULL, pass varchar(50) NOT NULL, email_mobile varchar(50))"""
        cursor.execute(sql_query)
        connection.commit()
        print(" Success ")
    except (Exception, psycopg2.Error) as error:
        print(error)

        
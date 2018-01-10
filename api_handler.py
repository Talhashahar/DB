import mysql.connector

import traceback


def connect_to_remote_db():
    try:
        cnx = mysql.connector.connect(user='root', password='1234562',
                                      host='127.0.0.1',
                                      database='db_final_project', port=3306)
        return cnx
        #return 'connected! and disconnected...'
    except Exception as e:
        print (traceback.format_exc())
        return None
        #return e.message + e.args + traceback.format_exc()


def connect_to_local_db():
    try:
        cnx = mysql.connector.connect(user='root', password='1234562',
                                      host='127.0.0.1',
                                      database='db_final_project', port=3306)
        return cnx
        #return 'connected! and disconnected...'
    except Exception as e:
        print (traceback.format_exc())
        return None
        #return e.message + e.args + traceback.format_exc()


def disconnect(cnx):
    cnx.close()

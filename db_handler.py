# import mysql.connector
#
# #dict data {'header_name': value }
# def insert_row(command, tbl,data):
#     query = '{} {} {} {}'.format(command,tbl,data.keys()[0],data[data.keys()[0]])
import mysql.connector

cnx = None


def get_connection():
    global cnx
    if cnx is None:
        cnx = mysql.connector.connect(user='root', password='1234562',
                                      host='127.0.0.1',
                                      database='db_final_project', port=3306)
    return cnx


def disconnectDB():
    cnx = get_connection()
    cnx.close()


def get_all_tables():
    query = "SHOW TABLES"
    cursor = get_connection().cursor()
    cursor.execute(query)
    return_value = cursor.fetchall()
    return return_value


def show_all_tables(tables_names):
    return_value = []
    for table_name in tables_names:
        str = ''.join(table_name)
        return_value.append("table name is " + str)
        rows = show_table(cnx, str)
        for row in rows:
            return_value.append(row)
    return return_value


def show_table(table_name):
    query = "SELECT * FROM " + table_name
    cursor = get_connection().cursor()
    cursor.execute(query)
    return_value = cursor.fetchall()
    return return_value

def init_all_tables():
    project_table = "CREATE TABLE IF NOT EXISTS projects(project_id integer PRIMARY KEY, date text NOT NULL, cu_name text NOT NULL, dev_tools integer NOT NULL, mile_stones integer NOT NULL);"
    dev_tools_table = "CREATE TABLE IF NOT EXISTS dev_tools(project_id integer PRIMARY KEY, tool_id integer NOT NULL, tool_name text NOT NULL, FOREIGN KEY (project_id) REFERENCES projects(project_id));"
    mile_stones_table = "CREATE TABLE IF NOT EXISTS mile_stones(mile_stone_id INTEGER PRIMARY KEY, description text, date text NOT NULL, price FLOAT NOT NULL, project_id INTEGER, FOREIGN KEY (project_id) REFERENCES projects(project_id));;"
    engineer_table = "CREATE TABLE IF NOT EXISTS engineers (engineer_id integer PRIMARY KEY, date_of_birth text NOT NULL, adress text NOT NULL, name text NOT NULL, phone text NOT NULL, age double NOT NULL, software_interests integer NOT NULL);"
    sofware_interests_eng = "CREATE TABLE IF NOT EXISTS sofware_interests (interest_id INTEGER PRIMARY KEY, interest_specelity text NOT NULL, interest_name text NOT NULL, FOREIGN  KEY (interest_id) REFERENCES Engineers(engineer_id));"
    phone_table = "CREATE TABLE IF NOT EXISTS phone (phone_number varchar(10)  PRIMARY KEY, engineer_id integer NOT NULL,  interest_name text NOT NULL, FOREIGN KEY (engineer_id) REFERENCES engineers (engineer_id));"
    project_to_eng_table = "CREATE TABLE IF NOT EXISTS project_to_eng (project_id integer NOT NULL, engineer_id integer NOT NULL, grade double NOT NULL, FOREIGN KEY (project_id) REFERENCES projects (project_id), FOREIGN KEY (engineer_id) REFERENCES Engineers(engineer_id));"
    cursor = get_connection().cursor()
    try:
        cursor.execute(project_table)
        cursor.execute(dev_tools_table)
        cursor.execute(mile_stones_table)
        cursor.execute(engineer_table)
        cursor.execute(sofware_interests_eng)
        cursor.execute(phone_table)
        cursor.execute(project_to_eng_table)
    except Exception as e:
        print "the error is : " + e.message + e.args

def drop_all_tables():
    tables_names = []
    cursor = get_connection().cursor()
    tables_names = get_all_tables()
    for table_name in tables_names:
        str = ''.join(table_name)
        try:
            cursor.execute("drop table " + str)
        except Exception as e:
            print ("Drop table failed with table " + str + "   " + e.message + e.args)

    #project_table = "CREATE TABLE IF NOT EXISTS projects(project_number integer PRIMARY KEY, date text NOT NULL, cu_name text NOT NULL, dev_tools integer NOT NULL, mile_stones integer NOT NULL, FOREIGN KEY (dev_tools) REFERENCES dev_tools (project_number));"

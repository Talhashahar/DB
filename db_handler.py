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
    db = get_connection()
    db.close()


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
    project_table = "CREATE TABLE IF NOT EXISTS projects(project_id integer PRIMARY KEY, date text NOT NULL, cu_name text NOT NULL, name text NOT NULL);"
    dev_tools_table = "CREATE TABLE IF NOT EXISTS dev_tools(project_id integer, tool_id integer NOT NULL, PRIMARY KEY(project_id, tool_id), tool_name text NOT NULL, FOREIGN KEY (project_id) REFERENCES projects(project_id)) ON DELETE CASCADE ON UPDATE CASCADE;"
    mile_stones_table = "CREATE TABLE IF NOT EXISTS mile_stones(project_id INTEGER, mile_stone_id INTEGER, PRIMARY KEY(project_id, mile_stone_id), description text, date text NOT NULL, price DOUBLE NOT NULL, FOREIGN KEY (project_id) REFERENCES projects(project_id)) ON DELETE CASCADE ON UPDATE CASCADE;"
    engineer_table = "CREATE TABLE IF NOT EXISTS engineers (engineer_id integer PRIMARY KEY, date_of_birth text NOT NULL, adress text NOT NULL, name text NOT NULL, software_interests integer NOT NULL, FOREIGN KEY (software_interests) REFERENCES software_interests(interest_id)) ON DELETE CASCADE ON UPDATE CASCADE;"
    software_interests_eng = "CREATE TABLE IF NOT EXISTS software_interests (interest_id INTEGER PRIMARY KEY, interest_specelity text NOT NULL, interest_name text NOT NULL);"
    phone_table = "CREATE TABLE IF NOT EXISTS phone (phone_number varchar(10)  PRIMARY KEY, engineer_id integer NOT NULL, FOREIGN KEY (engineer_id) REFERENCES engineers (engineer_id));"
    project_to_eng_table = "CREATE TABLE IF NOT EXISTS project_to_eng (project_id integer NOT NULL, engineer_id integer NOT NULL, grade double NOT NULL, FOREIGN KEY (project_id) REFERENCES projects (project_id), FOREIGN KEY (engineer_id) REFERENCES Engineers(engineer_id)) ON DELETE CASCADE ON UPDATE CASCADE;"
    cursor = get_connection().cursor()
    try:
        cursor.execute(project_table)
        cursor.execute(dev_tools_table)
        cursor.execute(mile_stones_table)
        cursor.execute(software_interests_eng)
        cursor.execute(engineer_table)
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


def insert_engineer(id, date, adr, name, interests):
    query = ("insert into engineers VALUES (%s, %s, %s, %s, %s)")
    data = (id, date, adr, name, interests)
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(query, data)
        db.commit()
    except Exception as e:
        print "insert failed to engineer table " + e.message + e.args
        db.rollback()


def insert_interests(id, speceity, name):
    query = ("INSERT INTO software_interests "
             "(interest_id, interest_specelity, interest_name)"
             " VALUES (%s, %s, %s)")
    data = (id, speceity, name)
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(query, data)
        db.commit()
    except Exception as e:
        print "insert failed to software_interests tables " + e.message + e.args
        db.rollback()


def insert_phone(number, id):
    query = ("insert into phone VALUES (%s, %s)")
    data = (number, id)
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(query, data)
        db.commit()
    except Exception as e:
        print "insert failed to phone table " + e.message + e.args
        db.rollback()


def insert_projects(proj_id, date, customer_name, name):
    query = ("insert into projects VALUES (%s, %s, %s, %s)")
    data = (proj_id, date, customer_name, name)
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(query, data)
        db.commit()
    except Exception as e:
        print "insert failed to projects " + e.message + e.args
        db.rollback()


def insert_dev_tools(proj_id, tool_id, tool_name):
    query = ("insert into dev_tools VALUES (%s, %s, %s)")
    data = (proj_id, tool_id, tool_name)
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(query, data)
        db.commit()
    except Exception as e:
        print "insert failed to dev_tools table " + e.message + e.args
        db.rollback()


def insert_mile_stones(project_id, ms_id, description, date, price):
    query = ("insert into mile_stones VALUES (%s, %s, %s, %s, %s)")
    data = (project_id, ms_id, description, date, price)
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(query, data)
        db.commit()
    except Exception as e:
        print "insert failed to mile_stones table " + e.message + e.args
        db.rollback()


def insert_project_to_eng(proj_id, engineer_id, grade):
    query = ("insert into project_to_eng VALUES (%s, %s, %s)")
    data = (proj_id, engineer_id, grade)
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(query, data)
        db.commit()
    except Exception as e:
        print "insert failed to project_to_eng table " + e.message + e.args
        db.rollback()


def get_engineer_by_id(eng_id):
    query = ("select * from engineers where engineer_id=%s")
    data = eng_id
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(query, (data,))
    except Exception as e:
        print 'insert failed ' + e.message + e.args
    res = cursor.fetchall()[0]
    return res

def get_engineer_name_by_id(id):
    query = ("select name from engineers where engineer_id=%s")
    data = id
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(query, (data,))
    except Exception as e:
        print 'get engineer name by id failed ' + e.message + e.args
    res = cursor.fetchall()[0]
    return res


def get_avg_grade_by_project_id(project_id):
    query = ("SELECT avg(grade) from db_final_project.project_to_eng WHERE project_id = %s")
    data = project_id
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(query, (data,))
    except Exception as e:
        print 'get avarge from project_2_grade id failed ' + e.message + e.args
    res = cursor.fetchall()[0]
    return res


def get_project_id_from_grade():
    query = ("select project_id from project_to_eng;")
    cursor = get_connection().cursor()
    cursor.execute(query)
    return_value = cursor.fetchall()
    return return_value


def delete_eng_by_id(eng_id):
    query = ("delete from engineers where engineer_id=%s;")
    data = eng_id
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(query, data)
        db.commit()
    except Exception as e:
        print "delete engineer failed " + e.message + e.args
        db.rollback()


def delete_project_by_id(prj_id):
    query = ("delete from engineers where engineer_id=%s;")
    data = prj_id
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(query, data)
        db.commit()
    except Exception as e:
        print "delete engineer failed " + e.message + e.args
        db.rollback()


def delete_software_interests_by_id(interests_id):
    query = ("delete from engineers where engineer_id=%s;")
    data = interests_id
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(query, data)
        db.commit()
    except Exception as e:
        print "delete engineer failed " + e.message + e.args
        db.rollback()


def update_engineer(id, date, adr, name, interests):
    query = ("""
    update engineers 
    set date_of_birth=%s, adress=%s, name=%s, software_interests=%s) 
    where engineer_id=%s"""), (date, adr, name, interests, id)
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(query)
        db.commit()
    except Exception as e:
        print "insert failed to engineer table " + e.message + e.args
        db.rollback()



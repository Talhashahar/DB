import json
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask import Flask, request, jsonify, Response
import api_handler
import db_handler

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return 'Hello!,!'


@app.route('/connect_remote', methods=['GET', 'POST'])
def connect_remote():
    cnx = api_handler.connect_to_remote_db()
    return cnx


@app.route('/connect_local', methods=['GET', 'POST'])
def connect_local():
    try:
        cnx = api_handler.connect_to_local_db()
        return cnx
    except Exception as e:
        print e.message + e.args
        return None


@app.route('/disconnect', methods=['GET', 'POST'])
def disconnect(cnx):
    api_handler.disconnect(cnx)


@app.route('/index', methods=['GET', 'POST'])
def index():
    ret = 'b'#api_handler.connect_to_db()
    return '<h1>' + ret + '<h1>'


@app.route('/show-all-tbl', methods=['GET', 'POST'])
def show_all_tables():
    res = db_handler.show_all_tables(db_handler.get_all_tables())
    return res


@app.route('/show-tbl/<table>', methods=['GET', 'POST'])
def show_tbl(table):
    res = db_handler.show_table(table)
    return str(res)
    pass


@app.route('/init_all', methods=['GET', 'POST'])
def init_table():
    db_handler.init_all_tables()


@app.route('/drop_all', methods=['GET', 'POST'])
def drop_tables():
    db_handler.drop_all_tables()


@app.route('/init_data', methods=['GET', 'POST'])
def init_data():
    try:
        db_handler.insert_interests(123, 'backend', 'python')
        db_handler.insert_interests(321, 'frontend', 'python')
        db_handler.insert_interests(456, 'backend', 'java')
        db_handler.insert_interests(654, 'frontend', 'java')
        db_handler.insert_engineer(111, '05.02.94', 'Shenkar', 'Shaked', 123)
        db_handler.insert_engineer(222, '01.02.91', 'Merkaz', 'Avi', 456)
        db_handler.insert_engineer(333, '01.02.90', 'Herzeliya', 'Tal', 321)
        db_handler.insert_engineer(444, '01.02.89', 'Ramat Gan', 'Tomer', 321)
        db_handler.insert_phone('0524424445', 333)
        db_handler.insert_phone('0523719826', 222)
        db_handler.insert_phone('0532777866', 111)
        db_handler.insert_phone('0546578900', 111)
        db_handler.insert_projects(789, '01.01.2018', 'albert', 'kipat-barzel')
        db_handler.insert_projects(987, '01.01.2017', 'hpe', 'serverXYZ')
        db_handler.insert_projects(101112, '05.11.2014', 'sony', 'playstation')
        db_handler.insert_dev_tools(789, 1, 'xyz')
        db_handler.insert_dev_tools(987, 21, 'zyx')
        db_handler.insert_dev_tools(789, 777, 'dbtools')
        db_handler.insert_dev_tools(101112, 64, 'mytools')
        db_handler.insert_mile_stones(789, 888, 'MM-Zibi', '01.01.1990', 1729.22)
        db_handler.insert_mile_stones(101112, 1, 'Start', '05.11.2015', 1000)
        db_handler.insert_mile_stones(101112, 2, 'mid', '05.11.2016', 1000)
        db_handler.insert_mile_stones(101112, 2, 'finish', '05.11.2017', 3500)
        db_handler.insert_project_to_eng(789, 111, 90)
        db_handler.insert_project_to_eng(987, 111, 80)
        db_handler.insert_project_to_eng(101112, 222, 50)
        db_handler.insert_project_to_eng(101112, 333, 60)
        db_handler.insert_project_to_eng(101112, 444, 80)
    except Exception as e:
        print e.message + e.args
    finally: return Response("lol")


@app.route('/engs_in_project/<project_name>', methods=['GET', 'POST'])
def engs_in_project(project_name):
    listofengineer = []
    listeng = []
    project_to_eng = db_handler.show_table('project_to_eng')
    projects = db_handler.show_table('projects')
    for project in projects:
        if project[3] == project_name:
            project_id = project[0]
            break
    for proj in project_to_eng:
        if proj[0] == project_id:
            listofengineer.append(proj)
    for eng in listofengineer:
        listeng.append(db_handler.get_engineer_by_id(eng[1]))
    try:
        listeng.sort(key=lambda x: x[4])
    except Exception as e:
        print e.message
    pass


@app.route('/eng_names_by_prj', methods=['GET', 'POST'])
def eng_names_by_prj():
    project_to_eng = db_handler.show_table('project_to_eng')
    project_to_eng.sort(key=lambda x: x[0])
    prjAndeng = []
    last_prg = project_to_eng[0][0]
    prjAndeng.append(last_prg)
    for y in project_to_eng:
        if last_prg != y[0]:
            prjAndeng.append(y[0])
        egnineer_name = db_handler.get_engineer_name_by_id(y[1])
        prjAndeng.append(egnineer_name)
        last_prg = y[0]
    return prjAndeng


@app.route('/get_avg_by_prj_id', methods=['GET', 'POST'])
def get_avg_by_prj_id():
    project_list = db_handler.get_project_id_from_grade()
    project_list = list(set(project_list))
    avglist = []
    for prj_id in project_list:
        res = db_handler.get_avg_grade_by_project_id(prj_id[0])
        avglist.append(res)
    return avglist


if __name__ == '__main__':
    app.run()

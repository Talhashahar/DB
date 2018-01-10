import json
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask import Flask, request, jsonify
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
def show_all_tables(cnx):
    res = db_handler.show_all_tables(cnx, db_handler.get_all_tables(cnx))
    return res

@app.route('/show-tbl/<table>', methods=['GET', 'POST'])
def show_tbl(cnx, table):
    return db_handler.show_table(cnx, table)

@app.route('/init_all', methods=['GET', 'POST'])
def init_table():
    db_handler.init_all_tables()


@app.route('/drop_all', methods=['GET', 'POST'])
def drop_tables():
    db_handler.drop_all_tables()


if __name__ == '__main__':
    app.run()

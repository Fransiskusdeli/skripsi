"""import xlrd
location=('D:\TUGAS KULIAH INFORMATIKA\SEM 8\SEM 8 - SKRIPSI\Data Penting\ST-Dekan_Update_new.xls')

var_workbook = xlrd.open_workbook(location)
sheet = var_workbook.sheet_by_index(0)
print(sheet.cell_value(2,0))"""

# import pandas as pd
# #read file st dekan
# dataframe1 = pd.read_excel(r'D:\TUGAS KULIAH INFORMATIKA\SEM 8\SEM 8 - SKRIPSI\Data Penting\ST-Dekan_Update_new.xls')
# #data = pd.Series([1,2,3]) read data per baris
# print(dataframe1)
# #read file st rektor
# dataframe2 = pd.read_excel(r'D:\TUGAS KULIAH INFORMATIKA\SEM 8\SEM 8 - SKRIPSI\Data Penting\ST-Rektor_Update_new.xls')
# #data = pd.Series([1,2,3]) read data per baris
# print(dataframe2)

#testing connection
# cur = conn.cursor()
# cur.execute("CREATE TABLE hayo(id serial PRIMARY KEY, name CHAR(50), roll integer);")
# print("Table Created....")
# conn.commit()
# conn.close()

# print("Database berhasil connect....")

# from dash import Dash, html, dcc
# import plotly.express as px
# import pandas as pd

from flask import Flask, request, session, redirect, url_for, render_template, flash;
import psycopg2
import psycopg2.extras
import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# app.secret_key = 'cairocoders-ednalan'

DB_HOST = "localhost"
DB_NAME = "surat_tugas"
DB_USER = "postgres"
DB_PASS = "admin"
conn = psycopg2.connect(database="surat_tugas", user="postgres", password="admin", host="localhost", port="5432")

# @app.route('/', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'testuname1' or request.form['password'] != 'testpass1':
#             error = 'Username atau Password anda salah. Silahkan coba kembali'
#         else:
#             return redirect(url_for("homepage.html"))
#     return render_template("login.html", error=error)
#
#
# if __name__ == '__main__':
#      app.run(debug=True)

#login
@app.route('/login/', methods=['GET', 'POST'])
def login():
    cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        # print(username)
        # print(password)

        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()

        if account:
            password_rs = account['password']
            print(password_rs)
            if check_password_hash(password_rs, password):
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                return redirect(url_for('homepage'))
            else:
                error = 'Username atau Password anda salah. Silahkan coba kembali'
        else:
            error = 'Username atau Password anda salah. Silahkan coba kembali'
    return render_template("login.html")

#home
@app.route('/')
def homepage():
    if 'loggedin' in session:
        return render_template('homepage', username=session['username'])
    return redirect(url_for('login'))

# #register
# @app.route('/register/')
# def register():


if __name__ == '__main__':
     app.run(debug=True)


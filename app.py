from flask import Flask, render_template, request, session, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import json

app = Flask(__name__)
app.secret_key = "lesgo"

# Connecting app to DB

app.config['MYSQL_USER'] = 'fjjcoreudogl1fxb'
app.config['MYSQL_PASSWORD'] = 'zuiyjci4038yq91m'
app.config['MYSQL_HOST'] = 'xlf3ljx3beaucz9x.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_DB'] = 'u9zs3sxzsl1bf3ly'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

db = MySQL(app)

@app.route("/")
def index():
    # declaring tables for DB:

    #cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    #cursor.execute('''CREATE TABLE person (userid INTEGER, password VARCHAR(30), first_name VARCHAR(30), last_name VARCHAR(30), birth_date date, email_address VARCHAR(50), address VARCHAR(60), patient_patient_id INTEGER, physician_physician_id INTEGER)''')
    #cursor.execute('''CREATE TABLE patient (patient_id INTEGER)''')
    #cursor.execute('''CREATE TABLE physician (pysician_id INTEGER, clinic_address VARCHAR(60))''')
    #cursor.execute('''CREATE TABLE appointment (appointment_id INTEGER, description VARCHAR(300), patient_patient_id INTEGER, availability_availability_id INTEGER)''')
    #cursor.execute('''CREATE TABLE availability (availability_id INTEGER, start_time date, end_time date, physician_physician_id INTEGER)''')
    #cursor.execute('''INSERT INTO accounts VALUES(30217890, "abc123")''')
    #cursor.connection.commit()

    return render_template("form.html")

# Login method

@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST' and 'userid' in request.form and 'password' in request.form:
        userid = request.form['userid']
        password = request.form['password']
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('''CREATE TABLE accounts (userid INTEGER, password VARCHAR(32))''')
        cursor.execute('SELECT * FROM accounts WHERE userid = %s AND password = %s', (userid, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['userid'] = account['userid']
            session['password'] = account['password']
            msg = 'logged in successfully.'
            return render_template('scheduler.html', msg=msg)
        else:
            msg = 'Incorrect username / password!'
    return render_template('form.html', msg=msg)

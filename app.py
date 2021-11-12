# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import MySQLdb
from flask import Flask, render_template, request, session, jsonify
from flask_mysqldb import MySQL
import json


app = Flask(__name__)
db = MySQL(app)

app.config['MYSQL_USER'] = 'fjjcoreudogl1fxb'
app.config['MYSQL_PASSWORD'] = 'zuiyjci4038yq91m'
app.config['MYSQL_HOST'] = 'xlf3ljx3beaucz9x.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_DB'] = 'u9zs3sxzsl1bf3ly'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def hello():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('''CREATE TABLE accounts (user_id INT(9), password VARCHAR(32), ''')
    return render_template("form.html")


@app.route('/newaccount')
def newaccount():
    return render_template('create.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST' and 'account_id' in request.form and 'password' in request.form:
        user_id = request.form['user_id']
        password = request.form['password']
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('''CREATE TABLE accounts (user_id INT(9), password VARCHAR(32), ''')
        cursor.execute('SELECT * FROM accounts WHERE user_id = %s AND password = %s', (user_id, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['user_id'] = account['user_id']
            session['password'] = account['password']
            return 'Logged in successfully !'
        else:
            msg = 'Incorrect username / password!'
            return render_template('formfailed.html')
        db.connection.commit()
        cursor.close()
    return render_template('scheduler.html')
    db.connection.commit()
    cursor.close()


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import MySQLdb
from flask import Flask, render_template, request, session, jsonify
from flask_mysqldb import MySQL
import json


app = Flask(__name__)
db = MySQL(app)

app.config['MYSQL_USER'] = 'kcpfar0g2e7hgqbe'
app.config['MYSQL_PASSWORD'] = 'j51sb4ak6b9tpup0'
app.config['MYSQL_HOST'] = 'd6rii63wp64rsfb5.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_DB'] = 'fzscfmwkq57p3pdd'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def hello():
    return render_template("form.html")


@app.route('/newaccount')
def newaccount():
    return render_template('create.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('''CREATE TABLE accounts (username VARCHAR(16), password VARCHAR(32), email VARCHAR(32))''')
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['username'] = account['username']
            session['password'] = account['password']
            return 'Logged in successfully !'
        else:
            msg = 'Incorrect username / password!'
            return render_template('formfailed.html')
    return render_template('home.html')
    # db.connection.commit()
    # cursor.close()


@app.route('/create', methods=['POST'])
def create():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = db.connection.cursor()
        cursor.execute(''' INSERT INTO accounts VALUES(%s,%s,%s)''', (username, password, email))
        db.connection.commit()
        cursor.close()
        return render_template("created.html")


@app.route('/users', methods=['GET'])
def users():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM accounts")
    rows = cursor.fetchall()
    usernames = []
    content = {}

    for result in rows:
        content = {'username': result['username'], 'password': result['password'], 'email': result['email']}
        usernames.append(content)
        content = {}
    with open('outfile.json', 'w') as outfile:
        json.dump(usernames, outfile, indent=4)
    return jsonify(usernames)


    # cursor.execute('''CREATE TABLE accounts (username VARCHAR(16), password VARCHAR(32), email VARCHAR(32))''')

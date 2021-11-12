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
        # cursor.execute('SELECT * FROM accounts WHERE user_id = %s AND password = %s', (user_id, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['user_id'] = account['user_id']
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

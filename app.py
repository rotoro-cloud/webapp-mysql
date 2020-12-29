from flask import Flask
from flask import render_template
import socket
import mysql.connector
import os

app = Flask(__name__)

DB_Host = os.environ.get('DB_Host') or "localhost"
DB_Database = os.environ.get('DB_Database') or "mysql"
DB_User = os.environ.get('DB_User') or "root"
DB_Password = os.environ.get('DB_Password') or "paswrd"

@app.route("/")
def main():
    db_connect_result = False
    err_message = ""
    try:
        mysql.connector.connect(host=DB_Host, database=DB_Database, user=DB_User, password=DB_Password)
        rocket = 'rocket_fly'
        db_connect_result = True
    except Exception as e:
        rocket = 'rocket_crash'
        err_message = str(e)

    return render_template('view.html', debug="Переменные окружения: DB_Host=" + (os.environ.get('DB_Host') or "Not Set") + "; DB_Database=" + (os.environ.get('DB_Database')  or "Not Set") + "; DB_User=" + (os.environ.get('DB_User')  or "Not Set") + "; DB_Password=" + (os.environ.get('DB_Password')  or "Not Set") + "; " + err_message, db_connect_result=db_connect_result, name=socket.gethostname(), rocket=rocket)

@app.route("/debug")
def debug():
    rocket = 'rocker_scanner'
    return render_template('view.html', debug="Переменные окружения: DB_Host=" + (os.environ.get('DB_Host') or "Not Set") + "; DB_Database=" + (os.environ.get('DB_Database')  or "Not Set") + "; DB_User=" + (os.environ.get('DB_User')  or "Not Set") + "; DB_Password=" + (os.environ.get('DB_Password')  or "Not Set"), rocket=rocket)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

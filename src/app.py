from flask import Flask
from flask import render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
import os


fake_db: list[dict] = []

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/explore')
def explore():
    return render_template('explore.html')


@app.route('/login',methods = ['POST'])
def login():
    fake_name = 'iwan'
    user = request.form['nm']
    return 'Valid name' if user == fake_name else 'Not valid'


if __name__ == '__main__':
    app.run(debug=True)
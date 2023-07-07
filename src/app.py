from flask import Flask
from flask import render_template, request
import os
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username') 
    print(username)
    # your code
    # return a response
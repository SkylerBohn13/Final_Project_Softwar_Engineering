import json

from flask import request, Flask, redirect, url_for, render_template
import requests

import db


#db.prepare_db()



app = Flask(__name__)

# This app is just for testing. Never expose your secret in a production app!
app.secret_key = b'mysecretkey'


@app.route('/', endpoint='index')
def index():
    return render_template('home.html')

@app.route('/admin/login', endpoint='admin_login')
def admin_login():
    return render_template('adminLogin.html')



@app.route('/v1/login', methods=['POST'], endpoint='api_login')
def api_login():
    """Using a hardcoded admin password for the MVP of this project"""

    headers = {}
    if not request.form['username'] or not request.form['password']:
        body = {
            'error': 'missingFields',
            'details': 'Must include username and password'
        }
        return (body, 400, headers)

    user_provided = request.form['username']
    password = request.form['password']
    if user_provided != 'admin' or password != 'admin':  # Hardcoded password, no secure!
        body = {
            'error': 'passwordInvalid',
            'details': 'Password was not valid'
        }
        return (body, 400, headers)

    body = {
        'error': 'None',
        'details': 'Member logged in successfully'
    }
    return (body, 200, headers)


@app.route('/login', methods=['GET'], endpoint='login')
def login():
    return render_template('adminLogin.html')


@app.route('/admin', methods=['GET'], endpoint='admin')
def admin():
    return render_template('admin.html')

@app.route('/v1/voters', methods=['GET'], endpoint='voters')
def voters():
    body = {
        'voters': [
            {
                'id': '1234',
                'first_name': 'john',
                'last_name': 'doe',
                'address': '123 sycamore ln'
            },
            {
                'id': '5678',
                'first_name': 'don',
                'last_name': 'rickles',
                'address': '145 masters ln'    
            },
        ]
    }
    return (body, 200)


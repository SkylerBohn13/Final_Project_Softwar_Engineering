import json

from flask import request, Flask, render_template
import requests

from db import get_sqlite3_conx
from voter_db import initializeVoters, initializeCandidates, addVoter, getVoters, addCandidate, getCandidates
from voter import Voter
from candidate import Candidate


VOTER_DB = 'voters.db'
CANDIDATES_DB = 'candidates.db'


conx = get_sqlite3_conx(VOTER_DB)
initializeVoters(conx)
initializeCandidates(conx)
conx.close()


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

@app.route('/v1/admin/voters', methods=['GET', 'POST'], endpoint='voters')
def voters():
    conx = get_sqlite3_conx(VOTER_DB)
    if request.method == 'GET':
        body = json.dumps(getVoters(conx))

        return (body, 200)

    elif request.method == 'POST':
        print(request.json)
        if not request.json:
            return ({'error': 'No body found'}, 400)
        
        voter_record = request.json
        new_voter = Voter(as_json=voter_record)
        addVoter(conx, new_voter)
        return (voter_record, 201)

@app.route('/v1/admin/candidates', methods=['GET', 'POST'], endpoint='candidates')
def candidates():
    conx = get_sqlite3_conx(VOTER_DB)
    if request.method == 'GET':
        body = json.dumps(getCandidates(conx))

        return (body, 200)

    elif request.method == 'POST':
        if not request.json:
            return ({'error': 'No body found'}, 400)
        
        voter_record = request.json
        new_candidate = Candidate(as_json=voter_record)
        addCandidate(conx, new_candidate)
        return (voter_record, 201)

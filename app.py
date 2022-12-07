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

@app.route('/voter', methods=['GET'], endpoint='voter')
def vote():
    return render_template('voter.html')


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
            return ({'error': 'No body found'}, 402)
        
        voter_record = request.json
        new_voter = Voter(as_json=voter_record)
        addVoter(conx, new_voter)
        print(f"voter record: {voter_record}")
        voter_record["id"] = new_voter.id
        return (voter_record, 201)


@app.route('/v1/admin/candidates', methods=['GET', 'POST'], endpoint='candidates')
def candidates():
    conx = get_sqlite3_conx(VOTER_DB)
    if request.method == 'GET':
        body = json.dumps(getCandidates(conx))
        return (body, 200)

    elif request.method == 'POST':
        if not request.json:
            return ({'error': 'No body found'}, 401)
        
        voter_record = request.json
        new_candidate = Candidate(as_json=voter_record)
        addCandidate(conx, new_candidate)
        return (voter_record, 201)

@app.route('/v1/admin/votes', methods=['GET', 'POST'], endpoint='votes')
def votes():
    conx = get_sqlite3_conx(VOTER_DB)
    if request.method == 'GET':
        body = json.dumps(getVotes(conx))

        return (body, 200)

    elif request.method == 'POST':
        if not request.json:
            return ({'error': 'No body found'}, 400)
        
        vote_record = request.json
        new_vote = Vote(as_json=vote_record)
        addVote(conx, new_vote)
        return (vote_record, 201)

@app.route('/v1/admin/vote_totals', methods=['GET'], endpoint='vote_totals')
def vote_totals():
    conx = get_sqlite3_conx(VOTER_DB)
    votes = getVotes(conx)
    totals = votes.get('votes', None)
    if not totals:
        raise Exception('Could not retrieve totals from body')

    president_votes = {}
    vice_president_votes = {}
    senator_votes = {}
    representative_votes = {}
    for vote in totals:
        president = vote.get('president', None)
        vice_president = vote.get('vice_president', None)
        senator = vote.get('senator', None)
        representative = vote.get('representative', None)
        if not president or not vice_president or not senator or not representative:
            print('Vote record must include president, vice_president, senator, and representative')
            continue # record is corrupt, skip it

        if not president_votes.get(president, None):
            president_votes[president] = 0
        president_votes[president] += 1

        if not vice_president_votes.get(vice_president, None):
            vice_president_votes[vice_president] = 0
        vice_president_votes[vice_president] += 1

        if not senator_votes.get(senator, None):
            senator_votes[senator] = 0
        senator_votes[senator] += 1

        if not representative_votes.get(representative, None):
            representative_votes[representative] = 0
        representative_votes[representative] += 1

    president_votes_sorted = sorted(president_votes.items(), key=lambda x: x[1])[0]
    vice_president_votes_sorted = sorted(vice_president_votes.items(), key=lambda x: x[1])[0]
    senator_votes_sorted = sorted(senator_votes.items(), key=lambda x: x[1])[0]
    representative_votes_sorted = sorted(representative_votes.items(), key=lambda x: x[1])[0]

    body = {
        'vote_totals': {
            'president': president_votes,
            'vice_president': vice_president_votes,
            'senator': senator_votes,
            'representative': representative_votes,
        },
        'winners': {
            'president': {
                'name': president_votes_sorted[0],
                'votes': president_votes_sorted[1]
            },
            'vice_president': {
                'name': vice_president_votes_sorted[0],
                'votes': vice_president_votes_sorted[1]
            },
            'senator': {
                'name': senator_votes_sorted[0],
                'votes': senator_votes_sorted[1]
            },
            'representative': {
                'name': representative_votes_sorted[0],
                'votes': representative_votes_sorted[1]
            }
        }
    }

    return (body, 200)

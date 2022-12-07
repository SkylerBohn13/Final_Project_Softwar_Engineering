import requests

pres1 = {
    'position': 'president',
    'first_name': 'Marvin',
    'last_name': 'Martian'
}

pres2 = {
    'position': 'president',
    'first_name': 'Bugs',
    'last_name': 'Bunny'
}

vice_pres1 = {
    'position': 'vice_president',
    'first_name': 'Tweety',
    'last_name': 'Bird'
}

vice_pres2 = {
    'position': 'vice_president',
    'first_name': 'Yosemite',
    'last_name': 'Sam'
}

senator1 = {
    'position': 'senator',
    'first_name': 'Daffy',
    'last_name': 'Duck'
}

senator2 = {
    'position': 'senator',
    'first_name': 'Porky',
    'last_name': 'Pig'
}

rep1 = {
    'position': 'representative',
    'first_name': 'Babs',
    'last_name': 'Bunny'
}

rep2 = {
    'position': 'representative',
    'first_name': 'Foghorn',
    'last_name': 'Leghorn'
}

url = 'http://127.0.0.1:5000/v1/admin/candidates'

candidates = [pres1, pres2, vice_pres1, vice_pres2, senator1, senator2, rep1, rep2]

for c in candidates:

    resp = requests.post(url, json=c)
    print(resp)
    assert resp.status_code == 201

resp = requests.get(url)
print("Candidates: ", resp.text)
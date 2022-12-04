#!/usr/bin/env python3

import sqlite3

from db import query_result


DB_NAME = 'voters.db'


def initializeVoters(conx):
    cursor = conx.cursor()
    # Creates table voterInfo and deletes all rows to ensure a clean dataset
    cursor.execute("CREATE TABLE IF NOT EXISTS voterInfo(id,firstName,lastName,address)")
    cursor.execute("DELETE FROM voterInfo")
    conx.commit()

def initializeCandidates(conx):
    cursor = conx.cursor()
    # Creates table candidateInfo and deletes all rows to ensure a clean dataset
    cursor.execute("CREATE TABLE IF NOT EXISTS candidateInfo(id,firstName,lastName,position)")
    cursor.execute("DELETE FROM candidateInfo")
    conx.commit()

def addVoter(conx, voter):
    cursor = conx.cursor()
    # Creates unique voterID by concatenating first,last,address
    cursor.execute("INSERT INTO voterInfo (id,firstName,lastName,address) VALUES (?,?,?,?)",
                   (voter.id, voter.first_name, voter.last_name, voter.address))
    conx.commit()
    print("Created candidates DB")


def getVoters(conx):
    query = 'SELECT * FROM voterInfo'
    formatted_results = []
    results = query_result(conx, query, empty_results=True, all_fields=True)
    if len(results) > 0:
        for r in results:
            formatted_results.append(
                {
                    'id': r[0],
                    'first_name': r[1],
                    'last_name': r[2],
                    'address': r[3],
                }
            )

    response_body = {
        'voters': formatted_results
    }

    return response_body
    
def addCandidate(conx, candidate):
    cursor = conx.cursor()
    cursor.execute("INSERT INTO candidateInfo (id, firstName, lastName, position) VALUES (?,?,?,?)",
                   (candidate.id, candidate.first_name, candidate.last_name, candidate.position))
    conx.commit()

def getCandidates(conx):
    query = 'SELECT * FROM candidateInfo'
    formatted_results = []
    results = query_result(conx, query, empty_results=True, all_fields=True)
    if len(results) > 0:
        for r in results:
            formatted_results.append(
                {
                    'id': r[0],
                    'first_name': r[1],
                    'last_name': r[2],
                    'position': r[3],
                }
            )

    response_body = {
        'candidates': formatted_results
    }
    
    return response_body

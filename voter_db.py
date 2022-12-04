#!/usr/bin/env python3

import sqlite3

from db import query_result


DB_NAME = 'voters.db'


def initializeTables(conx):
    cursor = conx.cursor()
    # Creates table voterInfo and deletes all rows to ensure a clean dataset
    cursor.execute("CREATE TABLE IF NOT EXISTS voterInfo(voterID,firstName,lastName,address)")
    cursor.execute("DELETE FROM voterInfo")
    conx.commit()
    # Creates table candidateInfo and deletes all rows to ensure a clean dataset
    cursor.execute("CREATE TABLE IF NOT EXISTS candidateInfo(candidateID,firstName,lastName,desiredPosition)")
    cursor.execute("DELETE FROM candidateInfo")
    conx.commit()

def addVoter(conx, voter):
    cursor = conx.cursor()
    # Creates unique voterID by concatenating first,last,address
    cursor.execute("INSERT INTO voterInfo (voterID,firstName,lastname,address) VALUES (?,?,?,?)",
                   (voter.id, voter.first_name, voter.last_name, voter.address))
    conx.commit()


def getVoters(conx):
    query = 'SELECT * FROM voterInfo'
    result = query_result(conx, query, empty_results=True, all_fields=False)
    result_dict = {
        'id': result[0],
        'first_name': result[1],
        'last_name': result[2],
        'address': result[3],
    }
    return result_dict
    
def addCandidate(conx, firstName,lastName,desiredPosition):
    cursor = conx.cursor()
    # Creates unique candidateID by concatenating first,last,position
    candidateID = firstName+lastName+desiredPosition
    cursor.execute("INSERT INTO candidateInfo (candidateID,firstName,lastname,desiredPosition) VALUES (?,?,?,?)",
                   (candidateID,firstName,lastName,desiredPosition))
    conx.commit()

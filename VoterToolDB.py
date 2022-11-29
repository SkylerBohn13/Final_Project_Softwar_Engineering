#!/usr/bin/env python3

import sqlite3

# Initialize database
db1 = sqlite3.connect("VoteDB.db")

# Create cursor to execute SQL commands
cursor = db1.cursor()

def initializeTables():
    # Creates table voterInfo and deletes all rows to ensure a clean dataset
    cursor.execute("CREATE TABLE IF NOT EXISTS voterInfo(voterID,firstName,lastName,address)")
    cursor.execute("DELETE FROM voterInfo")
    # Creates table candidateInfo and deletes all rows to ensure a clean dataset
    cursor.execute("CREATE TABLE IF NOT EXISTS candidateInfo(candidateID,firstName,lastName,desiredPosition)")
    cursor.execute("DELETE FROM candidateInfo")

def addVoter(firstName,lastName,address):
    # Creates unique voterID by concatenating first,last,address
    voterID = firstName+lastName+address
    cursor.execute("INSERT INTO voterInfo (voterID,firstName,lastname,address) VALUES (?,?,?,?)",
                   (voterID,firstName,lastName,address))
    db1.commit()
    
def addCandidate(firstName,lastName,desiredPosition):
    # Creates unique candidateID by concatenating first,last,position
    candidateID = firstName+lastName+desiredPosition
    cursor.execute("INSERT INTO candidateInfo (candidateID,firstName,lastname,desiredPosition) VALUES (?,?,?,?)",
                   (candidateID,firstName,lastName,desiredPosition))
    db1.commit()

# main created for testing purposes    
def main():
    initializeTables()
    firstName = input("voterFN: ") 
    lastName = input("voterLN: ")                
    address = input("voterAD: ")   
    addVoter(firstName,lastName,address)             
    result = cursor.execute("SELECT * FROM voterInfo")
    print (result.fetchall())

main()

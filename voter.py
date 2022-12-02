import hashlib


class Voter:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.id = self.GenerateID()

    def GenerateID(self):
        formatted_name = self.name.replace(' ', '')
        return formatted_name.lower() + hashlib.md5(self.address.encode()).hexdigest()

    def ViewInfo(self):
        return "Voter Name: "+self.name +"\nVoter Address: "+self.address+"\nVoter ID: "+self.voterID






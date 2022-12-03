import hashlib


class Voter:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.id = self.GenerateID()

    def GenerateID(self):
        formatted_name = f"{self.first_name.replace(' ', '')}{self.last_name.replace(' ', '')}"
        return formatted_name.lower() + hashlib.md5(self.address.encode()).hexdigest()

    def ViewInfo(self):
        return "Voter Name: "+self.name +"\nVoter Address: "+self.address+"\nVoter ID: "+self.voterID






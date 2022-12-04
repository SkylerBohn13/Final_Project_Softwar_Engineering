import hashlib

from person import Person


class Voter(Person):
    def __init__(self, first_name='N/A', last_name='N/A', address='N/A', as_json=None):
        if as_json:
            fname = as_json.get('first_name')
            lname = as_json.get('last_name')
            super().__init__(fname, lname)  # call parent init method to write name fields for true inheritance

            self.address = as_json.get('address')
        else:
            super().__init__(first_name, last_name)  # call parent init
            self.address = address
        self.id = self.GenerateID()

    def GenerateID(self):
        formatted_name = f"{self.first_name.replace(' ', '')}{self.last_name.replace(' ', '')}"
        return formatted_name.lower() + hashlib.md5(self.address.encode()).hexdigest()

    def ViewInfo(self):
        return "Voter Name: "+self.name +"\nVoter Address: "+self.address+"\nVoter ID: "+self.voterID






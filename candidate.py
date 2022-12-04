import hashlib

from person import Person


class Candidate(Person):
    def __init__(self, first_name='N/A', last_name='N/A', position='N/A', as_json=None):
        if as_json:
            fname = as_json.get('first_name')
            lname = as_json.get('last_name')
            super().__init__(fname, lname)  # call parent init method to write name fields for true inheritance

            self.position = as_json.get('position')
        else:
            super().__init__(first_name, last_name)  # call parent init
            self.position = position
        self.id = self.GenerateID()

    def GenerateID(self):
        formatted_name = f"{self.first_name.replace(' ', '')}{self.last_name.replace(' ', '')}"
        formatted_position = f"{self.position.lower().replace(' ', '')}"
        return formatted_name.lower() + hashlib.md5(formatted_position.encode()).hexdigest()

    def ViewInfo(self):
        return "Candidate Name: "+self.name +"\Candidate Position: "+self.position+"\Candidate ID: "+self.voterID
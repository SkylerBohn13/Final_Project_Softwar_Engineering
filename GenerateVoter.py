class GenerateVoter:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.voterID = self.name.lower() + ''.join(e for e in address if e.isalnum()).lower()

    def GenerateID(self):
        temp = self.name.lower() + (self.address.lower().sub('[\W+]', '', mystring))
        self.voterID = temp

    def SetAddress(self,address):
        self.address = address

    def ViewInfo(self):
        return "Voter Name: "+self.name +"\nVoter Address: "+self.address+"\nVoter ID: "+self.voterID






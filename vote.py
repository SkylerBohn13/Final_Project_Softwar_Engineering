class Vote:
    def __init__(self, voter_id='N/A', president='N/A', vice_president='N/A', senator='N/A', representative='N/A', as_json=None):
        if voter_id == 'N/A' and president == 'N/A' and vice_president == 'N/A' and senator == 'N/A' and representative == 'N/A' and as_json is None:
            raise Exception('Must include required fields or as_json')

        if as_json:
            self.voter_id = as_json.get('voter_id', '')
            self.president = as_json.get('president', '')
            self.vice_president = as_json.get('vice_president', '')
            self.senator = as_json.get('senator')
            self.representative = as_json.get('representative', '')

            if len(self.voter_id) < 1 or len(self.president) < 1 or len(self.vice_president) < 1 or len(self.senator) < 1 or len(self.representative) < 1:
                raise Exception('Vote requires president, vice_president, senator, and representative fields')

        else:
            self.voter_id = voter_id
            self.president = president
            self.vice_president = vice_president
            self.senator = senator
            self.representative = representative

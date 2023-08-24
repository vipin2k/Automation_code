import os
import uuid


class Constants:
    def __init__(self):
        # create params dict
        self.patientParams = {}
        # create constant values
        os.environ['EnvironmentName'] = "dev"
        os.environ['docspera_id'] = ""
    def patientParameters(self, uuidval):
     
        # set env variables
        os.environ['file_name'] = uuidval
        # store it in dict 
        self.patientParams['EnvironmentName'] = os.getenv('EnvironmentName')
        self.patientParams['docspera_id'] = os.getenv('docspera_id')
        return self.patientParams


import requests
import os
from CommonClass.api_utils.CommonApiActions import find_values

class Validations():
    def __init__(self, logger):
        self.logger = logger

    def statusCodeValidation(self,statuscodes,responsestatuscode ):
        try:
            assert str(responsestatuscode) in statuscodes
            return True
        except AssertionError:
            return False

    def negativeStatusCodeValidation(self,negativeresponsestatuscode):
        try:
            assert negativeresponsestatuscode in self.negativestatuscodevalidation
            return True
        except AssertionError as err:
            return False

    def responseTimeValidation(self, reponsetime):
        try:
            if reponsetime<1:
                return 'Low response time'
            else:
                self.logger.warning('This endpoint took more than 1 sec for response !')
                return 'High response time'

        except requests.exceptions.Timeout as e:
            print('Timeout exception')

    def stringValidations(self,keyName, listValue, envValue, logger=None, contains=None):
        for stringValue in listValue:
            if contains is True:
                if os.getenv(envValue) in stringValue:
                    print("         "+keyName + ' in Acknowledgement is same as the '+keyName +" Generated "+"("+os.getenv(envValue)+")."+" -PASS")

            if os.getenv(envValue) == stringValue:
                print("         "+keyName + ' in Acknowledgement is same as the '+keyName+" Generated "+"("+os.getenv(envValue)+")."+" -PASS")
            else:
                continue

    def BasicValidations(self,keyName, listValue, envValue, logger=None, contains=None):
        for stringValue in listValue:
            if contains is True:
                if envValue in stringValue:
                    print("         "+keyName + ' in Response is same as the '+keyName +" Generated "+"("+str(envValue)+")."+" -PASS")

            if envValue == stringValue:
                print("         "+keyName + ' in Response is same as the '+keyName+" Generated "+"("+str(envValue)+")."+" -PASS")
            else:
                continue

    def jsonValidation(self, response, ResponseBodyVerification, logger):
        responseText = response.text
        DataFromAckJson = {}
        try:
            for i in range(len(ResponseBodyVerification)):
                DataFromAckJson[ResponseBodyVerification[i]] = []
                DataFromAckJson[ResponseBodyVerification[i]] = find_values(ResponseBodyVerification[i], responseText)
            return DataFromAckJson
        except Exception as e:
            logger.info(e)
            return None
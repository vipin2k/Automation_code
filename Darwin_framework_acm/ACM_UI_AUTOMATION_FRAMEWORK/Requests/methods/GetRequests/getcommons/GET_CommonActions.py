from asyncio import constants
from asyncio.log import logger
import json
import os, sys
from CommonClass.api_utils.CommonApiActions import writeResponseBodyInJson
from CommonClass.api_utils.FrameworkConstants import Constants
from Requests.methods.GetRequests.getcommons.GET_MakeEndpoint import makeEndpoint
from CommonClass.api_utils.RequestsLib import apiRequest, renameJsonDir
from CommonClass.api_utils.RequestValidations import Validations

current_path = os.path.abspath('.')
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)

validations = Validations(logger=logger)

def get_user(apiTestData, endpointkey, configLogger, readPayLoadJson=None, env_instance=None,headers=None):
    logger = configLogger
    try:
        # get endpoint details
        endPoint, Token, ResponseCode, ResponseBodyVerification, ResponseBodyType = makeEndpoint(apiTestData["BaseUrl"].get("GetBaseUrl"), apiTestData, endpointkey, 'Valid '+endpointkey)
        # Get the endpoint
        endPointAfterReplacement = endPoint.replace('user_id',"2").replace('{', "").replace('}', "")
        print("endPointAfterReplacement :"+endPointAfterReplacement)
        endPointAfterReplacement = endPointAfterReplacement + "?" + Token
        responseBodyDict, reponseBody, Headers = apiRequest("GET", endPointAfterReplacement, ResponseCode, configLogger,ResponseBodyVerification=ResponseBodyVerification, ResponseBodyType=ResponseBodyType)
        print("reponseBody :"+str(reponseBody))
        # filename = ""
        # writeResponseBodyInJson(filename, jsonData=json.loads(reponseBody))
        if 'plain' != ResponseBodyType.lower():            
            validations.BasicValidations('first name', responseBodyDict.get('first_name'), 'Janet')
            validations.BasicValidations('last name', responseBodyDict.get('last_name'), 'Weaver')
    except AssertionError as error:
        logger.error("Validation error in given api endpoint, exception is:" + str(error))
        assert False

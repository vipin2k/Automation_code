import os, sys, requests, json
from Requests.methods.PutRequests.putcommons.PUT_MakeEndpoint import makeEndpoint
from CommonClass.api_utils.RequestsLib import apiRequest

current_path = os.path.abspath('.')
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)


def put_user(apiTestData, endpointkey, configLogger, readPayLoadJson=None, headers=None, env_instance=None, update_scenario=None):
    logger = configLogger
    try:
        # get endpoint details
        endPoint, Token, ResponseCode, ResponseBodyVerification, ResponseBodyType = makeEndpoint(apiTestData["BaseUrl"].get("Put Valid Data"), apiTestData, endpointkey, 'Valid Patient')
        # Get the endpoint
        endPointAfterReplacement = endPoint.replace('uuid', os.getenv('file_name')).replace('{', "").replace('}', "")
        endPointAfterReplacement = endPointAfterReplacement+"?"+Token
        responseBodyDict, reponseBody, Headers=apiRequest("PUT", endPointAfterReplacement, ResponseCode, configLogger, readPayLoadJson, headers, ResponseBodyType=ResponseBodyType)

    except AssertionError as error:
        logger.error("Validation error in given api endpoint, exception is:" + str(error))
        assert False

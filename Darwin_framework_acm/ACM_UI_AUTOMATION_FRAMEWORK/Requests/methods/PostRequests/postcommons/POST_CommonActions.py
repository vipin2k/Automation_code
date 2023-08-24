import os, sys, requests, json
from Requests.methods.PostRequests.postcommons.POST_MakeEndpoint import makeEndpoint
from CommonClass.api_utils.RequestsLib import apiRequest

current_path = os.path.abspath('.')
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)


def post_user(apiTestData, endpointkey, configLogger, readPayLoadJson=None, headers=None, env_instance=None, update_scenario=None):
    logger = configLogger
    try:
        # get endpoint details
        endPoint, Token, ResponseCode, ResponseBodyVerification, ResponseBodyType = makeEndpoint(apiTestData["BaseUrl"].get("PostBaseUrl"), apiTestData, endpointkey, 'Valid '+endpointkey)
        # Get the endpoint
        endPointAfterReplacement = endPoint #.replace('uuid', os.getenv('file_name')).replace('{', "").replace('}', "")
        endPointAfterReplacement = endPointAfterReplacement #"?"+Token
        readPayLoadJson = None
        print("endPointAfterReplacement : "+endPointAfterReplacement)
        print("ResponseCode : "+ResponseCode)
        print("configLogger : "+str(configLogger))
        print("readPayLoadJson : "+str(readPayLoadJson))
        print("headers : "+str(headers))
        print("ResponseBodyType : "+str(ResponseBodyType))
        responseBodyDict, reponseBody, Headers=apiRequest("POST", endPointAfterReplacement, ResponseCode, configLogger, readPayLoadJson, headers, ResponseBodyType=ResponseBodyType)
        print("responseBodyDict : "+responseBodyDict)
        print("reponseBody : "+reponseBody)

    except AssertionError as error:
        logger.error("Validation error in given api endpoint, exception is:" + str(error))
        assert False

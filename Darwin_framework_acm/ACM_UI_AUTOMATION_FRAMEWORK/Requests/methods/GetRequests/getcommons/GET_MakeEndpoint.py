import os

from CommonClass.api_utils.CommonApiActions import ApiActions

def makeEndpoint(baseUrl, apiTestData, endpointkey, serviceName):
    ApiActionsObj = ApiActions(apiTestData)
    # POST_CommonActions
    BaseUrl = baseUrl
    # env_name = "Dev" if os.getenv("EnvironmentName") is None else os.getenv("EnvironmentName").title()
    # BaseUrl = ApiActionsObj.replace_all(env_name, BaseUrl)
    # Get the current dict
    currentDict = ApiActionsObj.listToDict(listVal=apiTestData, methodName='GetMethodUrls', serviceName=serviceName)
    endPointWithoutBaseUrl = currentDict.get(endpointkey).get("EndPoint")
    # Get the endpoint
    ResponseBodyType = currentDict.get(endpointkey).get("ResponseType")
    ResponseBodyVerification = currentDict.get(endpointkey).get("ResponseValidation")
    ResponseCode = currentDict.get(endpointkey).get("ResponseCode")
    Token = ""
    endPoint = BaseUrl + endPointWithoutBaseUrl

    return endPoint, Token, ResponseCode, ResponseBodyVerification, ResponseBodyType
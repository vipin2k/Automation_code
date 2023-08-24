from asyncio.log import logger
import json
import os,shutil
import requests
from CommonClass.api_utils.RequestValidations import Validations


def apiRequest(requestType, endPoint, ResponseCode, logger, readPayLoadJson=None, headers=None, ResponseBodyVerification=None, ResponseBodyType=None, env_instance=None):
    ValidationsObj = Validations(logger)
    try:
        if readPayLoadJson is None:
            readPayLoadJson = {}
            headers = {}
        if 'PUT' == requestType.upper():
            response = requests.put(endPoint, data=json.dumps(readPayLoadJson), headers=headers)
        if 'GET' == requestType.upper():
            response = requests.get(endPoint, data=json.dumps(readPayLoadJson), headers=headers)
        if 'POST' == requestType.upper():
            response = requests.post(endPoint, data=json.dumps(readPayLoadJson), headers=headers)
        if 'DELETE' == requestType.upper():
            response = requests.delete(endPoint, data=json.dumps(readPayLoadJson), headers=headers)
        # Response code and response time
        statusCodeValidation = ValidationsObj.statusCodeValidation(ResponseCode, response.status_code)
        # response body - verification
        if statusCodeValidation is True:
            #logger.info("Response body values need to verify: " + str(ResponseBodyVerification))
            if ResponseBodyType is not None or ResponseBodyType.lower() != 'plain':
                if 'json' == ResponseBodyType.lower():
                    responseBody = ValidationsObj.jsonValidation(response, ResponseBodyVerification, logger)
                    # logger.info('Response validation values from given api response: ' + str(responseBody))
                    return responseBody, response.text, response.headers
            else:
                return None
        else:
            logger.error('Expected response code [' + str(
                ResponseCode) + '] not matched with the current end point response code [' + str(
                response.status_code) + ']')
    except requests.exceptions.RequestException as e:
        logger.info(e)

def renameJsonDir():
    try:
        # make ack json file
        source = f"{os.getcwd()}/Payload/JsonList/"
        des = f"{os.getcwd()}/Payload/JsonList/"
        try:
            os.rename(source, des)
        except:
            try:
                for i in os.listdir(source):
                    shutil.move(source+i,des)
            except:
                source = f"{os.getcwd()}/Payload/JsonList/"
                des = f"{os.getcwd()}/Payload/JsonList/"
                for i in os.listdir(source):
                    shutil.move(source+i, des)

    except FileNotFoundError as e:
        print(f"ERROR: {e}")


def listRequirements(arg):
    lisOfReq = []
    for i in range(len(arg)):
        lisOfReq.append(arg[i][2])
    return lisOfReq
         

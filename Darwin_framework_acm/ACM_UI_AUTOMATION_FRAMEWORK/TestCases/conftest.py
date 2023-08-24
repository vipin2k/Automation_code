import pytest
import os, re
import json
import logging,logging.config
import allure
import mysql.connector
import uuid
from CommonClass.api_utils.FrameworkConstants import Constants
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


############################# Allure config #######################################
class AllureLoggingHandler(logging.Handler):
    def log(self, message):
        with allure.step('Log {}'.format(message)):
            pass

    def emit(self, record):
        self.log("({}) {}".format(record.levelname, record.getMessage()))


class AllureCatchLogs:
    def __init__(self):
        self.rootlogger = logging.getLogger()
        self.allurehandler = AllureLoggingHandler()

    def __enter__(self):
        if self.allurehandler not in self.rootlogger.handlers:
            self.rootlogger.addHandler(self.allurehandler)

    def __exit__(self, exc_type, exc_value, traceback):
        self.rootlogger.removeHandler(self.allurehandler)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup():
    with AllureCatchLogs():
        yield

def pytest_configure(config):
    config._metadata = None

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call():
    with AllureCatchLogs():
        yield

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown():
    with AllureCatchLogs():
        yield


############################# custom fixtures ######################################

# get env name for test

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Type in environment name e.g. dev or idev")
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")


@pytest.fixture(scope='class')
def env_setup(request):
    environ = request.config.getoption("--env")
    os.environ["environment"] = environ
    return environ

@pytest.fixture(scope='class')
def test_setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    driver.quit()
    print("Test completed")


@pytest.fixture(scope="class")
def readPayLoadJsonWithUUID(request):
    active_uuid = uuid.uuid4()
    filepath = f"{os.getcwd()}/{str(request.param)}"
    with open(filepath, 'r') as js:
        base_jsondata = json.load(js)
    js.close()
    base_jsonStr = json.dumps(base_jsondata)
    # logging.info('base_jsonStr :'+base_jsonStr)
    jsonDataModify = Constants().patientParameters(str(active_uuid))
    for keys, value in jsonDataModify.items():
        if keys in base_jsonStr:
            base_jsonStr = base_jsonStr.replace("{{" + keys + "}}", value)
    jsonData = json.loads(base_jsonStr)
    return jsonData


@pytest.fixture(scope="class")
def readPayLoadJson(request):
    filepath = f"{os.getcwd()}/{str(request.param)}"
    with open(filepath, 'r') as js:
        jsondata = json.load(js)
    js.close()
    return jsondata


@pytest.fixture(scope="class")
def readPayLoadXml(request):
    filepath = os.getcwd() + "\\" + str(request.param)
    xmldata = open(filepath, 'rb')

    return xmldata


@pytest.fixture(scope="class")
def readPayLoadTextFile(request):
    with open(os.getcwd() + "\\" + str(request.param), 'r') as file:
        data = file.read().replace('\r', '')
    return data


@pytest.fixture(scope="class")
def readUploadFilePath(request):
    filepath = f"{os.getcwd()}/{str(request.param)}"
    return filepath

@pytest.fixture(scope="class")
def apiTestData():
    # get env name
    env_name = os.getenv("environment")
    print("env_name : "+env_name)
    # read json for access the env data
    with open(f"{os.getcwd()}/ConfigFiles/{env_name}/API/ApiTestData.json", 'r') as js:
        apiEndpointData = json.load(js)
    js.close()
    # return the dict for test data
    return apiEndpointData

@pytest.fixture(scope="class")
def uiTestData():
    # get env name
    # env_name = os.getenv("environment")
    env_name = "dev"
    print("env_name : "+env_name)
    # read json for access the env data
    with open(f"{os.getcwd()}/ConfigFiles/{env_name}/UI/UiTestData.json", 'r') as js:
        print(os.getcwd())
        testData = json.load(js)
    js.close()
    # return the dict for test data
    return testData


@pytest.fixture(scope="class")
def readEnvDataFromDB():
    # get env name
    env_name = "dev" if os.getenv("EnvironmentName") is None else os.getenv("EnvironmentName")
    # sqlquery = 'SELECT * FROM api_automation.post_openjobs_endpoints;'
    method_lst = ['get', 'post', 'put', 'delete', 'head', 'patch']
    # read json for access the env data
    with open(os.getcwd() + '/ConfigFiles/'+env_name+'/DB/DbConfigData.json', 'r') as js:
        dbjsondata = json.load(js)
    js.close()
    # store the retrived data to variable
    endpoint_sqlquerylst = dbjsondata['SqlQuery']['Enpoint_Query']
    endpoint_baseurl_query = dbjsondata['SqlQuery']['BaseUrlQuery'][0].replace('$env', env_name)
    endpoint_headers_query = dbjsondata['SqlQuery']['HeadersQuery'][0]
    endpoint_auth_query = dbjsondata['SqlQuery']['AuthQuery'][0]
    password = os.getenv("dbUserPassword")
    # DB Connection
    db = mysql.connector.connect(host=dbjsondata['DbCredentials']['HostName'],
                                 user=dbjsondata['DbCredentials']['DbUsername'], passwd=password)
    cursor = db.cursor()
    # Final dict for env data
    finalendpointdict = {}
    for sqlquery in endpoint_sqlquerylst:
        sqlquery = sqlquery.replace('$env', env_name)
        ServiceName, MethodName = (re.split('[_,.]', sqlquery)[-2].title()), (re.split('[_,.]', sqlquery)[2].title())
        if MethodName.lower() in method_lst:
            MethodName = MethodName.title() + "MethodUrls"
        # fetch db data
        cursor.execute(sqlquery)
        columns = cursor.description
        # dict for store the db data
        finalendpointdict_temp1 = {}
        finalendpointdict_temp2 = {}
        client_secdict = {}
        for value in cursor.fetchall():
            tmp = {}
            for (index, column) in enumerate(value):
                tmp[columns[index][0]] = column
            finalendpointdict_temp1[tmp['EndPointName']] = tmp
        finalendpointdict_temp2[ServiceName] = finalendpointdict_temp1
        finalendpointdict.setdefault(MethodName, [])
        finalendpointdict[MethodName].append(finalendpointdict_temp2)
    # base url dict
    BaseUrlDict = {}
    cursor.execute(endpoint_baseurl_query)
    for value in cursor.fetchall():
        BaseUrlDict[value[2]] = value[3]
    finalendpointdict["BaseUrl"] = BaseUrlDict
    # Herders read
    HeadersDict = {}
    cursor.execute(endpoint_headers_query)
    for value in cursor.fetchall():
        HeadersDict[value[1]] = value[2]
    finalendpointdict["Headers"] = HeadersDict
    # Client read
    ClientDict = {}
    cursor.execute(endpoint_auth_query)
    cli_columns = cursor.description
    for value in cursor.fetchall():
        cli_tmp = {}
        for (index, column) in enumerate(value):
            cli_tmp[cli_columns[index][0]] = column
        ClientDict[cli_tmp['Id']] = cli_tmp
    finalendpointdict["Credentials"] = ClientDict
    with open(os.getcwd() + '', 'w') as jsonfile:
        json.dump(finalendpointdict, jsonfile, sort_keys=True, indent=8, ensure_ascii=False)
    jsonfile.close()
    # return the dict for test data
    return finalendpointdict


@pytest.fixture(scope="class")
def configLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger



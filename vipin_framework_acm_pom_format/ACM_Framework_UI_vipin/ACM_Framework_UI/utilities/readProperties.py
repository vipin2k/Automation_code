import configparser

config = configparser.RawConfigParser()
# config.read(".\\Configurations\\config.ini")
# configFilePath = r'D:\Users\pvelu\.jenkins\workspace\sample\00ACM_Framework_UI\Configurations\config.ini'
# config = configparser.RawConfigParser()
# config.read(".\\Configurations\\config.ini")
configFilePath = r'.\ACM_Framework_UI\Configurations\config.ini'
config.read(configFilePath)


class ReadConfig:
    @staticmethod
    def getApplicationURl():
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getFirstname():
        firstname = config.get('common info', 'firstname')
        return firstname

    @staticmethod
    def getLastname():
        lastname = config.get('common info', 'lastname')
        return lastname

    @staticmethod
    def getMember_id():
        member_id = config.get('common info', 'member_id')
        return member_id

    @staticmethod
    def getMember_DOB():
        DOB = config.get('common info', 'DOB')
        return DOB

    @staticmethod
    def getEffective_date():
        Effective_date = config.get('common info', 'Effective_date')
        return Effective_date

    @staticmethod
    def getSearchMemberid():
        SearchMemberid = config.get('common info', 'search_id')
        return SearchMemberid

    @staticmethod
    def getexisting_member_id():
        existing_member_id = config.get('common info', 'existing_member_id')
        return existing_member_id

    @staticmethod
    def getAdmit_date():
        Admit_date = config.get('common info', 'Admit_date')
        return Admit_date

    @staticmethod
    def getunit_date():
        unit_date = config.get('common info', 'unit_date')
        return unit_date

    @staticmethod
    def getdischarge_date():
        discharge_date = config.get('common info', 'discharge_date')
        return discharge_date

    @staticmethod
    def getowner():
        owner = config.get('common info', 'owner')
        return owner

    @staticmethod
    def getfacility():
        facility = config.get('common info', 'facility')
        return facility

    @staticmethod
    def getstart_date():
        start_date = config.get('common info', 'start_date')
        return start_date

    @staticmethod
    def getTo_date():
        To_date = config.get('common info', 'To_date')
        return To_date

    @staticmethod
    def getrequestedunits():
        requested_units = config.get('common info', 'requested_units')
        return requested_units

    @staticmethod
    def getDescription():
        Description = config.get('common info', 'Description')
        return Description

    @staticmethod
    def getdiagnoses_score():
        diagnoses_score = config.get('common info', 'diagnoses_score')
        return diagnoses_score


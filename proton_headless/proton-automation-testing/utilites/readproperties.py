import configparser
import os

# Use relative path for the config file
configFilePath = os.path.join(os.path.dirname(__file__), '../Configuration/config.ini')
print("Config file path:", configFilePath)

config = configparser.RawConfigParser()
config.read(configFilePath)


class Readconfig:
    @staticmethod
    def get_proton_url():
        demo_url = config.get('common info', 'proton_Demo_url')
        dev_url = config.get('common info', 'Proton_Dev_Url')
        live_url = config.get('common info', 'proton_Live_Url')
        return demo_url, dev_url, live_url

    @staticmethod
    def getusername():
        login_username = config.get('common info', 'Username')
        return login_username

    @staticmethod
    def get_password():
        login_password = config.get('common info', 'Password')
        return login_password

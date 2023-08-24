import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="./Logs/automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d%/Y %I:%M:%S %p')
        logger = logging.getLogger('automation.log')
        logger.setLevel(logging.INFO)
        return logger
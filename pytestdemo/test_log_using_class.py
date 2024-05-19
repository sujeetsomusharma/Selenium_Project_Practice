import logging  # this is package


# object created and logging.logger() is a method
class LogClass:
    def getLogger(self):
        logger = logging.getLogger(__name__)  # __name__ to   generate test case name

        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)  # filehandler object

        # setting the level

        logger.setLevel(logging.INFO)

        logger.debug("Debug statement is executed")
        logger.info("Information statement")
        logger.warning("Something is in warning mode")
        logger.error("A Major error has happened")
        logger.critical("Critical issue")

        return logger

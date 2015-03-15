import logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s; %(thread)d; %(name)s:%(levelname)s %(funcName)15s\t%(message)s")

getLogger = logging.getLogger
INFO = logging.INFO
DEBUG = logging.DEBUG
WARN = logging.WARN
ERROR = logging.ERROR

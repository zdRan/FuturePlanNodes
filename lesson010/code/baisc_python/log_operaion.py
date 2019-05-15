import logging

LOG_FORMAT = "%(asctime)s -%(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
#logging.basicConfig(filename="python.log", level=logging.WARNING, format=LOG_FORMAT, datefmt=DATE_FORMAT)

#
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
# logging.debug("debug log")
# logging.warning("warning log")
# logging.info("info log")
# logging.error("error log")


logger = logging.getLogger()

logger.setLevel(9)

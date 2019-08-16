import logging

LOG_FORMAT = "%(asctime)s -%(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
# logging.basicConfig(filename="python.log", level=logging.WARNING, format=LOG_FORMAT, datefmt=DATE_FORMAT)

#
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
# logging.debug("debug log")
# logging.warning("warning log")
# logging.info("info log")
# logging.error("error log")


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 文件处理器。输入到文件
file_handler = logging.FileHandler("all_python.log", encoding="UTF-8")

# 流处理器，输出到控制台
stream_handler = logging.StreamHandler()

# 错误日志单独输出到 指定文件
error_handler = logging.FileHandler("error.log", encoding="UTF-8")
error_handler.setLevel(logging.ERROR)

# 将处理器添加到 logger 中
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.addHandler(error_handler)

# 格式化
formatter = logging.Formatter(fmt=LOG_FORMAT,datefmt=DATE_FORMAT)
# 设置每个处理器的 格式
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# 过滤器
my_filter = logging.Filter()
my_filter.filter("github")
file_filter_handler = file_handler.addFilter(my_filter)
print(file_filter_handler)
logger.info("日志打印，，，")
logger.info("日志打印 github ，，，")
logger.error("错误日志打印")





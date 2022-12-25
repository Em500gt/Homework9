import logging

logging.basicConfig(
    level=logging.INFO,
    filename='logger.log',
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S ',
)

def read_file():
    with open('logger.log', 'r') as file_log:
        readin = file_log.read()
        print(readin)
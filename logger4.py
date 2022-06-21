import sys
from logging import *
# LOG_FORMAT='%asctime)s // %(message)// %(lineno)d'
LOG_FORMAT='{asctime} {levelname} {funcName} {lineno} {message}'
basicConfig(filename='logfile3.log',level=NOTSET,filemode='w', style='{', format=LOG_FORMAT, datefmt='%d-%m-%y %H:%M:%S')
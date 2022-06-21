import sys
from logging import *
# LOG_FORMAT='%asctime)s // %(message)// %(lineno)d'
LOG_FORMAT=' {name} {asctime} {funcName} {message}  {levelname}  {lineno}'
basicConfig(filename='logfile2.log',level=DEBUG,filemode='w', style='{', format=LOG_FORMAT, datefmt='%d-%m-%y %H:%M:%S')
# by default logger is root now we will changing logger using getlogger
logger=getLogger("kirti")
logger.debug("this is debug")

logger.warning("this is warning")

logger.critical("this is critical")


def fun(a):

    try:
        k = 5 / a
        logger.error("this is error")

        print(k)
    except:
        logger.error(sys.exc_info())

fun(0)


# note that braces () are necessary here for
# multiple exceptions
# except:
    # logger.error("this is error")

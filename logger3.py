from logger4 import *

debug(sys.exc_info())

warning(sys.exc_info())
critical(sys.exc_info())


def fun(a):

    try:
        k = 5 / a
        print(k)
    except:
        error(sys.exc_info())

fun(0)


# note that braces () are necessary here for
# multiple exceptions
# except:
    # logger.error("this is error")

# Logging is a Python module in the standard library that provides the facility to work with the framework for releasing log messages from the Python programs
# How Logging Works
# The logging is a powerful module used by the beginners as well as enterprises. This module provides a proficiency to organize different control handlers and a transfer log messages to these handlers.
#
# To releasing a log message, we need to import the logging module as follows.
#
# import logging
# Now, we will call the logger to log messages that we want to see. The logging module offers the five levels that specify the severity of events. Each event contains the parallel methods that can be used to log events at the level of severity. Let's understand the following events and their working.
#
# DEBUG - It is used to provide detailed information and only use it when there is diagnosing problems.
# INFO - It provides the information regarding that things are working as we want.
# WARNING - It is used to warn that something happened unexpectedly, or we will face the problem in the upcoming time.
# ERROR - It is used to inform when we are in some serious trouble, the software hasn't executed some programs.
# CRITICAL - It specifies the serious error, the program itself may be incapable of remaining executing.
# The above levels are sufficient to handle any types of problems. These corresponding numerical values of the levels are given below.
#
# Level	Numeric Values
# NOTSET	0
# DEBUG	10
# INFO	20
# WARNING	30
# ERROR	40
# CRITICAL	50
# The logging module offers many features. It consists of several constants, classes, and methods. The constants are represented by the all caps latter; the classes are represented by capital letters. The items with lowercase represent methods.


from logging import *
basicConfig(filename='logfile.log',level=DEBUG,filemode='w',format='%(asctime)s --%(message)s')
debug("this is debug")
warning("this is warning")
error("this is error")
critical("this is critical")
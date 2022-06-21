import logging
class Loggerdemo:
    def sample_logger(self):
        # 1.create logger
        logger=logging.getLogger("demolog")
        # 2.set log level
        logger.setLevel(logging.DEBUG)
        # 3.add console handler-config to show your logs on console or file handler-config to save your logs in file
        ch=logging.StreamHandler()
        fh=logging.FileHandler("logger5.log")
        # 4.add your formatter to console or file handler
        formatter=logging.Formatter('%(asctime)s- %(levelname)s - %(name)s - %(message)s',datefmt='%d/%m/%y , %h:%m:%s')

        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        logger.addHandler(ch)
        logger.addHandler(fh)
        logger.debug("bebug")
        logger.info("info")
a=Loggerdemo()
a.sample_logger()
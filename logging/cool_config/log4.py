#!/usr/bin/env python
# coding: utf-8
import logging.config

LOGGER_CONFIG_FILE = 'log4.conf'
LOG_FILE_TO_STORE = 'my.log'


def get_cool_logger(logger_config_file=LOGGER_CONFIG_FILE, log_file=LOG_FILE_TO_STORE):
    try:
        logging.config.fileConfig(logger_config_file, defaults={'logfilename': log_file})       
        return logging.getLogger('cool_logger')
    except OSError as e:        
        logging.basicConfig(format = u"%(asctime)s - %(levelname)-8s - %(message)s", level=logging.DEBUG)
        logger=logging.getLogger(__name__)
        logger.warning("Can't load log configuration file, cause: {}".format(e))        
        return logger

logger = get_cool_logger()


#Test
if __name__=='__main__':
	for i in range(0,10):
		logger.debug('debug message')
		logger.info('info message')
		logger.warn('warn message')
		logger.error('error message')
		logger.critical('critical message')

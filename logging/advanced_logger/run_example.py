#!/usr/bin/env python
#coding: utf-8
import os
# Настройки конфига логера, тоже можно определить 
# и в настройках окржения, например, 
# используя команду export (linux)
os.environ['DEBUG'] = 'True'
os.environ['ROTATE_PERIOD_FOR_ZIP'] = 'm'
# os.environ['DEBUG_FILE_LOG'] = 'my_debug.log'
# os.environ['PRODUCTION_FILE_LOG'] = 'my_production.log'
# os.environ['ARHIVE_NANE'] = 'logs.zip'
from time import sleep
import logging_config
import logging
import other_my_module

logger = logging.getLogger(__name__)


# Тест1, просто выводим сообщения
logger.debug('The Main')
logger.info('The Main')
logger.warning('The Main')
logger.error('The Main')
logger.critical('The Main')


# Test2, логирование в другом нашем модуле
other_my_module.foo()


# Test3, Traceback тоже пишется
try:
	raise Exception
except Exception as e:
	logger.exception(e)


# Test4, будет создан архив через минуту
for i in range(35):    
    logger.debug('--This is debug message--')
    logger.info('--This is hello message--')
    sleep(2)


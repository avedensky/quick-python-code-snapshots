#!/usr/bin/env python
#coding: utf-8

# Этот модуль настраивает логирование
#
# Для использования, просто импортировать этот модуль в main модуль
# import logging_config
#
# Далее, в любом модуле нашей программы (в том числе и в main):
# import logging
# logger = logging.getLogger(__name__)
#
# Используем:
# logger.debug('The Main')
# logger.info('The Main')
#
#
# Логирование предусматривает два режима работы debug и production.
# Для их переключения следует использовать переменную окружения DEBUG.
# из кода можно определить переменную окружения так:
# import os
# os.environ['DEBUG'] = 'True'
#
# В DEBUG = True режиме:
# Будут писаться в файл и выводиться в консоль все сообщения уровня debug.
# 
# В DEBUG = False режиме:
# Будут писаться в файл и выводиться в консоль все сообщения уровня false.
#
# Используя переменные окружения DEBUG_FILE_LOG, PRODUCTION_FILE_LOG, 
# можно задать имена лог файлов, по умолчанию debug.log и production.log.
# 
# Также присутствует функция ротации логов
#
# avedensky@gmail.com <|>copyleft<|>2018<|>

import logging
import logging.config
from os import getenv


class DebugModeTrueFilter(logging.Filter):
    def filter(self, record):
        debug_mode = getenv('DEBUG', 'true').lower()
        return True if debug_mode == 'true' else False
            

class DebugModeFalseFilter(logging.Filter):
    def filter(self, record):
        debug_mode = getenv('DEBUG', 'true').lower()
        return True if debug_mode == 'false' else False
        

dictLogConfig = {    
    'version': 1,

    'filters': {        
        'debug_mode_true': {
            '()': DebugModeTrueFilter,            
        },
        'debug_mode_false': {
            '()': DebugModeFalseFilter,            
        },
    }, 

    'formatters': {
        'file_formater': {
            'format': '%(asctime)s - %(filename)s[LINE:%(lineno)-5d] - %(levelname)-8s # %(message)s',
        },
        'console_formater': {
            'format': '%(asctime)s - %(filename)s - %(levelname)-8s # %(message)s',
            'datefmt': '%H:%M:%S',
        },

        'simple': {
            'format': '%(asctime)s - %(levelname)-8s # %(message)s',
        },
    },    

    'handlers': {
        'debug_mode_console': {
            'level': 'DEBUG',            
            'class': 'logging.StreamHandler',
            'formatter': 'console_formater',            
            'filters': ['debug_mode_true'],
        },

        'production_mode_console': {
            'level': 'INFO',            
            'class': 'logging.StreamHandler',
            'formatter': 'console_formater',
            'filters': ['debug_mode_false'],
        },

        'debug_mode_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': getenv('DEBUG_FILE_LOG', 'debug.log'),
            'maxBytes': 1024 * 1024 * 3,  # 5 MB
            'backupCount': 3,
            'formatter': 'file_formater',
            'filters': ['debug_mode_true'],
        },
        'production_mode_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': getenv('PRODUCTION_FILE_LOG', 'production.log'),
            'maxBytes': 1024 * 1024 * 7,  # 5 MB
            'backupCount': 7,
            'formatter': 'file_formater',           
            'filters': ['debug_mode_false'],
        }
    },

    'loggers': {
        '': {
            'handlers': ['debug_mode_console', 'production_mode_console', 'debug_mode_file', 'production_mode_file'],
            'level': "DEBUG",
            },
    }
}

logging.config.dictConfig(dictLogConfig)
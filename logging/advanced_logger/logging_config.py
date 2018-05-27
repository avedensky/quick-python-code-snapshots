#!/usr/bin/env python
#coding: utf-8

# Этот модуль настраивает логирование
#
# Для использования, просто импортировать этот модуль в main модуле, ранее импорта: import logging 
# т.е.:
# import logging_config
# import logging
#
# Далее, в любом модуле нашей программы:
# import logging
# logger = logging.getLogger(__name__)
#
# Используем:
# logger.debug('Debug Message')
# logger.info('Info Message')
#
#
# Логирование предусматривает два режима работы debug и production.
# Для их переключения следует использовать переменную окружения DEBUG.
# Из кода можно определить переменную окружения так:
# import os
# os.environ['DEBUG'] = 'True'
#
# В DEBUG = True :
# Сообщения будут писаться в файл debug.log (по умолчанию) 
# и выводиться в консоль все сообщения уровня debug и выше.
# 
# В DEBUG = False :
# Сообщения будут писаться в файл production.log (по умолчанию) 
# и выводиться в консоль все сообщения от уровня info и выше.
#
# Используя переменные окружения DEBUG_FILE_LOG, PRODUCTION_FILE_LOG, 
# можно задать имена лог файлов, по умолчанию debug.log и production.log.
# 
# В лог файлы пишется расширенная информация, в консоль - краткая
# Также присутствует функция ротации логов:
#
# Ротация управляется классами ZipRotatingFileHandlerBySize, ZipRotatingFileHandlerByTime и RotatingFileHandler
# Которые можно включить ниже, в конфиге, соответствующие параметры должы быть раскомментированы.
#
# RotatingFileHandler - обычная ротация логов без архивирования
#
# ZipRotatingFileHandlerBySize - при достижении определенного размера, лог файл записывается в архив
#
# ZipRotatingFileHandlerByTime - в архив сбрасывается лог файл, каждые:
# сеунду ('when':'s')
# минуту ('when':'m')
# час ('when':'h')
# день ('when':'d')
#
# Название файла - архива может быть задано переменной окружения ARHIVE_NANE или log.zip, по умолчанию.
import logging
import logging.config
from os import getenv, remove
import zipfile
import datetime
import os.path


class DebugModeTrueFilter(logging.Filter):
    def filter(self, record):
        debug_mode = getenv('DEBUG', 'true').lower()
        return True if debug_mode == 'true' else False
            

class DebugModeFalseFilter(logging.Filter):
    def filter(self, record):
        debug_mode = getenv('DEBUG', 'true').lower()
        return True if debug_mode == 'false' else False


class ZipRotatingFileHandlerByTime(logging.handlers.TimedRotatingFileHandler):
    def __init__(self, arhive_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arhive_name = arhive_name

    def rotate(self, source, dest):        
        path, filename = os.path.split(source)

        current_dt = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        new_log_name = '{}_{}'.format(current_dt, filename)
        new_log_path = os.path.join(path, new_log_name)

        try:
            os.rename (source, new_log_path)

            with zipfile.ZipFile(self.arhive_name, 'a', zipfile.ZIP_LZMA) as myzip:
                myzip.write(new_log_path, new_log_name)

            remove(new_log_path)
        except (PermissionError, FileNotFoundError, OSError) as e:            
            super().rotate(source, dest)


class ZipRotatingFileHandlerBySize(logging.handlers.RotatingFileHandler):
    def __init__(self, arhive_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arhive_name = arhive_name

    def rotate(self, source, dest):        
        path, filename = os.path.split(source)

        current_dt = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        new_log_name = '{}_{}'.format(current_dt, filename)
        new_log_path = os.path.join(path, new_log_name)
            
        try:
            os.rename (source, new_log_path)

            with zipfile.ZipFile(self.arhive_name, 'a', zipfile.ZIP_LZMA) as myzip:
                myzip.write(new_log_path, new_log_name)

            remove(new_log_path)
        except (PermissionError, FileNotFoundError, OSError) as e:            
            super().rotate(source, dest)


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
            'format': '%(asctime)s.%(msecs)03d %(filename)s %(levelname)-8s # %(message)s',
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
            #'class': 'logging.handlers.RotatingFileHandler',
            #'class': 'logging_config.ZipRotatingFileHandlerBySize',
            'class': 'logging_config.ZipRotatingFileHandlerByTime',
            'filename': getenv('DEBUG_FILE_LOG', 'debug.log'),
            #'maxBytes': 1500,                                      # !NEED define - if 'class': 'RotatingFileHandler' or 'ZipRotatingFileHandlerBySize'
            'backupCount': 1,
            'formatter': 'file_formater',
            'filters': ['debug_mode_true'],
            'arhive_name': getenv('ARHIVE_NANE', 'logs.zip'),       # !NEED define - if 'class': 'ZipRotatingFileHandler...'
            'when':'m',                                             # !NEED define - if 'class': 'ZipRotatingFileHandlerByTime' values: s, m, h, d
        },

        'production_mode_file': {
            'level': 'INFO',
            #'class': 'logging.handlers.RotatingFileHandler',
            #'class': 'logging_config.ZipRotatingFileHandlerBySize',
            'class': 'logging_config.ZipRotatingFileHandlerByTime',
            'filename': getenv('PRODUCTION_FILE_LOG', 'production.log'),
            #'maxBytes': 1024 * 1024 * 7,  # 7 MB                    # !NEED define - if 'class': 'RotatingFileHandler' or 'ZipRotatingFileHandlerBySize'
            'backupCount': 1,
            'formatter': 'file_formater',           
            'filters': ['debug_mode_false'],
            'arhive_name': getenv('ARHIVE_NANE', 'logs.zip'),        # !NEED define - if 'class': 'ZipRotatingFileHandler...'
            'when':'m',                                              # !NEED define - if 'class': 'ZipRotatingFileHandlerByTime' values: s, m, h, d
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
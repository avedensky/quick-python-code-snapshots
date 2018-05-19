#!/usr/bin/env python
#coding: utf-8
import os
os.environ['DEBUG'] = 'True'

import logging_config
import logging
import other_my_module

logger = logging.getLogger(__name__)

logger.debug('The Main')
logger.info('The Main')
other_my_module.foo()

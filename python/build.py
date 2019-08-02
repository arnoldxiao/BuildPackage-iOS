#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# @Author: xiaochenghua
# @Date: 2019/08/01

import coloredlogs
import logging
import os

from utils import Utils


class Build(object):

    logger = logging.getLogger(__name__)
    coloredlogs.install(level='DEBUG', logger=logger)

    def __init__(self, configuration='Debug'):
        self.__configuration = configuration

    def pre_clean(self):
        # path =
        if not os.path.exists(Utils.code_path()):
            logging.error('%s is not exists!' % Utils.code_path())
            exit()

        os.system('cd %s;xcodebuild clean -project Pods/Pods.xcodeproj -alltargets -sdk iphoneos -configuration %s' % (Utils.code_path(), self.__configuration))

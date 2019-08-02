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

    def __init__(self, server=None, configuration='Debug'):
        self.__server = server
        self.__configuration = configuration
        self.__utils = Utils(self.__server, self.__configuration)

    def pre_clean(self):
        # path =
        if not os.path.exists(Utils.code_path()):
            logging.error('%s is not exists!' % Utils.code_path())
            exit()

        os.system('cd %s;xcodebuild clean -project Pods/Pods.xcodeproj -alltargets -sdk iphoneos -configuration %s' %
                  (Utils.code_path(), self.__configuration))

    def run(self):
        self.__clean()
        self.__archive()
        self.__export()

    def __clean(self):
        os.system('cd %s;xcodebuild clean -workspace %s -scheme %s -sdk iphoneos -configuration %s' %
                  (self.__utils.src_path(), Utils.project_xcworkspace_file(), Utils.scheme_name(), self.__configuration))

    def __archive(self):
        os.system('cd %s;xcodebuild archive -workspace %s -scheme %s -configuration %s -archivePath build/%s.xcarchive' %
                  (self.__utils.src_path(), Utils.project_xcworkspace_file(), Utils.scheme_name(), self.__configuration, Utils.project_name()))

    def __export(self):
        export_options = os.path.join(os.getenv('HOME'), '*/ExportOptions.plist')
        os.system('cd %s;xcodebuild -exportArchive -archivePath build/%s.xcarchive -exportPath %s -exportOptionsPlist %s' %
                  (self.__utils.src_path(), Utils.project_name(), self.__utils.ipa_path(), export_options))

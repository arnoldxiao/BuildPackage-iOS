#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# @Author: xiaochenghua
# @Date: 2019/07/31

import os
import re
import shutil

number_regex = r'(\d{1,2}|1\d{2}|25[0-5]|2[0-4]\d)'
port_regex = r'(\d{1,4}|[1-5]\d{4}|6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3})'
ip_regex = r'^((%s\.){3}%s(:%s)?)$' % (number_regex, number_regex, port_regex)


class Utils(object):

    def __init__(self, server, configuration, version=None):
        self.__server = server
        self.__configuration = configuration
        self.__version = version

    def server_name(self):
        return self.__server.split(':')[0]

    def server_ip(self):
        if re.match(ip_regex, self.__server) is not None:
            return self.server_name()
        return None

    def __server_short_name(self):
        if self.server_ip() is None:
            return self.server_name().split('.')[1]
        return self.server_name().split('.')[3]

    def server_path(self):
        return Utils.make_return(os.path.join(Utils.workspace(), self.server_name()))

    def version_id(self):
        if self.__version is None:
            return None
        return self.__version.split('-')[0]

    def build_id(self):
        if self.__version is None:
            return None
        return self.__version.split('-')[1]

    """
    只返回暂时先不创建目录，否则拷贝代码时会报错
    """
    def src_path(self):
        return os.path.join(self.server_path(), 'src')

    # def build_path(self):
    #     return os.path.join(self.server_path(), 'build')

    def ipa_path(self):
        return Utils.make_return(os.path.join(self.server_path(), 'ipa'))

    def copy_code(self):
        shutil.copytree(Utils.code_path(), self.src_path())

    def config_path(self):
        if self.__configuration == 'Debug':
            return os.path.join(self.src_path(), os.path.join(Utils.project_name(), 'Config/Debug.xcconfig'))
        elif self.__configuration == 'Release':
            return os.path.join(self.src_path(), os.path.join(Utils.project_name(), 'Config/Release.xcconfig'))
        else:
            return None

    def info_plist_path(self):
        return os.path.join(self.src_path(), os.path.join(Utils.project_name(), 'Info.plist'))

    def app_display_name(self):
        return '%s.%s' % (self.__configuration, self.__server_short_name())

    @staticmethod
    def project_name():
        return 'BuildPackage-Example'

    @staticmethod
    def scheme_name():
        return Utils.project_name()

    @staticmethod
    def project_xcworkspace_file():
        return Utils.project_name() + '.xcworkspace'

    @staticmethod
    def desktop():
        return Utils.make_return(os.path.join(os.getenv('HOME'), 'Desktop'))

    @staticmethod
    def workspace():
        return Utils.make_return(os.path.join(Utils.desktop(), 'BuildPackageWorkspace'))

    @staticmethod
    def code_path():
        return Utils.make_return(os.path.join(Utils.workspace(), Utils.project_name()))

    """
    给定一个path，如果path不存在，则递归创建，并原样返回path
    """
    @staticmethod
    def make_return(path):
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    @staticmethod
    def remove_workspace():
        shutil.rmtree(Utils.workspace())


if __name__ == "__main__":
    pass
    # print(Utils.return_path(os.path.join(Utils.desktop(), 'a/b/c/d')))
    # shutil.copytree(os.path.join(Utils.desktop(), 'a'), os.path.join(Utils.desktop(), 'b'))

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

    def __init__(self, server):
        self.__server = server

    def server_ip(self):
        if re.match(ip_regex, self.__server) is not None:
            return self.__server.split(':')[0]
        return None

    def __server_short_name(self):
        if self.server_ip() is None:
            return self.__server.split(':')[0].split('.')[1]
        return self.__server.split(':')[0].split('.')[3]

    def server_path(self):
        return Utils.return_path(os.path.join(Utils.workspace_root_path(), self.__server_short_name()))

    def src_path(self):
        # return Utils.return_path(os.path.join(self.server_path(), 'src'))
        return os.path.join(self.server_path(), 'src')

    def build_path(self):
        return Utils.return_path(os.path.join(self.server_path(), 'build'))

    def ipa_path(self):
        return Utils.return_path(os.path.join(self.server_path(), 'ipa'))

    def copy_code(self):
        shutil.copytree(Utils.workspace_project_path(), self.src_path())

    @staticmethod
    def project_name():
        return 'BuildPackage-Example'

    @staticmethod
    def project_path():
        # /Users/xiaochenghua/BuildPackage-iOS/BuildPackage-Example
        root_path = os.path.join(os.getenv('HOME'), 'BuildPackage-iOS')
        return Utils.return_path(os.path.join(root_path, Utils.project_name()))

    @staticmethod
    def project_code_path():
        # /Users/xiaochenghua/BuildPackage-iOS/BuildPackage-Example/BuildPackage-Example
        return Utils.return_path(os.path.join(Utils.project_path(), Utils.project_name()))

    @staticmethod
    def desktop():
        return Utils.return_path(os.path.join(os.getenv('HOME'), 'Desktop'))

    @staticmethod
    def workspace_root_path():
        return Utils.return_path(os.path.join(Utils.desktop(), 'BuildPackageWorkspace'))

    @staticmethod
    def workspace_project_path():
        return Utils.return_path(os.path.join(Utils.workspace_root_path(), Utils.project_name()))

    """
    给定一个path，如果path不存在，则递归创建，并原样返回path
    """
    @staticmethod
    def return_path(path):
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    @staticmethod
    def rm_workspace_path():
        shutil.rmtree(Utils.workspace_root_path())


if __name__ == "__main__":
    pass
    # print(Utils.return_path(os.path.join(Utils.desktop(), 'a/b/c/d')))
    # shutil.copytree(os.path.join(Utils.desktop(), 'a'), os.path.join(Utils.desktop(), 'b'))

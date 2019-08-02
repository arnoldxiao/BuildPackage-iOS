#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# @Author: xiaochenghua
# @Date: 2019/08/01

from utils import Utils


class File(object):

    def __init__(self, server, configuration, version=None):
        self.__server = server
        self.__utils = Utils(self.__server, configuration, version)

    def modify_all(self):
        self.__modify_config()
        self.__modify_info()

    def __modify_config(self):
        path = self.__utils.config_path()
        if path is None:
            return

        # 读取
        f = open(path, 'r')
        lines = f.readlines()
        f.close()

        # 写入
        f = open(path, 'w')

        url_suffix = 'API_URL'
        url_full = '%s = @\"https:/$()/%s\"\n' % (url_suffix, self.__server)

        for line in lines:
            if not line.startswith(url_suffix):
                f.write(line)
                continue
            if line != url_full:
                f.write(url_full)
        f.close()

    def __modify_info(self):
        path = self.__utils.info_plist_path()

        # 读取
        f = open(path, 'r')
        lines = f.readlines()
        f.close()

        # 寻找 CFBundleDisplayName/CFBundleShortVersionString/CFBundleVersion 所在行号
        head_display_name = -1
        head_version = -1
        head_build_version = -1

        # 写入, 分别修改App显示名、versionId、buildId
        f = open(path, 'w')
        for i in range(len(lines)):
            if lines[i].find('<key>CFBundleDisplayName</key>') != -1:
                head_display_name = i + 1
            elif lines[i].find('<key>CFBundleShortVersionString</key>') != -1:
                head_version = i + 1
            elif lines[i].find('<key>CFBundleVersion</key>') != -1:
                head_build_version = i + 1
            elif i == head_display_name:
                lines[i] = '\t<string>%s</string>' % self.__utils.app_display_name()
            elif i == head_version:
                lines[i] = '\t<string>%s</string>' % self.__utils.version_id()
            elif i == head_build_version:
                lines[i] = '\t<string>%s</string>' % self.__utils.build_id()
            f.write(lines[i])
        f.close()

    @staticmethod
    def __read_lines(path):
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        return lines

    @staticmethod
    def __write_lines(path, lines):
        f = open(path, 'w')
        for line in lines:
            f.write(line)
        f.close()


if __name__ == '__main__':
    File('192.168.1.19', 'Debug').modify_all()

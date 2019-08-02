#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# @Author: xiaochenghua
# @Date: 2019/08/01

from utils import Utils


class File(object):

    def __init__(self, server, configuration):
        self.__server = server
        self.__configuration = configuration

    def modify_all(self):
        self.__modify_config()
        self.__modify_info()

    def __modify_config(self):
        path = Utils(self.__server).config_path(self.__configuration)
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
        path = Utils(self.__server).info_plist_path()

        # 读取
        f = open(path, 'r')
        lines = f.readlines()
        f.close()

        # 寻找CFBundleDisplayName所在行号
        head = -1

        # 写入
        f = open(path, 'w')
        for i in range(len(lines)):
            # CFBundleDisplayName
            if lines[i].find('<key>CFBundleDisplayName</key>') != -1:
                f.write(lines[i])
                head = i + 1
                continue
            elif i == head:
                f.write('\t<string>%s</string>' % Utils(self.__server).app_display_name(self.__configuration))
            else:
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

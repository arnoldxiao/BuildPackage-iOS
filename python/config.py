#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# @Author: xiaochenghua
# @Date: 2019/08/02

import os

from configparser import ConfigParser


class Config(object):

    def __init__(self):
        parser = ConfigParser()
        parser.read(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'config.ini'))
        self.configParser = parser

    def test(self):
        print(self.configParser.get('DEFAULT', 'server'))


if __name__ == '__main__':
    Config().test()

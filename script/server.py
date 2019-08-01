#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# @Author: xiaochenghua
# @Date: 2019/08/01

import re

number_regex = r'(\d{1,2}|1\d{2}|25[0-5]|2[0-4]\d)'
port_regex = r'(\d{1,4}|[1-5]\d{4}|6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3})'

ip_regex = r'^((%s\.){3}%s(:%s)?)$' % (number_regex, number_regex, port_regex)
domain_regex = r'^(m.xiaochenghua.com(:%s)?)$' % port_regex
server_regex = r'%s|%s' % (ip_regex, domain_regex)


class Server(object):

    def __init__(self, string):
        self.__string = string

    def servers(self):
        if self.__string is None:
            return
        formats = set()
        # Jenkins定时任务会将crontab命令中的\n转换成\\n，这里需要替换回去\n
        servers = self.__string.replace('\\n', '\n').splitlines()
        for server in servers:
            # 空字符串需要过滤掉
            if len(server.strip()) == 0:
                continue
            # 不匹配正则表达式需要过滤掉
            if re.match(server_regex, server) is None:
                continue
            formats.add(server)
        return list(formats)

#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# @Author: xiaochenghua
# @Date: 2019/08/01

# 这里可以换成企业邮箱域名
email_domain = '163.com'


class Recipient(object):

    def __init__(self, string):
        self.__string = string

    def recipients(self):
        formats = set()
        # Jenkins定时任务会将crontab命令中的\n转换成\\n，这里需要替换回去\n
        recipients = self.__string.replace('\\n', '\n').splitlines()

        for recipient in recipients:
            if not recipient.strip().endswith('@' + email_domain):
                continue
            formats.add(recipient.strip())
        return list(formats)

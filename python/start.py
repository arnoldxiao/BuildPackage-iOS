#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# @Author: xiaochenghua
# @Date: 2019/07/31

import os
import time
import coloredlogs
import logging

from server import Server
from recipient import Recipient
from code import Code
from build import Build
from utils import Utils
from file import File


class Start(object):

    default_configuration = 'Debug'
    default_version = '1.1.0-0801'
    default_server = '192.168.1.19'
    default_recipient_to = 'arnoldxiao@163.com'
    default_recipient_cc = ''

    user_configuration = os.getenv('configuration')
    user_version = os.getenv('version')
    user_server = os.getenv('servers')
    user_recipient_to = os.getenv('recipients_to')
    user_recipient_cc = os.getenv('recipients_cc')

    configuration = user_configuration if user_configuration is not None else default_configuration
    version = user_version if user_version is not None else default_version
    servers = Server(user_server if user_server is not None else default_server).servers()
    recipient_to = Recipient(user_recipient_to if user_recipient_to is not None else default_recipient_to).recipients()
    recipient_cc = Recipient(user_recipient_cc if user_recipient_cc is not None else default_recipient_cc).recipients()


if __name__ == '__main__':
    """
    打包程序
    """

    logger = logging.getLogger(__name__)
    coloredlogs.install(level='DEBUG', logger=logger)

    if len(Start.servers) == 0:
        logger.error('servers count is 0!')
        exit()

    begin_time = time.time()
    date_time = time.strftime('%Y%m%d%H%M', time.localtime(begin_time))

    Code(version=Start.version).clone()
    Build(configuration=Start.configuration).pre_clean()

    for server in Start.servers:
        Utils(server).copy_code()
        File(server).modify_all()



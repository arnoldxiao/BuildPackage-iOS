#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# @Author: xiaochenghua
# @Date: 2019/08/01

import coloredlogs
import logging

from git import Repo
from utils import Utils

repo = 'https://github.com/arnoldxiao/BuildPackage-Example.git'


class Code(object):

    logger = logging.getLogger(__name__)
    coloredlogs.install(level='DEBUG', logger=logger)

    def __init__(self, version=None):
        self.__version = version
        # self.__branch = 'BE/' + version if version is not None else 'master'

    def clone(self):
        if self.__version is None:
            logging.error('version is None!')
            exit()

        __branch = 'BE/' + self.__version
        Repo.clone_from(url=repo, to_path=Utils.workspace_project_path(), branch=__branch)


if __name__ == '__main__':
    Code(version='1.1.0-0801').clone()




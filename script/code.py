#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# @Author: xiaochenghua
# @Date: 2019/08/01

from git import Repo
from utils import Utils

repo = 'https://github.com/arnoldxiao/BuildPackage-iOS.git'


class Code(object):

    def __init__(self, version=None):
        self.__branch = 'YQ/' + version if version is not None else 'master'

    def clone(self):
        print('path: ' + Utils.workspace_project_path())
        print('branch: ' + self.__branch)
        Repo.clone_from(url=repo, to_path=Utils.workspace_project_path(), branch=self.__branch)


if __name__ == '__main__':
    Code(version='1.0.0').clone()




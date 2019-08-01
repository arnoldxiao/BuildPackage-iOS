#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# @Author: xiaochenghua
# @Date: 2019/07/31

import os
import shutil


class Utils(object):

    def __init__(self):
        pass

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
    print(Utils.return_path(os.path.join(Utils.desktop(), 'a/b/c/d')))

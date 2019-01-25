#!/usr/bin/env Python
# -*- coding:utf-8 -*-


import zipfile
import os
import re


def zip_all(from_dir, target_zip):
    """把目录中的每个文件写入zip文件"""
    my_zip = zipfile.ZipFile(target_zip, 'w')
    # 遍历目录内的所有目录和文件，返回列表
    for root, dir, files in os.walk(from_dir):
        # 遍历文件
        for file in files:
            # 根路径+文件名
            filename = os.path.join(root, file)
            print(filename)
            # 循环写入文件 可自定义
            if re_filename.match(filename):
                my_zip.write(filename, compress_type=zipfile.ZIP_DEFLATED)

    # 关闭
    my_zip.close()


# 需要压缩的目录, 可自定义
from_dir = r'D:\360安全浏览器下载'
# 需要新建的压缩文件名， 可自定义
target_zip = 'project.zip'
# 需要备份的文件名 正则
re_filename = re.compile('(.*pdf$)|(.*doc$)|(.*xlsx$)')
# 开始执行
zip_all(from_dir, target_zip)

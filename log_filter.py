#!/usr/bin/env Python
# -*- coding:utf-8 -*-


import os
import re


def readStaus(log_path):
    with open(log_path) as f:
        for line in f:
            line_status = line.split(' ')[8]
            if line_status == '200':
                status_dic[line_status] = status_dic.get(line_status, 0) + 1
    print(status_dic)


def readIp(log_path):
    with open(log_path) as f:
        for line in f:
            match = re_ip.match(line)
            if match:
                ip = match.group()
                ip_dic[ip] = ip_dic.get(ip, 0) + 1
    for k, v in ip_dic.items():
        print(k, ":", v)

# 不使用readlines()返回整个列表，直接返回生成器generator, 节省内存
# def readData(log_path):
#     with open(log_path) as f:
#           return f.readlines()


base_dir = 'log_data'
log_path = os.path.join(base_dir, 'access.log')
re_ip = re.compile(r'((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)')
ip_dic = {}
status_dic = {}
# log_data = readData(log_path)
readStaus(log_path)
readIp(log_path)
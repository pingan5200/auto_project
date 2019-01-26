#!/usr/bin/env Python
# -*- coding:utf-8 -*-


import configparser
import os


class ConfigAdmin:
    """配置文件的增删改查"""
    def __init__(self, config_path, config):
        # 初始化配置文件路径和模块存储对象
        self.config_path = config_path
        self.config = config

    def write_config(self, data):
        # 写入数据
        for k, v in data.items():
            self.config[k] = v
        with open(self.config_path, 'w') as f:
            self.config.write(f)
        print('write success')

    def read_config(self, section, option, config_path):
        # 读option对应的值
        self.config.read(config_path)
        print(option, "=", self.config[section][option])
        print('read success')

    def add_config(self, section, option, value):
        # 增加数据
        try:
            if self.config.has_section(section):
                print(f'已经有{section}了')
            else:
                self.config.read(self.config_path)
                self.config.add_section(section)
                self.config.set(section, option, value)
                with open(config_path, 'w') as f:
                    config.write(f)
                print('add success')
        except Exception as e:
            print(e)

    def update_config(self, section, option, value, config_path):
        # 修改section的数据
        self.config.read(self.config_path)
        self.config[section][option] = value
        with open(config_path, 'w') as f:
            config.write(f)
        print('update success')


# 字典嵌套字典 可自定义
data = {'DEFAULT': {'basedir': base_dir,
                    'user': 'admin',
                    'passwd': '123456'
        },
        'VIP': {'basedir': base_dir,
                'user': 'lcs',
                'passwd': '123456'
        }
}
# windows根目录，linux就是反/ 可自定义
base_dir = 'config'
config = configparser.ConfigParser()
config_path = os.path.join(base_dir, 'allocation.ini')
c = ConfigAdmin(config_path, config)
# 可自定义
# c.write_config(data)
# 可自定义
# c.read_config('VIP', 'passwd', config_path)
# 可自定义
# c.add_config('SECURE', 'card', '42000980890')
# c.update_config('DEFAULT', 'basedir', r'D:\test', config_path)
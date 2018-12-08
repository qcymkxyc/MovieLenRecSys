#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    18-12-8 下午12:16
@Author:  qcymkxyc
@File: mongo_helper.py
@Software: PyCharm
"""
import pymongo
from config import conf


def create_mongo_db(config_name):
    """创建MongoDB的DB

    :param config_name: str
        配置名
    :return: mongo.database
        mongodb的数据库
    """
    current_config = conf.config[config_name]
    client = pymongo.MongoClient(current_config.MONGO_HOST, current_config.MONGO_POST)
    db = client[current_config.MONGO_DB]

    return db

#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: conf.py.py
 @time: 2018/12/3 18:45

"""


class Config:
    # 数据库设置
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True

    username = "root"
    pw = 123456
    host = "47.94.80.98"
    database = "movielen"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{pw}@{host}/{database}".format(
        username=username,
        pw=pw,
        host=host,
        database=database)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        # from logging.handlers import


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}

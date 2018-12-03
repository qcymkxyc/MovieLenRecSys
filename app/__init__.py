#!usr/bin/env python 
# -*- coding:utf-8 _*-  
""" 
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: __init__.py.py
 @time: 2018/12/3 18:35
 
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

from config import conf

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()


def create_app(config_name):
    """创建程序

    :param config_name: str
        配置模式
    :return: flask.Flask
        应用
    """
    app = Flask(__name__)
    app.config.from_object(conf.config[config_name])
    conf.config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)

    from .main import main
    app.register_blueprint(main)

    return app


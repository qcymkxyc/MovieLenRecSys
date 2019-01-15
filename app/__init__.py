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
from app.recommend import mongo_helper

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
mongo_db = None


def create_app(config_name):
    """创建程序

    :param config_name: str
        配置模式
    :return: flask.Flask
        应用
    """
    global mongo_db

    app = Flask(__name__)
    app.config.from_object(conf.config[config_name])
    conf.config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)

    mongo_db = mongo_helper.create_mongo_db(config_name)

    # 蓝图
    from .main import main
    app.register_blueprint(main)
    from .movie import movie
    app.register_blueprint(movie,url_prefix="/movies")

    return app


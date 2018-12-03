#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: __init__.py.py
 @time: 2018/12/3 18:44

"""
from flask import blueprints

main = blueprints.Blueprint("main", __name__)
from . import views, errors, forms

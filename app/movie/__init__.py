#!usr/bin/env python 
# -*- coding:utf-8 _*-  
""" 
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: __init__.py.py
 @time: 2018/12/3 18:43
 
"""
from flask import blueprints

movie = blueprints.Blueprint("movie",__name__)

from app.movie import errors, forms, views
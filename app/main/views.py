#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: views.py
 @time: 2018/12/3 18:44

"""
from . import main
from flask import render_template, current_app


@main.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

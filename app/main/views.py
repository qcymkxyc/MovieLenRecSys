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
from flask import render_template,current_app
from app.models import Movie
from app.rec import rec


@main.route("/", methods=["GET", "POST"])
def index():
    # 热门电影
    if not hasattr(current_app,"popular_movies"):
        popular_movies = rec.get_popular_movies(current_app.config["POPULAR_TOP_N"])
        current_app.popular_movies = popular_movies

    return render_template("index.html",popular_movies = current_app.popular_movies)

#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: views.py
 @time: 2018/12/3 18:43

"""
from flask import render_template, request
from . import movie as movie_blueprint
from ..models import Movie, Tag, Rating, UserTag


@movie_blueprint.route("/movie/<movie_id>", methods=["GET", "POST"])
def find_movie(movie_id):
    movie = Movie.query.filter_by(movie_id=movie_id).first()
    return render_template("movie_detail.html", movie=movie)


@movie_blueprint.route("/tag/<tag_id>", methods=["GET"])
def find_tag(tag_id):
    # tag = Tag.query.filter_by(tag_id=tag_id).first()
    return render_template("index.html")


@movie_blueprint.route("find_rating", methods=["GET"])
def find_rating():
    user_id = request.args.get("userId", type=int)
    movie_id = request.args.get("movieId", type=int)

    filters = {"user_id": user_id, "movie_id": movie_id}
    rating = Rating.query.filter_by(**filters).first()
    return render_template("index.html")


@movie_blueprint.route("find_user_tag", methods=["GET"])
def find_user_tag():
    user_id = request.args.get("userId", type=int)
    movie_id = request.args.get("movieId", type=int)

    user_tag = UserTag.query.filter_by(user_id=user_id, movie_id=movie_id).first()

    return render_template("index.html")

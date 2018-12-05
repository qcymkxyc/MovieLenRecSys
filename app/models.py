#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: models.py
 @time: 2018/12/3 21:24

"""
from app import db


class Movie(db.Model):
    __tablename__ = "t_movies"

    movie_id = db.Column("movieId", db.Integer, primary_key=True)
    title = db.Column("title", db.String)
    genres = db.Column("genres", db.String)

    pic_paths = db.Column("pictures", db.String)


class Tag(db.Model):
    __tablename__ = "t_genome-tags"

    tag_id = db.Column("tagId", db.Integer,primary_key=True)
    tag_name = db.Column("tag", db.String)


class Links(db.Model):
    __tablename__ = "t_links"

    movie_id = db.Column("movieId", db.Integer,primary_key=True)
    imdb_id = db.Column("imdbId", db.Integer)
    tmdb_id = db.Column("tmdbId", db.Integer)


class Rating(db.Model):
    __tablename__ = "t_ratings"

    user_id = db.Column("userId", db.Integer, primary_key=True)
    movie_id = db.Column("movieId", db.Integer, primary_key=True)
    rating = db.Column("rating", db.FLOAT)
    timestamp = db.Column("timestamp", db.BigInteger)


class UserTag(db.Model):
    """用户打标签"""
    __tablename__ = "t_tags"

    id = db.Column("id",db.Integer,autoincrement=True,primary_key=True)
    user_id = db.Column("userId",db.Integer)
    movie_id = db.Column("movieId",db.Integer)
    tag_name = db.Column("tag", db.String,)
    timestamp = db.Column("timestamp",db.BigInteger)




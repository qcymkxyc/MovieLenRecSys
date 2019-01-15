#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    18-12-8 下午1:11
@Author:  qcymkxyc
@File: most_popular.py
@Software: PyCharm
"""
from app.models import Rating, Movie
from flask import current_app
from operator import itemgetter
import app


def create_movie_popularity():
    """计算电影的流行度，并存入mongodb"""
    print("开始统计流行度...")

    page_limit = 50
    current_page = 1
    rating_dict = dict()

    while True:
        rating_pagnate = Rating.query.paginate(page=current_page, per_page=page_limit)
        ratings = rating_pagnate.items
        for single_rating in ratings:
            rating_dict.setdefault(single_rating.movie_id,0)
            rating_dict[single_rating.movie_id] += 1

        # 效率考虑，取前100页
        # if current_page == 100:
        #     break

        if rating_pagnate.has_next:
            current_page = current_page + 1
        else:
            break

    # 加入mongoDB数据库
    top_movies = sorted(rating_dict.items(), key=itemgetter(1), reverse=True)
    # 转化为list形式
    top_movie_list = list()
    for movie_id, count in top_movies:
        temp_movie = dict()
        temp_movie["movieID"] = movie_id
        temp_movie["popularity"] = count
        top_movie_list.append(temp_movie)

    mongo_movie_popularity = app.mongo_db.movie_popularity
    mongo_movie_popularity.insert_many(top_movie_list)


def get_popular_movies(top_n=None):
    """返回流行电影

    :param top_n: int
        前多少个(None表示取出collection中的所有)
    :return: list(Movie)
        流行电影的list
    """
    # 流行电影查询
    popular_movies_collection_name = current_app.config["POPULAR_MOVIE_COLLECTION"]
    popular_movies_collection = app.mongo_db[popular_movies_collection_name]
    # 如果没有建立流行电影的collection，则建立一个
    if popular_movies_collection.count() == 0:
        movie_popularity_collection_name = current_app.config["MOVIE_POPULARITY_COLLECTION"]
        popular_movies_n = current_app.config["POPULAR_MOVIE_N"]
        popular_movies = app.mongo_db[movie_popularity_collection_name].\
            find().sort("popularity", -1).\
            limit(popular_movies_n)

        popular_movies = [movie for movie in popular_movies]
        popular_movies_collection.insert_many(popular_movies)
    # 有则直接取出
    else:
        popular_movies = popular_movies_collection.find()

    # 转换为Movie类
    popular_movies = sorted(popular_movies, key=lambda x: x["popularity"], reverse=True)[:top_n]
    popular_movie_entrys = list()
    for popular_movie in popular_movies:
        movie_id = popular_movie["movieID"]
        movie = Movie.query.filter_by(movie_id=movie_id).first()
        popular_movie_entrys.append(movie)

    return popular_movie_entrys


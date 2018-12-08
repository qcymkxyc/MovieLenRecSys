#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    18-12-8 下午1:11
@Author:  qcymkxyc
@File: rec.py
@Software: PyCharm
"""
from app.models import Rating, Movie
from operator import itemgetter
import app


def create_popular_movies(top_n=10):
    """热门电影

    :param top_n: int
        推荐个数
    :return: Movie
    """
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
        if current_page == 100:
            break

        if rating_pagnate.has_next:
            current_page = current_page + 1
        else:
            break

    # 加入mongoDB数据库
    top_movies = sorted(rating_dict.items(), key=itemgetter(1), reverse=True)[:top_n]
    # 转化为list形式
    top_movie_list = list()
    for movie_id, count in top_movies:
        temp_movie = dict()
        temp_movie["movieID"] = movie_id
        temp_movie["popularity"] = count
        top_movie_list.append(temp_movie)

    mongo_popular_movie = app.mongo_db.popular_movies
    mongo_popular_movie.insert_many(top_movie_list)


def get_popular_movies(top_n):
    """返回流行电影

    :param top_n: int
        前多少个
    :return: list(Movie)
        流行电影的list
    """
    popular_movies = app.mongo_db.popular_movies.find()
    popular_movies = sorted(popular_movies, key=lambda x: x["movieID"], reverse=True)[:top_n]

    popular_movie_entrys = list()
    for popular_movie in popular_movies:
        movie_id = popular_movie["movieID"]
        movie = Movie.query.filter_by(movie_id=movie_id).first()
        popular_movie_entrys.append(movie)

    return popular_movie_entrys


#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: tool.py
 @time: 2018/12/4 13:22

"""
import requests
from bs4 import BeautifulSoup
from app import create_app
from app import db
from app.models import Movie
import json

app = create_app("default")
app_ctx = app.app_context()
app_ctx.push()


def add_pic_path():
    """添加图片路径"""
    movies = Movie.query.all()
    for i, movie in enumerate(movies):
        print("正在爬取第{}个图片".format(i))
        movie_id = movie.movie_id
        movie_json = crawl_by_movie_id(movie_id)
        # 如果爬取时出现异常
        if not movie_json:
            continue

        pics = movie_json["data"]["movieDetails"]["movie"]["backdropPaths"]
        pics = ["https://image.tmdb.org/t/p/original/" + pic for pic in pics]
        pics = ",".join(pics)
        movie.pic_paths = pics
    db.session.commit()


def add_description():
    movies = Movie.query.all()
    for i, movie in enumerate(movies):
        print("正在爬取电影:{}".format(movie.movie_id))


def crawl_by_movie_id(movie_id):
    """通过电影ID爬取电影图片

    :param movie_id: int
        电影ID
    :return: dict
        电影资料
    """
    movie_url = "https://movielens.org/api/movies/{movie_id}".format(
        movie_id=movie_id)
    cookies = dict(
        _ga="GA1.2.1071770607.1543829613",
        _gid="GA1.2.31642592.1543829613",
        ml4_session="a72da636d760bcc8ee851859e06c4fde6c3cc739_c467352e-70c4-4e00-a196-c16826b4e52c")
    try:
        response = requests.get(movie_url, cookies=cookies)
        movie_json = json.loads(response.text)
    except requests.exceptions.ConnectionError:
        return None
    return movie_json


if __name__ == '__main__':
    add_pic_path()
    # crawl_by_movie_id(1198)

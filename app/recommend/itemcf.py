#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    18-12-27 下午2:21
    @Author:  qcymkxyc
    @File: itemcf.py
    @Software: PyCharm


"""
from app.models import Rating
import math
from flask import current_app
import app


def create_itemcf_matrix():
    """创建item协同过滤矩阵"""

    page_limit = 50
    current_page = 1
    item_users = dict()
    item_matrix = dict()
    item_count = dict()

    # 建立倒排表
    while True:
        rating_pagnate = Rating.query.paginate(
            page=current_page, per_page=page_limit)
        ratings = rating_pagnate.items
        for single_rating in ratings:
            item_users.setdefault(single_rating.movie_id, set())
            item_users[single_rating.movie_id].add(single_rating.user_id)
            item_count.setdefault(single_rating.movie_id, 0)
            item_count[single_rating.movie_id] += 1

        if rating_pagnate.has_next:
            current_page = current_page + 1
        else:
            break

    # 计算相似性矩阵
    for item1, users1 in item_users.items():
        for item2, users2 in item_users.items():
            if item1 == item2:
                continue
            else:
                user_count = len(users1.intersection(users2))
                res = user_count / \
                    math.sqrt(item_count[item1] * item_count[item2])
                item_matrix.setdefault(item1, dict())
                item_matrix[item1][item2] = res

    # 保存至数据库中
    matrix_name = current_app.config["ITEMCF_MATRIX"]
    data_list = list()
    for item_id, item_sim in item_matrix.items():
        mongo_dict = dict()
        mongo_dict["itemId"] = item_id
        mongo_dict.setdefault("similarity", list())
        for item1, similarity in item_sim.items():
            mongo_dict["similarity"].append(
                {"ItemId": item1, "sim": similarity})

        data_list.append(mongo_dict)

    app.mongo_db[matrix_name].insert_many(data_list)

    return item_matrix




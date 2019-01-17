#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    18-12-27 下午2:51
    @Author:  qcymkxyc
    @File: itemcf_test.py
    @Software: PyCharm


"""
import unittest
from app.recommend import itemcf
import app


class ItemCFTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.create_app("default")
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()

    def test_create_itemcf_matrix(self):
        d = itemcf.create_itemcf_matrix()
        for item_id, item_sim in d.items():
            print(item_id, item_sim)

    def test_sim_item(self):
        item_id = 307
        itemcf.sim_item(307, 10)


if __name__ == '__main__':
    unittest.main()

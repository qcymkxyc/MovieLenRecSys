#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: manager.py
 @time: 2018/12/3 20:02

"""
import os

from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv("CONFIG") or "default")
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(db=db, app=app)


manager.add_command("shell", Shell(make_shell_context()))
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()

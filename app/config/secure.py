"""
    Created by 吴闻（gawinwu@163.com） on 2020-01-16.
"""

__author__ = '吴闻'

SQLALCHEMY_DATABASE_URI = \
    'mysql+cymysql://root:123456@localhost/flask_api'

SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'

SQLALCHEMY_TRACK_MODIFICATIONS = True

# 输出 SQLAlchemy 执行过程
SQLALCHEMY_ECHO = False

SQLALCHEMY_POOL_SIZE = 5

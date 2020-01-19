"""
    Created by 吴闻（gawinwu@163.com） on 2020-01-16.
"""

__author__ = '吴闻'

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.api_json_info import ServerError
from datetime import date


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        # print('------------------', type(o))
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder

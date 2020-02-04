"""
    Created by 吴闻（gawinwu@163.com） on 2020-01-16.
"""

__author__ = '吴闻'

from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('/get')
def get_book():
    return 'A book!'

"""
    Created by 吴闻（gawinwu@163.com） on 2020-01-17.
"""

__author__ = '吴闻'


class Gawin(object):
    name = 'gawin'
    age = 18

    def __init__(self):
        self.api = 'flask'

    def keys(self):
        return ['name', 'age']

    def __getitem__(self, item):
        return getattr(self, item)


o = Gawin()
# print(o['name'], o['age'], o['api'])
print(dict(o))

# Gawin().__dict__ #只可以取得实例变量


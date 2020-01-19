"""
    Created by 吴闻（gawinwu@163.com） on 2020-01-19.
"""

__author__ = '吴闻'

auth_scope_dict = {
    'SuperScope': 99,
    'AdminScope': 88,
    'UserScope': 1,
}


def get_scope(auth):
    auth_scope = 1
    try:
        auth_scope = list(auth_scope_dict.keys())[list(auth_scope_dict.values()).index(auth)]
    except IndexError:
        pass
    return auth_scope


class BaseScope:
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        # 通过set去重
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))

        return self


class UserScope(BaseScope):
    allow_api = ['v1.user+get_user', 'v1.user+delete_user']


class AdminScope(BaseScope):
    allow_api = ['v1.user+super_get_user']

    def __init__(self):
        self + UserScope()
        # print(self.allow_api)


class SuperScope(BaseScope):
    allow_module = ['v1.user']

    # forbidden = ['v1.user+get_user']

    def __init__(self):
        # self + UserScope() + AdminScope()
        # print(self.allow_api)
        pass


def is_in_scope(scope, endpoint):
    # 通过 globals 实现java的反射
    scope = globals()[scope]()

    # 切分红图模块名与函数名, 见 redprint.register
    splits = endpoint.split('+')
    red_name = splits[0]

    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False

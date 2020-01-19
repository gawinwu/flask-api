"""
    Created by 吴闻（gawinwu@163.com） on 2020-01-16.
"""

__author__ = '吴闻'

from flask import jsonify, g

from app.libs.api_json_info import DeleteSuccess
from app.libs.redprint import Redprint
from app.models.base_model import db
from app.libs.utils import format_time_long
from app.models.user_model import User
from app.libs.token_auth import auth

api = Redprint('user')


# 通过ID的获取用户账号信息
@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    user.create_time = format_time_long(user.create_time)
    return jsonify(user)


# 用户获取自己的账号信息
@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    user.create_time = format_time_long(user.create_time)
    return jsonify(user)


# 管理员删除用户
@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delete_user(uid):
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


# 用户主动注销账号
@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()

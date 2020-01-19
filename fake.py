"""
    Created by 吴闻（gawinwu@163.com） on 2020-01-18.
"""

__author__ = '吴闻'

from app import create_app
from app.models.base_model import db
from app.models.user_model import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建超级管理员账号
        user = User()
        user.nickname = 'SuperAdmin'
        user.password = '123456'
        user.email = '3195968@qq.com'
        user.auth = 99
        user.openid = None
        db.session.add(user)

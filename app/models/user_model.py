"""
    Created by 吴闻（gawinwu@163.com） on 2020-01-16.
"""

__author__ = '吴闻'

from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.api_json_info import NotFound, AuthFailed
from app.models.base_model import Base, db, MixinJSONSerializer
from app.libs.scope import get_scope
import datetime


class User(Base):
    id = Column(Integer, primary_key=True)
    mobile = Column(String(11), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    openid = Column(String(64), unique=False, nullable=True, default='')
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    def keys(self):
        return ['id', 'mobile', 'nickname', 'auth', 'create_time', 'openid']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_mobile(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.mobile = account
            user.password = secret
            db.session.add(user)

    # 验证用户账号密码登录
    @staticmethod
    def verify(mobile, password):
        user = User.query.filter_by(mobile=mobile).first()
        if not user:
            raise NotFound(msg='用户不存在')
        if not user.check_password(password):
            raise AuthFailed()
        scope = get_scope(user.auth)
        return {'uid': user.id, 'scope': scope}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

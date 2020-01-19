"""
    Created by 吴闻（gawinwu@163.com） on 2020-01-16.
"""

__author__ = '吴闻'

from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Regexp, Email, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user_model import User
from app.validators.base_form import BaseForm as Form


class ClientForm(Form):
    account = StringField(validators=[DataRequired(message='登录账号不可为空'), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            # 枚举转换
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='email 格式错误')
    ])
    secret = StringField(validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError(message="账号已存在")

    def validate_nickname(self, value):
        if User.query.filter_by(nickname=value.data).first():
            raise ValidationError(message="昵称已存在")

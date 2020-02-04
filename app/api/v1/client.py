"""
    Created by 吴闻（gawinwu@163.com） on 2020-01-16.
"""

__author__ = '吴闻'

from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.api_json_info import Success
from app.libs.redprint import Redprint
from app.models.user_model import User
from app.validators.client_form import ClientForm, UserMobileForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_MOBILE: __register_user_by_mobile,
        ClientTypeEnum.USER_MINA: __register_user_by_mina,
        ClientTypeEnum.USER_DOUYIN: __register_user_by_douyin,
    }
    promise[form.type.data]()
    return Success()


def __register_user_by_mobile():
    form = UserMobileForm().validate_for_api()
    User.register_by_mobile(form.nickname.data,
                           form.account.data,
                           form.secret.data)


def __register_user_by_mina():
    pass


def __register_user_by_douyin():
    pass

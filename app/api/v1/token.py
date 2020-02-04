"""
    Created by 吴闻（gawinwu@163.com） on 2020-01-17.
"""

__author__ = '吴闻'

from flask import current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user_model import User
from app.validators.client_form import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_MOBILE: User.verify,
        ClientTypeEnum.USER_MINA: __verify_user_by_mina,
        # ClientTypeEnum.USER_DOUYIN: __verify_user_by_douyin,
    }
    # 向 promise 传递验证参数, account, secret
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    # Token
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'],
                                form.type.data,
                                identity['scope'],
                                expiration)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None,
                        expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })


def __verify_user_by_mina(email, password):
    print('--------- __verify_user_by_mina ----------')
    return {'uid': 3}

"""
    Created by 吴闻（gawinwu@163.com） on 2020-01-16.
"""

__author__ = '吴闻'

from flask import request
from wtforms import Form

from app.libs.api_json_info import ParameterException


class BaseForm(Form):
    def __init__(self):
        data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # form errors
            raise ParameterException(msg=self.errors)
        return self

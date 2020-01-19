"""
    Created by 吴闻（gawinwu@163.com） on 2020-01-17.
"""

__author__ = '吴闻'

import datetime


# 将unix时间戳格式化为yyyy-mm-dd H:i:s格式字符串
def format_time_long(time_stamp):
    time_array = datetime.datetime.utcfromtimestamp(time_stamp)
    time_style = time_array.strftime("%Y-%m-%d %H:%M:%S")
    return time_style

# coding=utf-8

from flask import jsonify
from flask import make_response
from datetime import datetime, date
from flask.json import JSONEncoder

from mixin import ModelJsonMixin


class JsonResult:
    """
    JSON格式的响应结果对象
    """

    @staticmethod
    def fail(code):
        return JsonResult(False, code, 'System Busy', None).response()

    @staticmethod
    def fail(code, message):
        return JsonResult(False, code, message, None).response()

    @staticmethod
    def success(data):
        return JsonResult(True, 'SUCCESS_RESPONSE', None, data).response()

    def __init__(self, success, code, message, data=None):
        self._success = success if isinstance(success, bool) else False
        self._code = code
        self._message = message
        if isinstance(data, ModelJsonMixin):
            self._data = data.as_dict()
        else:
            self._data = data

    def __str__(self):
        return jsonify({
            'success': self._success,
            'code': self._code,
            'message': self._message,
            'data': self._data
        })

    def response(self):
        resp = make_response(self.__str__())
        resp.headers['Content-Type'] = 'application/json;charset=utf-8'
        return resp


class GenericJSONEncoder(JSONEncoder):
    """
    通用Flask的jsonify的JSON解码自定义实现
    """

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return JSONEncoder.default(self, obj)

from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlathanor import FlaskBaseModel, initialize_flask_sqlathanor

db = SQLAlchemy(model_class=FlaskBaseModel)
db = initialize_flask_sqlathanor(db)


class JsonResult:
    @staticmethod
    def fail(code):
        return JsonResult(False, code, 'System Busy', None).to_json()

    @staticmethod
    def fail(code, message):
        return JsonResult(False, code, message, None).to_json()

    @staticmethod
    def success(data):
        return JsonResult(True, 'OK', None, data).to_json()

    def __init__(self, success, code, message, data=None):
        self._success = success if isinstance(success, bool) else False
        self._code = code
        self._message = message
        self._data = data

    def to_json(self):
        return jsonify({
            'success': self._success,
            'code': self._code,
            'message': self._message,
            'data': self._data
        })

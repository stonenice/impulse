from supports import JsonResult
from models import School
from flask import request


def query_school_list():
    id = request.values.get('id')
    if not id:
        return JsonResult.fail('INVALID_PARAM')
    data = School.query.get(id)
    return JsonResult.success(data)

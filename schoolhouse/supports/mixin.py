from flask import jsonify
from sqlalchemy.orm import class_mapper


class ModelJsonMixin:
    def __init__(self):
        pass

    def __str__(self):
        return jsonify(self.as_dict())

    def as_dict(self):
        columns = [c.key for c in class_mapper(self.__class__).columns]
        return dict((c, getattr(self, c)) for c in columns)

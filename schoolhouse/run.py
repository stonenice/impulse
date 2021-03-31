# coding=utf-8
import config
from flask import Flask
from flask import jsonify
from exts import db
from views import SchoolApi

app = Flask(__name__)
# 加載配置
app.config.from_object(config)
# 配置路由
app.add_url_rule('/', 'index', SchoolApi.query_school_list,methods=['GET'])

if __name__ == '__main__':
    db.init_app(app)
    app.run()

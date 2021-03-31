# coding=utf-8
import os
import base64
import arc4
import pyhocon

conf = pyhocon.ConfigFactory.parse_file(os.getenv('SYS_CFG_PATH'))
safe_pwd = base64.b64decode(conf.get_string('database.mysql.password'))
raw_pwd = arc4.ARC4(os.getenv('SYS_CFG_PWD')).decrypt(safe_pwd)

# ============================= FLASK CONFIG ============================================

DEBUG = True

# sqlalchemy
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8".format(
    user=conf.get_string('database.mysql.user'),
    password=raw_pwd,
    host=conf.get_string('database.mysql.host'),
    port=conf.get_int('database.mysql.port'),
    db='gather',
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

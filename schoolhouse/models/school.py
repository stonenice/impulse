# coding=utf-8
from exts import db
# from sqlalchemy.types import *
import datetime



class School(db.Model):
    __tablename__ = 'edu_school'
    # 自增ID
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True, nullable=False)
    # 创建时间
    gmt_create = db.Column(db.DateTime, default=datetime.datetime.now)
    # 修改時間
    gmt_modified = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    # 是否已删除
    is_deleted = db.Column(db.SmallInteger, default=0)
    # '学校名称',
    school_name = db.Column(db.String(255))
    # '学校类型：幼儿园、小学、初中等',
    school_type = db.Column(db.String(255))
    # '学校所属区域'
    school_edu = db.Column(db.String(255))
    # '学校教育局',
    school_level = db.Column(db.String(255))
    # '学校性质',
    school_nature = db.Column(db.String(255))
    # '学校电话',
    school_phone = db.Column(db.String(255))
    # '城市名称',
    city_name = db.Column(db.String(255))
    # '行政区名称',
    area_name = db.Column(db.String(255))
    # 學校地址
    address_detail = db.Column(db.String(4096))
    # 外部鏈接
    outer_link = db.Column(db.String(4096))
    # 外部ID
    outer_id = db.Column(db.String(1028))
    # 学校标签
    mark_tags = db.Column(db.Text)

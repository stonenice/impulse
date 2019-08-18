#!/usr/bin/python
# encoding:utf-8

from __future__ import print_function
import json
import sxtwl
import damson
from damson.constraint import (Required, DataType, Between)

from flask import Flask, request


class Result(object):

    @staticmethod
    def fail(code, message):
        return Result(False, code, message)

    @staticmethod
    def sys_error(message=None):
        return Result(False, 'SYS_ERROR', message if message else u'系统繁忙，请稍后再试！')

    @staticmethod
    def params_error(message=None):
        return Result(False, 'PARAMS_ERROR', message if message else u'参数校验未通过！')

    @staticmethod
    def success(data):
        return Result(True, 'SUCCESS', 'ok', data=data)

    def __init__(self, success, code, message, data=None):
        self.success = success
        self.code = code,
        self.message = message
        self.data = data

    def __str__(self):
        result = {
            'success': self.success,
            'message': self.message,
            'code': self.code[0],
            'data': self.data
        }
        return json.dumps(result, ensure_ascii=False)


class OnionLunar:
    TIAN_GAN = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    DI_ZHI = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    SHX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
    CN_NUM = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    JQMC = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露",
            "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
    YMC = ["冬月", "腊月", "正月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月"]
    RMC = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八",
           "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]
    SHI_CHEN = {'子时': ('23:00', '00:59'),
                '丑时': ('01:00', '02:59'),
                '寅时': ('03:59', '04：59'),
                '卯时': ('05:00', '06:59'),
                '辰时': ('07:00', '08:59'),
                '巳时': ('09:00', '10:59'),
                '午时': ('11:00', '12:59'),
                '未时': ('13:00', '14:59'),
                '申时': ('15:00', '16:59'),
                '酉时': ('17:00', '18:59'),
                '戊时': ('19:00', '20:59'),
                '亥时': ('21:00', '22:59')
                }

    def __init__(self):
        self.lunar = sxtwl.Lunar()

    @damson.verify(hour=[DataType(int), Between(0, 24)], minute=[DataType(int), Between(0, 60)])
    def shichen(self, hour, minute):
        key = '%02d:%02d' % (hour, minute)
        for text in self.SHI_CHEN:
            interval = self.SHI_CHEN[text]
            begin = interval[0]
            end = interval[1]
            if begin < end:
                if begin >= key <= end:
                    return text
            else:
                if (begin <= key <= '23:59') or ('00:00' <= key <= end):
                    return text
        return None

    @damson.verify(year=[Required(), DataType(int), Between(1901, 2100, eopen=False)],
                   month=[Required(), DataType(int), Between(1, 12, eopen=False)],
                   day=[Required(), DataType(int), Between(1, 31, eopen=False)])
    def s2y_json(self, year, month, day):
        try:
            day = self.lunar.getDayBySolar(year, month, day)
            data = {
                'year': day.y,
                'gzYear': self.TIAN_GAN[day.Lyear2.tg] + self.DI_ZHI[day.Lyear2.dz],
                'month': day.m,
                'leapMonth': day.Lleap,
                'ymcMonth': self.YMC[day.Lmc],
                'gzMonth': self.TIAN_GAN[day.Lmonth2.tg] + self.DI_ZHI[day.Lmonth2.dz],
                'day': day.d,
                'rmcDay': self.RMC[day.Ldi],
                'gzDay': self.TIAN_GAN[day.Lday2.tg] + self.DI_ZHI[day.Lday2.dz]
            }
            result = Result.success(data)
        except Exception as e:
            result = Result.sys_error(e)
        return str(result)

    @damson.verify(year=[Required(), DataType(int), Between(1901, 2100, eopen=False)],
                   month=[Required(), DataType(int), Between(1, 12, eopen=False)],
                   day=[Required(), DataType(int), Between(1, 31, eopen=False)])
    def y2s_json(self, year, month, day):
        try:
            day = self.lunar.getDayByLunar(year, month, day, True)
            data = {
                'year': day.y,
                'gzYear': self.TIAN_GAN[day.Lyear2.tg] + self.DI_ZHI[day.Lyear2.dz],
                'month': day.m,
                'leapMonth': day.Lleap,
                'ymcMonth': self.YMC[day.Lmc],
                'gzMonth': self.TIAN_GAN[day.Lmonth2.tg] + self.DI_ZHI[day.Lmonth2.dz],
                'day': day.d,
                'rmcDay': self.RMC[day.Ldi],
                'gzDay': self.TIAN_GAN[day.Lday2.tg] + self.DI_ZHI[day.Lday2.dz]
            }
            result = Result.success(data)
        except Exception as e:
            result = Result.sys_error(e)
        return result


# +++++++++++++++++ Flask Web ++++++++++++++++++++

app = Flask(__name__)
onion = OnionLunar()


@app.route('/solar2lunar', methods=['GET'])
def solar2lunar():
    try:
        year = int(request.args.get('year'))
        month = int(request.args.get('month'))
        day = int(request.args.get('day'))
        result = onion.s2y_json(year, month, day)
    except Exception as e:
        result = Result.sys_error(e)
    return str(result)


@app.route('/lunar2solar', methods=['GET'])
def lunar2solar():
    try:
        year = int(request.args.get('year'))
        month = int(request.args.get('month'))
        day = int(request.args.get('day'))
        result = onion.y2s_json(year, month, day)
    except Exception as e:
        result = Result.sys_error(e)
    return str(result)


if __name__ == '__main__':
    app.run('127.0.0.1', port=15954, debug=False)

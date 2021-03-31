#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Feb-24-21 23:04
# @Author  : Kelly Hwong (dianhuangkan@gmail.com)

import os
import time
from win32_setctime import setctime


def make_timestring(timestamp):
    """把时间戳转化为时间"""
    timestruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timestruct)


def get_filesize(filepath, units="M", system="win"):
    """获取文件的大小,结果保留两位小数，单位为MB"""
    base = 1024 if system == "win" else 1000

    f_size = os.path.getsize(filepath)

    assert units in ['M', 'K', 'B']
    if units == 'B':
        return f_size
    else:
        f_size /= base
        if units == 'K':
            return f_size
        else:
            f_size /= base
            if units == 'M':
                return f_size


def print_timestring(filepath):
    # 获取文件的访问时间
    t = os.path.getatime(filepath)
    print(make_timestring(t))
    # 获取文件的创建时间
    t = os.path.getctime(filepath)
    print(make_timestring(t))
    # 获取文件的修改时间
    t = os.path.getmtime(filepath)
    print(make_timestring(t))


def main():
    filepath_origin = "AI_2021-02-24-10-18-13-646.png"
    stat_origin = os.stat(filepath_origin)
    print(stat_origin)
    print_timestring(filepath_origin)
    filepath = "AI_2021-02-24-10-18-13-646-quality-95.jpg"
    stat = os.stat(filepath)
    print(stat)
    print_timestring(filepath)
    # Set atime and mtime
    os.utime(filepath, (stat_origin.st_atime, stat_origin.st_mtime))
    # Set ctime
    setctime(filepath, stat_origin.st_ctime)
    print_timestring(filepath)

    # units = "M"
    # f_size = get_filesize(filepath, units=units)
    # print(f_size, units+"B")


if __name__ == "__main__":
    main()

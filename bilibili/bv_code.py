#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Mar-26-20 01:49
# @Author  : Your Name (you@example.org)
# @RefLink : https://www.zhihu.com/question/381784377/answer/1099438784

import os

# base58
table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
s = [11, 10, 3, 8, 4, 6]
xor = 177451812  # 异或数 0001 0111 0111 ...
add = 8728348608  # 和数


class BV_Encoder(object):
    def __init__(self):
        pass

    def decode(parameter_list):
        pass

    def encode(parameter_list):
        pass


def decode():
    pass


def encode(x):
    """
    Inputs:
        x: 整型数，视频的av号，不要av
    Output:
        bv号，带“BV”
    """
    x = (x ^ xor)+add
    r = list('BV1  4 1 7  ')
    for i in range(6):
        r[s[i]] = table[x//58**i % 58]
    bv = ''.join(r)
    return bv


def main():
    # https://www.bilibili.com/video/av74395770/
    print(encode(74395770))


if __name__ == "__main__":
    main()

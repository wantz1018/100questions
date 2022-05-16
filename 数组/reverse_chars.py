"""
-*- coding: utf-8 -*-
@Time: 2022/5/8 9:54
@Author: Wantz
@Email: wantz@foxmail.com
url:https://www.lanqiao.cn/courses/1512/learning/?id=16663
"""

class ReverseString(object):

    def reverse(self, chars):
        if chars is None or chars == []:
            return chars
        chars.reverse()
        return chars


print(ReverseString().reverse(['1', '2', '3']))

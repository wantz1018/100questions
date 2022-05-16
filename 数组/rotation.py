"""
-*- coding: utf-8 -*-
@Time: 2022/5/8 9:04
@Author: Wantz
@Email: wantz@foxmail.com
url:https://www.lanqiao.cn/courses/1512/learning/?id=16661
"""


class Rotation(object):
    def is_substring(self, s1, s2):
        return s1 in s2

    def is_rotation(self, s1, s2):
        if s1 is None or s2 is None:
            return False
        if len(s1) != len(s2):
            return False
        return self.is_substring(s1, s2 + s2)


print(Rotation().is_rotation(input(), input()))

"""
-*- coding: utf-8 -*-
@Time: 2022/5/7 14:50
@Author: Wantz
@Email: wantz@foxmail.com 
"""


class UniqueChars(object):

    def has_unique_chars(self, string):
        if string == None:
            return False
        return len(set(string)) == len(string)


T = UniqueChars()
print(T.has_unique_chars(''))

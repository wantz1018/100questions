"""
-*- coding: utf-8 -*-
@Time: 2022/5/8 8:56
@Author: Wantz
@Email: wantz@foxmail.com
url:https://www.lanqiao.cn/courses/1512/learning/?id=16660
"""


class Permutations(object):

    def is_permutation(self, str1, str2):
        if str1 is None or str2 is None or str1 == '' or str2 == '':
            return False
        return sorted(x for x in str1) == sorted(y for y in str2)


print(Permutations().is_permutation(input(), input()))
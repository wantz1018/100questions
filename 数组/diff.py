"""
-*- coding: utf-8 -*-
@Time: 2022/5/8 10:03
@Author: Wantz
@Email: wantz@foxmail.com
url:https://www.lanqiao.cn/courses/1512/learning/?id=16664
"""


class Solution(object):

    def find_diff(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError
        list1 = list(str1)
        list2 = list(str2)
        while len(list1) != 0 and len(list2) != 0:
            for i in range(len(list1)):
                if list1[i] in list2:
                    list2.remove(list1[i])
                    list1.remove(list1[i])
                    break
        return list1[0] if len(list1) != 0 else list2[0]


print(Solution().find_diff(input(), input()))
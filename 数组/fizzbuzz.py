"""
-*- coding: utf-8 -*-
@Time: 2022/5/8 10:30
@Author: Wantz
@Email: wantz@foxmail.com
url:https://www.lanqiao.cn/courses/1512/learning/?id=16786
"""


class Solution(object):

    def fizz_buzz(self, num):
        if num is None:
            raise TypeError
        if num < 1:
            raise ValueError
        ans = []
        for i in range(1, num+1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')
            elif i % 3 == 0:
                ans.append('Fizz')
            elif i % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(i))
        return ans


print(Solution().fizz_buzz(int(input())))
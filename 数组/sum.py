"""
-*- coding: utf-8 -*-
@Time: 2022/5/8 10:21
@Author: Wantz
@Email: wantz@foxmail.com
url:https://www.lanqiao.cn/courses/1512/learning/?id=16725
"""


class Solution(object):

    def two_sum(self, nums, val):
        if nums is None or val is None:
            raise TypeError
        if not nums:
            raise ValueError
        for i in range(len(nums) - 1):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == val:
                    return [i, j]
        return None


print(Solution().two_sum( [], 7))

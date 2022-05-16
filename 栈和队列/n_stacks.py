"""
-*- coding: utf-8 -*-
@Time: 2022/5/15 14:34
@Author: Wantz
@Email: wantz@foxmail.com
url:https://www.lanqiao.cn/courses/1512/learning/?id=16837
"""


class Stacks(object):
    def __init__(self, num_stacks, stack_size):
        self.stack = []
        for x in range(num_stacks):
            self.stack.append([])
        self.stack_size = stack_size

    def abs_index(self, stack_index):
        return len(self.stack[stack_index - 1])

    def push(self, stack_index, data):
        if len(self.stack[stack_index - 1]) == self.stack_size:
            raise Exception
        self.stack[stack_index - 1].append(data)

    def pop(self, stack_index):
        if len(self.stack[stack_index - 1]) == 0:
            raise Exception
        return self.stack[stack_index - 1].pop(-1)

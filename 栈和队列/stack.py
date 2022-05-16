"""
-*- coding: utf-8 -*-
@Time: 2022/5/15 15:07
@Author: Wantz
@Email: wantz@foxmail.com
url:https://www.lanqiao.cn/courses/1512/learning/?id=16838
"""


class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):

    def __init__(self, top=None):
        self.top = top
        pass

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return None
        else:
            ans = self.top.data
            self.top = self.top.next
            return ans
        pass

    def peek(self):
        return self.top.data

    def is_empty(self):
        return self.top is None


S = Stack()
S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)
S.push(6)
S.push(7)
print(S.peek())
print(S.is_empty())
print(S.pop())
print(S.peek())
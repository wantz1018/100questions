"""
-*- coding: utf-8 -*-
@Time: 2022/5/8 10:38
@Author: Wantz
@Email: wantz@foxmail.com
url:https://www.lanqiao.cn/courses/1512/learning/?id=16795
"""


class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return self.data


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        current = self.head  # 记得保存下头结点
        count = 0
        while current is not None:  # 只要头结点为空，则继续循环
            count += 1
            current = current.next_node
        return count

    def insert_to_front(self, data):
        node = Node(data=data)
        node.next_node = self.head
        self.head = node
        return data

    def append(self, data):
        tail = self.head
        while tail.next_node is not None:
            tail = tail.next_node
        node = Node(data=data)
        tail.next_node = node
        return data

    def find(self, data):
        index = self.head
        while index.next_node is not None:
            if index.data == data:
                return index
            index = index.next_node
        return None

    # todo:不知道怎么删除
    def delete(self, data):
        current = self.head
        previous = None  # 初始值
        found = False
        while not found:  # 只要没找到待删除的值
            if current.data == data:
                found = True
            else:
                previous = current  # 若没找到，则向前挪动
                current = current.next_node
        if previous is None:  # 在找到待删除节点后，若删除的是头结点
            self.head = current.next_node  # 则直接将头指针指向后一个节点即可
        else:  # 若删除非头结点，则直接指向后一个即可
            previous = current.next_node

    #
    def print_list(self):
        index = self.head
        while index.next_node is not None:
            print(index.data)
            index = index.next_node
        print(index.data)

    def get_all_data(self):
        ans = []
        index = self.head
        while index.next_node is not None:
            ans.append(index.data)
            index = index.next_node
        ans.append(index.data)
        return ans


L = LinkedList()
L.insert_to_front('k')
L.insert_to_front('l')
L.append('e')
print(len(L))
print(L.get_all_data())
print(L.find('k'))
# fixme:看看吧
L.delete('k')
L.print_list()
print(L.get_all_data())

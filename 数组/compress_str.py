"""
-*- coding: utf-8 -*-
@Time: 2022/5/8 9:24
@Author: Wantz
@Email: wantz@foxmail.com
url:https://www.lanqiao.cn/courses/1512/learning/?id=16662
"""


class CompressString(object):

    def compress(self, string):
        if string is None or string == '':
            return string
        text = string
        words = []
        counts = []
        ans = ''
        for x in text:
            if len(words) == 0:
                words.append(x)
                counts.append(1)
            elif words[-1] != x:
                words.append(x)
                counts.append(1)
            else:
                counts[-1] += 1

        for i in range(len(words)):
            ans += words[i] + str(counts[i])
            if ans[-1] == '1':
                ans = ans[:-1]
        if len(ans) >= len(string):
            return string
        else:
            return ans


print(CompressString().compress(input('输入字符串：')))

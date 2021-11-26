#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/767. Reorganize String/main.py
# @DATE: 2021/11/26 Fri
# @TIME: 17:52:59
#
# @DESCRIPTION: 767


import math
import collections


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count_dict = collections.Counter(s)
        if (max(char_count_dict.values()) > math.ceil(len(s)/2)):
            return ""
        char_counts = char_count_dict.most_common()
        chars_str = "".join([str(char_count[0]*char_count[1]) \
            for char_count in char_counts])
        list1 = list(chars_str[0:math.ceil(len(s)/2)])
        list2 = list(chars_str[math.ceil(len(s)/2):])
        for i in range(len(list2), -1, -1):
            if (list1):
                list2.insert(i, list1.pop())
        return "".join(list2)


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    _input = "aab"
    print("输入：{}".format(str(_input)))
    result = solution.reorganizeString(_input)
    print("结果：{}".format(str(result)))
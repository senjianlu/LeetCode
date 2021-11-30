#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/884. Uncommon Words from Two Sentences/main.py
# @DATE: 2021/11/30 Tue
# @TIME: 16:25:07
#
# @DESCRIPTION: 884


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        return [w for w in list(set(s1.split(" "))^set(s2.split(" "))) \
            if (s1.split(" ").count(w) <= 1 and s2.split(" ").count(w) <= 1)]


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    s1 = "s z z z s"
    s2 = "s z ejt"
    print("输入：{}".format(s1+", "+s2))
    result = solution.uncommonFromSentences(s1, s2)
    print("结果：{}".format(str(result)))
#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/151. Reverse Words in a String/main.py
# @DATE: 2021/11/27 周六
# @TIME: 11:04:33
#
# @DESCRIPTION: 151


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        _s = ""
        for word in s.split(" "):
            if (word):
                _s = word + " " + _s
        return _s.strip()


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    _input = "the sky is blue "
    print("输入：{}".format(str(_input)))
    result = solution.reverseWords(_input)
    print("结果：{}".format(str(result)))
#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/696. Count Binary Substrings/main.py
# @DATE: 2021/12/01 Wed
# @TIME: 10:07:23
#
# @DESCRIPTION: 696


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        last_char = s[0]
        char_counts = [1]
        for char in s[1:]:
            if (char == last_char):
                char_counts[-1] += 1
            else:
                last_char = char
                char_counts.append(1)
        count = 0
        for i in range(1, len(char_counts)):
            count += min(char_counts[i-1], char_counts[i])
        return count


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    _input = "00110"
    print("输入：{}".format(str(_input)))
    result = solution.countBinarySubstrings(_input)
    print("结果：{}".format(str(result)))
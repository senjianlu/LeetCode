#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/594. Longest Harmonious Subsequence/main.py
# @DATE: 2021/11/23 Tue
# @TIME: 09:32:09
#
# @DESCRIPTION: 594


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def findLHS(self, nums) -> int:
        repeat_count_dict = {}
        for num in nums:
            if (num not in repeat_count_dict.keys()):
                repeat_count_dict[num] = 1
            else:
                repeat_count_dict[num] += 1
        max_len = 0
        for num in repeat_count_dict.keys():
            if ((num+1) in repeat_count_dict.keys()):
                _len = repeat_count_dict[num] + repeat_count_dict[num+1]
                if (_len > max_len):
                    max_len = _len
        return max_len


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    _input = [1, 2, 2, 1]
    print("输入：{}".format(str(_input)))
    result = solution.findLHS(_input)
    print("结果：{}".format(str(result)))
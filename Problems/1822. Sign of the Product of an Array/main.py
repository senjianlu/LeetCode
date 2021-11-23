#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/1822. Sign of the Product of an Array/main.py
# @DATE: 2021/11/23 Tue
# @TIME: 13:34:15
#
# @DESCRIPTION: 1822


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def arraySign(self, nums) -> int:
        negative_num_count = 0
        for num in nums:
            if (num == 0):
                return 0
            elif(num < 0):
                negative_num_count += 1
        if (negative_num_count%2 == 1):
            return -1
        else:
            return 1


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    _input = [-1, -2, -3, -4, 3, 2, 1]
    print("输入：{}".format(str(_input)))
    result = solution.arraySign(_input)
    print("结果：{}".format(str(result)))
#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/1770. Maximum Score from Performing Multiplication Operations/main.py
# @DATE: 2021/11/26 Fri
# @TIME: 17:52:42
#
# @DESCRIPTION: 1770


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def maximumScore(self, nums: [int], multipliers: [int]) -> int:
        n, m = len(nums), len(multipliers)
        x2_list = [[None]*(m+1) for _ in range(m+1)]
        # l 为从左向右的指针索引，r 为从右向左的指针索引
        def get_max(l, r):
            if (x2_list[l][r] != None):
                return x2_list[l][r]
            if ((l+r) == m):
                return 0
            x2_list[l][r] = max(
                nums[l]*multipliers[l+r]+get_max(l+1, r),
                nums[-1-r]*multipliers[l+r]+get_max(l, r+1))
            return x2_list[l][r]
        return get_max(0, 0)


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3]
    multipliers = [3,2,1]
    print("输入：{}".format(str(nums)+str(multipliers)))
    result = solution.maximumScore(nums, multipliers)
    print("结果：{}".format(str(result)))
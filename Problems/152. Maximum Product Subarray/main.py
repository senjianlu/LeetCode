#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/152. Maximum Product Subarray/main.py
# @DATE: 2021/12/03 Fri
# @TIME: 14:18:44
#
# @DESCRIPTION: 152


from functools import reduce


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def maxProduct(self, nums) -> int:
        def get_max(_nums):
            negative_num_indexes = [i for i in range(len(_nums)) if _nums[i] < 0]
            if (len(negative_num_indexes) == 1):
                if (negative_num_indexes[0] == 0):
                    _max = reduce(lambda a,b:a*b,_nums[1:]) if len(_nums) > 1 else _nums[negative_num_indexes[0]]
                elif(negative_num_indexes[0] == (len(_nums)-1)):
                    _max = reduce(lambda a,b:a*b,_nums[0:-1]) if len(_nums) > 1 else _nums[negative_num_indexes[0]]
                else:
                    _max = max(reduce(lambda a,b:a*b,_nums[negative_num_indexes[0]+1:]), reduce(lambda a,b:a*b,_nums[0:negative_num_indexes[0]]))
            else:
                _max = max(reduce(lambda a,b:a*b,_nums[negative_num_indexes[0]+1:]), reduce(lambda a,b:a*b,_nums[0:negative_num_indexes[-1]]))
            return _max

        _nums = []
        _max = max(nums)
        for i in range(len(nums)):
            if (nums[i] != 0):
                _nums.append(nums[i])
                if (i != (len(nums)-1)):
                    continue
            if (_nums):
                product = reduce(lambda a,b:a*b,_nums)
                if (product < 0):
                    product = get_max(_nums)
                _max = max(product, _max)
                _nums = []
        return _max


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    _input = [-3,-1,-1]
    # _input = [-2, 0, -1]
    _input = [-2]
    _input = [1,0,-1,2,3,-5,-2]
    print("输入：{}".format(str(_input)))
    result = solution.maxProduct(_input)
    print("结果：{}".format(str(result)))
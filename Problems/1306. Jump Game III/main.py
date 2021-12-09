#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/1306. Jump Game III/main.py
# @DATE: 2021/12/09 Thu
# @TIME: 15:14:04
#
# @DESCRIPTION: 1306


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def canReach(self, arr, start: int) -> bool:
        arrived = []
        def dfs(arr, i):
            if (i in arrived or i < 0 or i >= len(arr)):
                return False
            arrived.append(i)
            if (arr[i] == 0):
                return True
            return (dfs(arr, i+arr[i]) or dfs(arr, i-arr[i]))
        return dfs(arr, start)


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    arr = [3,0,2,1,2,0]
    start = 2
    print("输入：{}".format(str(arr)+", "+str(start)))
    result = solution.canReach(arr, start)
    print("结果：{}".format(str(result)))
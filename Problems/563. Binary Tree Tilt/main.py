#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/563. Binary Tree Tilt/main.py
# @DATE: 2021/12/08 Wed
# @TIME: 16:44:18
#
# @DESCRIPTION: 563


"""
@description: 树类
-------
@param:
-------
@return:
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node):
            if (not node):
                return 0
            else:
                nonlocal result
                l = dfs(node.left)
                r = dfs(node.right)
                result += abs(l-r)
                return node.val + l + r
        dfs(root)
        return result


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    _input = []
    print("输入：{}".format(str(_input)))
    result = solution.findTilt(_input)
    print("结果：{}".format(str(result)))
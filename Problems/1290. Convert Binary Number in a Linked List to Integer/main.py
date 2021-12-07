#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/1290. Convert Binary Number in a Linked List to Integer/main.py
# @DATE: 2021/12/07 周二
# @TIME: 21:02:22
#
# @DESCRIPTION: 1290


"""
@description: 链表类
-------
@param:
-------
@return:
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num_2 = ""
        while head:
            num_2 += str(head.val)
            head = head.next
        return int(num_2, 2)


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    _input = [1, 0]
    print("输入：{}".format(str(_input)))
    result = solution.getDecimalValue(_input)
    print("结果：{}".format(str(result)))